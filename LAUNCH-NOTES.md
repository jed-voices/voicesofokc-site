# VOICES of OKC Launch Notes

## What this fresh package fixes
- Header is cleaner and more streamlined.
- Navigation is all caps.
- `VOICES of OKC` formatting is applied through the core site build.
- Episode titles are styled in all caps.
- Student photos are integrated into the homepage.
- Internal navigation now includes a real `/episodes/` page.
- The custom media player no longer depends on weekly local MP3 uploads.

## How the custom player now works
- Homepage player reads `assets/data/latest-episode.json`
- GitHub Action updates that file from the Podbean feed
- If playback fails at first launch, run the workflow manually once in GitHub Actions

## Broken links that existed before
The main breakages came from missing repo folders and pages:
- `/assets/...`
- `/about/`
- `/sponsors/`
- `/episodes/`

This package includes those folders and pages so the main internal link structure resolves.

## Direct links to test after deploy
- https://voicesofokc.org/
- https://voicesofokc.org/about/
- https://voicesofokc.org/sponsors/
- https://voicesofokc.org/episodes/
- https://voicesofokc.org/episodes/mayor-david-holt/
- https://voicesofokc.org/episodes/derrick-sier/
- https://voicesofokc.org/assets/images/featured-episode-8.jpg
