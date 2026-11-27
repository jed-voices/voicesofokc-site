# Lessons

Short notes a future AI (or future human) should read before planning work on this repo.
Each entry: the date, what went wrong, the strongest form we can give the lesson (a test > a rule > a short note).

---

## 2026-11-24 — "WebFetch is not a bug report"

**What happened.** A review of voicesofokc.com concluded the home-page audio player was stuck on "LOADING LATEST EPISODE…". The report came from an agent whose fetch tool does not execute JavaScript, so it saw the HTML's initial placeholder text before `assets/js/player.js` ran. In a real browser the player hydrates correctly.

**Form of the lesson.**
- **Rule (this file):** Before changing front-end code on the basis of a reported bug, confirm the symptom in a real browser (the in-app browser pane, Safari, or Chrome with DevTools). Server-rendered HTML snapshots from WebFetch / curl / the `web-fetch` agent do not count as evidence that client-rendered UI is broken — they can only show the pre-hydration state.
- **Test:** none added. This is a rule about diagnostics, not a property of the code that a unit test can assert.

**Why it matters.** Writing a fix for a non-bug is a worse outcome than the non-bug itself: it changes live code without reason, costs time, and burns trust in the review process.

---

## 2026-11-24 — Featured-episode kicker goes blank when sync omits `guest_name`

**What happened.** The Podbean sync for the Janelle Nightingale episode produced a `latest-episode.json` with no `guest_name`, `guest_title`, or `guest_organization`. The home-page kicker (`#featuredEpisodeGuest`) in `assets/js/player.js` only populated when `guest_name` was truthy, so it stayed empty. The archive card used a `deriveGuest()` helper in `assets/js/episodes.js` that fell back to the title's `|` or `: <name> on …` form, but the player did not.

**Form of the lesson.**
- **Test:** `tests/test_featured_guest_fallback.cjs` asserts `deriveGuest` in `player.js` returns the pipe-form name for `"Seeing People Beyond Their Labels | Janelle Nightingale"`, returns the `: <name> on …` form for Mayor Holt-style titles, returns the hardcoded `guest_name` when present, and returns `VOICES of OKC` as the last-resort default. The test "bites": a bogus return value from the pipe branch fails it.
- **Rule:** Both `player.js` and `episodes.js` must keep their `deriveGuest()` helpers in sync. If one is changed, change the other.
- **Fix shipped in:** `fix/featured-episode-guest-kicker-fallback`.

**Why it matters.** The kicker is the first line a visitor reads next to the featured conversation. A blank kicker reads as "this show is broken."

---

## Policy: how to add a lesson

1. If a test can assert the property, write the test. Reference it here with its filename.
2. If a test cannot hold it (a workflow rule, an outside-system behavior), write the rule here in plain English, and add it to `~/.claude/CLAUDE.md` or the project `AGENTS.md` if it should apply beyond this repo.
3. Date every entry. Short beats long. Delete an entry only when its rule has moved into enforced tooling (a hook or CI job) that would catch the same mistake automatically.
