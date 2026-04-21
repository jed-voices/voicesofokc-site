# VOICES of OKC Launch Notes

## What this package fixes
- Header is cleaner and more streamlined.
- Navigation is all caps.
- `VOICES of OKC` formatting is applied through the core site build.
- Episode titles are styled in all caps.
- Student photos are integrated into the homepage.
- Internal navigation now includes a real `/episodes/` page.
- The custom media player no longer depends on weekly local MP3 uploads.
- The site is configured for `www.voicesofokc.com`.

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
- https://www.voicesofokc.com/
- https://www.voicesofokc.com/about/
- https://www.voicesofokc.com/sponsors/
- https://www.voicesofokc.com/episodes/
- https://www.voicesofokc.com/episodes/mayor-david-holt/
- https://www.voicesofokc.com/episodes/derrick-sier/
- https://www.voicesofokc.com/assets/images/featured-episode-8.jpg
