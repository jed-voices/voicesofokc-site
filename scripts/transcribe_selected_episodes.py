#!/usr/bin/env python3
"""Create timestamped transcript data for selected VOICES of OKC episodes.

This is an editorial build helper, not part of the scheduled Podbean sync.
It requires mlx-whisper and ffmpeg and is intended to run on Apple silicon.
"""

import argparse
import json
import os
import re
import tempfile
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import mlx_whisper


EPISODES_PATH = Path("assets/data/episodes.json")
TRANSCRIPTS_DIR = Path("assets/data/transcripts")
DEFAULT_MODEL = "mlx-community/whisper-large-v3-turbo"

PRIORITY_SLUGS = [
    "from-policy-to-people-the-privilege-of-leading-oklahoma-city",
    "what-oklahoma-city-cannot-lose-as-it-grows-with-brad-carter",
    "hope-in-hard-places-jabee-williams-on-okc-violence-and-hope",
    "rethinking-justice-in-oklahoma-public-safety-real-reform-and-redemption",
    "community-through-conversation-mike-hearne-on-storytelling-in-oklahoma-city",
    "beyond-winning-bryan-fetzer-on-pressure-and-perspective-in-okc",
    "over-22-000-babies-later-what-one-doctor-learned-about-life-and-hope",
    "use-wisely-adam-coury-on-leadership-learning-and-the-next-generation",
    "from-misnomer-to-mentorship-derrick-sier-on-rebuilding-identity-in-oklahoma-city",
    "growing-hope-in-oklahoma-brooke-freeman-on-farming-faith-and-community",
]


def slug_from_episode(episode):
    return str(episode.get("site_path", "")).strip("/").split("/")[-1]


def normalize_text(value):
    return re.sub(r"\s+", " ", str(value or "")).strip()


def download_audio(url, destination):
    request = urllib.request.Request(url, headers={"User-Agent": "VOICES-of-OKC-transcript-builder/1.0"})
    with urllib.request.urlopen(request, timeout=120) as response, destination.open("wb") as output:
        while chunk := response.read(1024 * 1024):
            output.write(chunk)


def transcribe_episode(episode, model):
    slug = slug_from_episode(episode)
    title = normalize_text(episode.get("title"))
    guest = normalize_text(episode.get("guest_name"))
    organization = normalize_text(episode.get("guest_organization"))
    prompt_parts = [
        "VOICES of OKC is an Oklahoma City interview podcast.",
        f"Episode title: {title}.",
    ]
    if guest:
        prompt_parts.append(f"Guest: {guest}.")
    if organization:
        prompt_parts.append(f"Organization: {organization}.")

    with tempfile.TemporaryDirectory(prefix="voices-transcript-") as temp_dir:
        audio_path = Path(temp_dir) / f"{slug}.mp3"
        print(f"Downloading {title}", flush=True)
        download_audio(episode["audio_url"], audio_path)
        print(f"Transcribing {title}", flush=True)
        result = mlx_whisper.transcribe(
            str(audio_path),
            path_or_hf_repo=model,
            language="en",
            initial_prompt=" ".join(prompt_parts),
            condition_on_previous_text=True,
            word_timestamps=False,
            verbose=False,
        )

    segments = []
    for segment in result.get("segments", []):
        text = normalize_text(segment.get("text"))
        if not text:
            continue
        segments.append(
            {
                "start": round(float(segment.get("start", 0)), 2),
                "end": round(float(segment.get("end", 0)), 2),
                "text": text,
            }
        )

    return {
        "episode_title": title,
        "episode_slug": slug,
        "source": "Published episode audio",
        "language": "en",
        "review_status": "machine-generated",
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "model": model,
        "segments": segments,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--slug", action="append", help="Transcribe one or more episode slugs")
    parser.add_argument("--model", default=os.environ.get("WHISPER_MODEL", DEFAULT_MODEL))
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    data = json.loads(EPISODES_PATH.read_text(encoding="utf-8"))
    episodes = {slug_from_episode(item): item for item in data.get("episodes", [])}
    selected = args.slug or PRIORITY_SLUGS
    missing = [slug for slug in selected if slug not in episodes]
    if missing:
        raise SystemExit(f"Unknown episode slug(s): {', '.join(missing)}")

    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    for slug in selected:
        destination = TRANSCRIPTS_DIR / f"{slug}.json"
        if destination.exists() and not args.overwrite:
            print(f"Skipping existing transcript: {slug}", flush=True)
            continue
        episode = episodes[slug]
        if not episode.get("audio_url"):
            raise SystemExit(f"Episode has no audio URL: {slug}")
        payload = transcribe_episode(episode, args.model)
        destination.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Wrote {destination} ({len(payload['segments'])} segments)", flush=True)


if __name__ == "__main__":
    main()
