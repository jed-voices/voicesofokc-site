from pathlib import Path
import json
import os
from datetime import datetime, timezone

import feedparser

feed_url = os.environ.get("PODBEAN_FEED_URL", "").strip()
spotify_url = os.environ.get("SPOTIFY_URL", "").strip()
apple_url = os.environ.get("APPLE_URL", "").strip()
youtube_url = os.environ.get("YOUTUBE_URL", "").strip()

latest_path = Path("assets/data/latest-episode.json")
episodes_path = Path("assets/data/episodes.json")
latest_path.parent.mkdir(parents=True, exist_ok=True)

def find_audio_url(entry):
    for enc in entry.get("enclosures", []) or []:
        href = enc.get("href")
        if href:
            return href
    for link in entry.get("links", []) or []:
        href = link.get("href")
        rel = link.get("rel")
        ltype = (link.get("type") or "").lower()
        if href and (rel == "enclosure" or "audio" in ltype or href.lower().endswith((".mp3", ".m4a", ".aac", ".ogg"))):
            return href
    return ""

def find_artwork_url(entry, feed):
    image = entry.get("image")
    if isinstance(image, dict) and image.get("href"):
        return image.get("href")
    media_thumbnail = entry.get("media_thumbnail")
    if isinstance(media_thumbnail, list) and media_thumbnail:
        if media_thumbnail[0].get("url"):
            return media_thumbnail[0].get("url")
    itunes_image = entry.get("itunes_image")
    if isinstance(itunes_image, dict) and itunes_image.get("href"):
        return itunes_image.get("href")
    feed_image = getattr(feed.feed, "image", None)
    if isinstance(feed_image, dict) and feed_image.get("href"):
        return feed_image.get("href")
    return ""

def clean_summary(entry):
    summary = entry.get("summary") or entry.get("description") or ""
    summary = " ".join(str(summary).split())
    summary = summary.replace("https://voicesofokc.org", "https://www.voicesofokc.com")
    summary = summary.replace("http://voicesofokc.org", "https://www.voicesofokc.com")
    summary = summary.replace("www.voicesofokc.org", "www.voicesofokc.com")
    summary = summary.replace("voicesofokc.org", "voicesofokc.com")
    summary = summary.replace("info@voicesofokc.org", "info@voicesofokc.com")
    return summary

if not feed_url:
    raise SystemExit("PODBEAN_FEED_URL is missing.")

feed = feedparser.parse(feed_url)
if feed.bozo and not getattr(feed, "entries", None):
    raise SystemExit(f"Feed could not be parsed: {feed.bozo_exception}")
if not feed.entries:
    raise SystemExit("Feed has no entries.")

entries = []
for entry in feed.entries[:12]:
    payload = {
        "title": (entry.get("title") or "").strip(),
        "audio_url": find_audio_url(entry),
        "episode_url": (entry.get("link") or "").strip(),
        "artwork_url": find_artwork_url(entry, feed),
        "summary": clean_summary(entry),
        "published_at": (entry.get("published") or entry.get("updated") or "").strip(),
        "spotify_url": spotify_url,
        "apple_url": apple_url,
        "youtube_url": youtube_url,
    }
    entries.append(payload)

latest = dict(entries[0])
latest["updated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

latest_path.write_text(json.dumps(latest, indent=2), encoding="utf-8")
episodes_path.write_text(json.dumps({"episodes": entries}, indent=2), encoding="utf-8")

print(f"Wrote {latest_path} and {episodes_path}")
