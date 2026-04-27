import json
import os
import re
import unicodedata
from datetime import datetime, timezone
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

import feedparser

feed_url = os.environ.get("PODBEAN_FEED_URL", "").strip()
spotify_url = os.environ.get("SPOTIFY_URL", "").strip()
apple_url = os.environ.get("APPLE_URL", "").strip()
youtube_url = os.environ.get("YOUTUBE_URL", "").strip()

site_origin = os.environ.get("SITE_ORIGIN", "https://www.voicesofokc.com").rstrip("/")
latest_path = Path("assets/data/latest-episode.json")
episodes_path = Path("assets/data/episodes.json")
sitemap_path = Path("sitemap.xml")
latest_path.parent.mkdir(parents=True, exist_ok=True)

SAFE_INLINE_TAGS = {"strong", "em", "b", "i", "br"}
SAFE_BLOCK_TAGS = {"p", "ul", "ol", "li", "blockquote", "h2", "h3", "h4"}
SAFE_TAGS = SAFE_INLINE_TAGS | SAFE_BLOCK_TAGS | {"a"}
URL_RE = re.compile(r"https?://[^\s<]+")


def normalize_brand_refs(value):
    text = str(value or "")
    replacements = {
        "https://voicesofokc.org": "https://www.voicesofokc.com",
        "http://voicesofokc.org": "https://www.voicesofokc.com",
        "www.voicesofokc.org": "www.voicesofokc.com",
        "voicesofokc.org": "voicesofokc.com",
        "info@voicesofokc.org": "info@voicesofokc.com",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def is_safe_url(value):
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https", "mailto"}


def escape_and_link_text(value):
    text = str(value or "")
    pieces = []
    cursor = 0
    for match in URL_RE.finditer(text):
        url = match.group(0).rstrip(".,);]")
        trailing = match.group(0)[len(url):]
        pieces.append(escape(text[cursor:match.start()]))
        href = escape(url, quote=True)
        pieces.append(f'<a href="{href}" target="_blank" rel="noreferrer">{escape(url)}</a>')
        pieces.append(escape(trailing))
        cursor = match.end()
    pieces.append(escape(text[cursor:]))
    return "".join(pieces)


class ShowNotesSanitizer(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.skip_depth = 0
        self.link_depth = 0

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag in {"script", "style"}:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag == "b":
            tag = "strong"
        if tag == "i":
            tag = "em"
        if tag not in SAFE_TAGS:
            return
        if tag == "a":
            href = ""
            for name, value in attrs:
                if name.lower() == "href":
                    href = str(value or "").strip()
                    break
            if not href or not is_safe_url(href):
                return
            self.link_depth += 1
            safe_href = escape(href, quote=True)
            self.parts.append(f'<a href="{safe_href}" target="_blank" rel="noreferrer">')
            return
        if tag == "br":
            self.parts.append("<br />")
            return
        self.parts.append(f"<{tag}>")

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in {"script", "style"}:
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if self.skip_depth:
            return
        if tag == "b":
            tag = "strong"
        if tag == "i":
            tag = "em"
        if tag == "a":
            if self.link_depth:
                self.parts.append("</a>")
                self.link_depth -= 1
            return
        if tag in SAFE_TAGS and tag != "br":
            self.parts.append(f"</{tag}>")

    def handle_data(self, data):
        if self.skip_depth:
            return
        if self.link_depth:
            self.parts.append(escape(data))
        else:
            self.parts.append(escape_and_link_text(data))

    def get_html(self):
        while self.link_depth:
            self.parts.append("</a>")
            self.link_depth -= 1
        return "".join(self.parts).strip()


def plain_text_to_html(value):
    text = normalize_brand_refs(value).replace("\r\n", "\n").replace("\r", "\n")
    blocks = [block.strip() for block in re.split(r"\n{2,}", text) if block.strip()]
    if not blocks and text.strip():
        blocks = [text.strip()]
    paragraphs = []
    for block in blocks:
        lines = [line.strip() for line in block.split("\n")]
        paragraphs.append(f"<p>{'<br />'.join(escape_and_link_text(line) for line in lines if line)}</p>")
    return "\n".join(paragraphs)


def sanitize_show_notes(value):
    raw = normalize_brand_refs(value)
    if not raw.strip():
        return "<p>Show notes will appear here once Podbean publishes them for this episode.</p>"
    if "<" not in raw and ">" not in raw:
        return plain_text_to_html(raw)
    sanitizer = ShowNotesSanitizer()
    sanitizer.feed(raw)
    html = sanitizer.get_html()
    if not html:
        return "<p>Show notes will appear here once Podbean publishes them for this episode.</p>"
    if not re.search(r"</?(p|ul|ol|li|blockquote|h[2-4])\b", html):
        html = f"<p>{html}</p>"
    return html


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
    return normalize_brand_refs(summary)


def find_show_notes(entry):
    for content in entry.get("content", []) or []:
        value = content.get("value") if isinstance(content, dict) else ""
        if value:
            return value
    return entry.get("summary") or entry.get("description") or ""


def strip_html(value):
    parser = ShowNotesSanitizer()
    parser.feed(str(value or ""))
    text = re.sub(r"<[^>]+>", " ", parser.get_html())
    return " ".join(text.split())


def truncate_text(value, limit=160):
    text = " ".join(str(value or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rsplit(" ", 1)[0] + "…"


def slugify(value):
    normalized = unicodedata.normalize("NFKD", value or "")
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_value).strip("-").lower()
    return slug[:96].strip("-") or "latest-episode"


def build_episode_page(episode, show_notes_html):
    title = episode["title"]
    display_title = title.upper()
    description = truncate_text(strip_html(show_notes_html) or episode.get("summary"), 170)
    site_url = episode["site_url"]
    artwork_url = episode.get("artwork_url") or "../../assets/images/featured-episode-8.jpg"
    audio_url = episode.get("audio_url", "")
    published_at = episode.get("published_at", "")

    audio_markup = ""
    if audio_url:
        audio_markup = (
            f'\n              <audio class="episode-audio" controls preload="none" '
            f'src="{escape(audio_url, quote=True)}"></audio>'
        )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{escape(description, quote=True)}" />
  <link rel="canonical" href="{escape(site_url, quote=True)}" />
  <meta property="og:title" content="{escape(title, quote=True)} | VOICES of OKC" />
  <meta property="og:description" content="{escape(description, quote=True)}" />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="{escape(site_url, quote=True)}" />
  <meta property="og:image" content="{escape(artwork_url, quote=True)}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{escape(title, quote=True)} | VOICES of OKC" />
  <meta name="twitter:description" content="{escape(description, quote=True)}" />
  <meta name="twitter:image" content="{escape(artwork_url, quote=True)}" />
  <meta name="theme-color" content="#0F2A44" />
  <link rel="icon" href="../../favicon.ico" />
  <link rel="icon" type="image/png" sizes="32x32" href="../../assets/favicon/favicon-32x32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="../../assets/favicon/favicon-16x16.png" />
  <link rel="apple-touch-icon" href="../../assets/favicon/apple-touch-icon.png" />
  <link rel="manifest" href="../../site.webmanifest" />
  <title>{escape(title)} | VOICES of OKC</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../assets/css/site.css" />
  <link rel="stylesheet" href="../../assets/css/final-overrides.css" />
  <script>(function(w,d,s,n,a){{if(!w[n]){{var l='call,catch,on,once,set,then,track,openCheckout'.split(','),i,o=function(n){{return'function'==typeof n?o.l.push([arguments])&&o:function(){{return o.l.push([n,arguments])&&o}}}},t=d.getElementsByTagName(s)[0],j=d.createElement(s);j.async=!0;j.src='https://cdn.fundraiseup.com/widget/'+a+'';t.parentNode.insertBefore(j,t);o.s=Date.now();o.v=5;o.h=w.location.href;o.l=[];for(i=0;i<8;i++)o[l[i]]=o(l[i]);w[n]=o}}}})(window,document,'script','FundraiseUp','ALZDJCPT');</script>
</head>
<body class="episode-detail-page">
  <a class="skip-link" href="#main-content">Skip to main content</a>
  <header class="site-header">
      <div class="container header-inner">
        <a class="brand" href="../../index.html" aria-label="VOICES of OKC home">
          <img class="brand-mark" src="../../assets/images/voices-icon-civic-navy.png" alt="VOICES of OKC logo icon" />
          <span class="brand-lockup">
            <span class="brand-name">VOICES of OKC</span>
            <span class="brand-tag">A CITY CENTER PODCAST</span>
          </span>
        </a>
        <nav class="nav" aria-label="Primary navigation">
          <a href="../../episodes/" aria-current="page">Episodes</a>
          <a href="../../about/">About</a>
          <a href="../../podcast-team/">Podcast Team</a>
          <a href="../../index.html#guests">Guests</a>
          <a href="../../sponsors/">Sponsors</a>
          <a href="../../index.html#contact">Contact</a>
        </nav>
        <div class="header-cta">
          <a class="button-secondary" href="https://youtube.com/@voicesofokc" target="_blank" rel="noreferrer">Watch Now</a>
        </div>
      </div>
    </header>
  <main id="main-content">
    <section class="hero">
      <div class="container">
        <div class="split-grid episode-detail-grid">
          <article class="image-frame featured-image detail-card-visual episode-artwork">
            <img src="{escape(artwork_url, quote=True)}" alt="{escape(title, quote=True)} artwork for VOICES of OKC" />
          </article>
          <article class="card-surface episode-detail-card">
            <span class="episode-kicker">Latest episode</span>
            <h1 class="episode-title title-with-rule">{escape(display_title)}</h1>
            <div class="episode-meta">
              <span>VOICES of OKC</span>
              <span>{escape(published_at)}</span>
              <span>Show notes from Podbean</span>
            </div>{audio_markup}
            <div class="episode-actions">
              <a class="action-pill" href="{escape(youtube_url, quote=True)}" target="_blank" rel="noreferrer"><img class="platform-icon-img" src="../../assets/images/icon-youtube.png" alt="YouTube icon" /><span class="action-label">YouTube</span></a>
              <a class="action-pill" href="{escape(apple_url, quote=True)}" target="_blank" rel="noreferrer"><img class="platform-icon-img" src="../../assets/images/icon-apple-podcasts.png" alt="Apple Podcasts icon" /><span class="action-label">Apple</span></a>
              <a class="action-pill" href="{escape(spotify_url, quote=True)}" target="_blank" rel="noreferrer"><img class="platform-icon-img" src="../../assets/images/icon-spotify.png" alt="Spotify icon" /><span class="action-label">Spotify</span></a>
            </div>
          </article>
        </div>
      </div>
    </section>
    <section class="section section-tight">
      <div class="container episode-notes-wrap">
        <article class="card-surface">
          <span class="eyebrow">Show notes</span>
          <div class="body-copy episode-notes" id="show-notes">
{show_notes_html}
          </div>
        </article>
      </div>
    </section>
  </main>
  <footer class="site-footer" id="contact">
      <div class="container">
        <div class="footer-grid">
          <div>
            <div class="brand footer-brand">
              <img class="brand-mark" src="../../assets/images/voices-icon-white.png" alt="VOICES of OKC logo icon" />
              <span class="brand-lockup">
                <span class="brand-name footer-brand-name">VOICES of OKC</span>
                <span class="brand-tag footer-brand-tag">A CITY CENTER PODCAST</span>
              </span>
            </div>
            <p class="footer-copy">VOICES of OKC is a student-produced podcast from City Center highlighting leaders, stories, and ideas shaping Oklahoma City.</p>
          </div>
          <div class="footer-column">
            <h2>Explore</h2>
            <a href="../../episodes/">Episodes</a>
            <a href="../../about/">About</a>
            <a href="../../podcast-team/">Podcast Team</a>
            <a href="../../index.html#guests">Guests</a>
          </div>
          <div class="footer-column">
            <h2>Follow</h2>
            <a href="https://youtube.com/@voicesofokc" target="_blank" rel="noreferrer">YouTube</a>
            <a href="https://instagram.com/voicesofokc" target="_blank" rel="noreferrer">Instagram</a>
            <a href="{escape(spotify_url, quote=True)}" target="_blank" rel="noreferrer">Spotify</a>
            <a href="{escape(apple_url, quote=True)}" target="_blank" rel="noreferrer">Apple Podcasts</a>
          </div>
          <div class="footer-column">
            <h2>Contact</h2>
            <span>info@voicesofokc.com</span>
            <span>Oklahoma City, Oklahoma</span>
            <span>Produced through City Center</span>
          </div>
        </div>
        <div class="footer-bottom">
          <span>© 2026 VOICES of OKC. All rights reserved.</span>
          <span>www.voicesofokc.com</span>
        </div>
      </div>
    </footer>
</body>
</html>
"""


def write_episode_page(episode, show_notes_html):
    out_dir = Path(episode["site_path"])
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "index.html"
    out_file.write_text(build_episode_page(episode, show_notes_html), encoding="utf-8")
    return out_file


def update_sitemap(episode):
    loc = episode["site_url"]
    if not sitemap_path.exists():
        sitemap_path.write_text(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"  <url><loc>{escape(loc)}</loc></url>\n"
            "</urlset>\n",
            encoding="utf-8",
        )
        return
    sitemap = sitemap_path.read_text(encoding="utf-8")
    if loc in sitemap:
        return
    insert = f"  <url><loc>{escape(loc)}</loc></url>\n"
    if "</urlset>" in sitemap:
        sitemap = sitemap.replace("</urlset>", insert + "</urlset>")
    else:
        sitemap = sitemap.rstrip() + "\n" + insert
    sitemap_path.write_text(sitemap, encoding="utf-8")

if not feed_url:
    raise SystemExit("PODBEAN_FEED_URL is missing.")

feed = feedparser.parse(feed_url)
if feed.bozo and not getattr(feed, "entries", None):
    raise SystemExit(f"Feed could not be parsed: {feed.bozo_exception}")
if not feed.entries:
    raise SystemExit("Feed has no entries.")

entries = []
for index, entry in enumerate(feed.entries[:12]):
    title = (entry.get("title") or "").strip()
    slug = slugify(title)
    site_path = f"episodes/{slug}/"
    podbean_url = (entry.get("link") or "").strip()
    payload = {
        "title": title,
        "audio_url": find_audio_url(entry),
        "episode_url": podbean_url,
        "podbean_url": podbean_url,
        "artwork_url": find_artwork_url(entry, feed),
        "summary": clean_summary(entry),
        "published_at": (entry.get("published") or entry.get("updated") or "").strip(),
        "spotify_url": spotify_url,
        "apple_url": apple_url,
        "youtube_url": youtube_url,
    }
    if index == 0:
        payload["site_path"] = site_path
        payload["site_url"] = f"{site_origin}/{site_path}"
        payload["episode_url"] = payload["site_url"]
    entries.append(payload)

latest = dict(entries[0])
latest["updated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
latest_show_notes = sanitize_show_notes(find_show_notes(feed.entries[0]))
episode_page = write_episode_page(latest, latest_show_notes)
update_sitemap(latest)

latest_path.write_text(json.dumps(latest, indent=2), encoding="utf-8")
episodes_path.write_text(json.dumps({"episodes": entries}, indent=2), encoding="utf-8")

print(f"Wrote {latest_path}, {episodes_path}, and {episode_page}")
