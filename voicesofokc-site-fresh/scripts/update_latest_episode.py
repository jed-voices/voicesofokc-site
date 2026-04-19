from pathlib import Path
import json
import os
from datetime import datetime, timezone
from urllib.parse import urlparse

import feedparser

feed_url = os.environ.get("PODBEAN_FEED_URL", "").strip()
spotify_url = os.environ.get("SPOTIFY_URL", "").strip()
apple_url = os.environ.get("APPLE_URL", "").strip()
youtube_url = os.environ.get("YOUTUBE_URL", "").strip()

out_path = Path("assets/data/latest-episode.json")
out_path.parent.mkdir(parents=True, exist_ok=True)

def find_audio_url(entry):
    enclosures = entry.get("enclosures", []) or []
    for enc in enclosures:
        href = enc.get("href")
        if href:
            return href

    links = entry.get("links", []) or []
    for link in links:
        href = link.get("href")
        rel = link.get("rel")
        ltype = (link.get("type") or "").lower()
        if href and (rel == "enclosure" or "audio" in ltype or href.lower().endswith((".mp3", ".m4a", ".aac", ".ogg"))):
            return href
    return ""

if not feed_url:
    raise SystemExit("PODBEAN_FEED_URL is missing.")

feed = feedparser.parse(feed_url)
if feed.bozo and not getattr(feed, "entries", None):
    raise SystemExit(f"Feed could not be parsed: {feed.bozo_exception}")

if not feed.entries:
    raise SystemExit("Feed has no entries.")

entry = feed.entries[0]
audio_url = find_audio_url(entry)

payload = {
    "title": entry.get("title", "").strip(),
    "audio_url": audio_url,
    "episode_url": entry.get("link", "").strip(),
    "spotify_url": spotify_url,
    "apple_url": apple_url,
    "youtube_url": youtube_url,
    "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    "feed_url": feed_url,
}

out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
print(f"Wrote {out_path} from {feed_url}")
