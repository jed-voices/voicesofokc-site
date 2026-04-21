# VOICES of OKC Website

Static GitHub Pages site for **VOICES of OKC**, a student-produced podcast from City Center.

## Pages included
- `/`
- `/about/`
- `/sponsors/`
- `/episodes/`
- `/episodes/mayor-david-holt/`
- `/episodes/derrick-sier/`

## Brand system preserved
- **Headline font:** Sora
- **Body/UI font:** Inter
- **Colors:** Civic Navy, Slate, Cloud White, Azure

## Refinement pass included
- cleaner, more streamlined header
- navigation text in all caps
- `VOICES of OKC` formatting throughout
- episode titles in all caps
- student photography integrated into the homepage
- internal pages restored so main nav links resolve correctly
- custom audio player wired to a JSON file instead of local weekly MP3 uploads
- subtle monochrome Oklahoma City backdrop layer
- latest episode card synced to Podbean data

## Important upload note
Upload the **contents** of this folder to the repository root so that `assets/`, `about/`, `episodes/`, and `sponsors/` all sit beside `index.html`.

## Custom player + Podbean automation
The site includes a custom player that reads:

`assets/data/latest-episode.json`

A GitHub Action is included at:

`.github/workflows/update-podbean-data.yml`

It runs on a schedule and updates episode JSON from the Podbean feed using:

`PODBEAN_FEED_URL = https://feed.podbean.com/voicesofokc/feed.xml`

If your Podbean feed URL is different, change it in the workflow file.

## Before going live
1. Upload **all files and folders**, not just `index.html`.
2. Confirm the repo root includes `assets/`, `about/`, `episodes/`, and `sponsors/`.
3. Enable GitHub Pages.
4. Keep the `CNAME` file with `www.voicesofokc.com`.
5. If the player is not loading audio, run the workflow manually once from GitHub Actions.
