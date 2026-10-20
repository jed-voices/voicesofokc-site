# Feed-content security regression tests

Run from the repository root:

```sh
python3 -m unittest discover -s tests -v
node tests/test_summary_rendering.cjs
node --check assets/js/episodes.js
node --check assets/js/player.js
git diff --check
```

The Python integration test runs the actual publisher twice with an in-memory
feedparser fixture, cleared environment, disabled YouTube configuration, blocked
URL/socket requests, and output confined to a temporary directory. It does not
fetch Podbean data, contact Google, publish, or push. No additional packages are
required. The helper tests load definitions without the publisher entry point.

The Node tests execute production summary and archive-rendering definitions in a
VM with a minimal DOM test double. DOM element creation is forbidden during text
normalization. Tests cover six hostile summary forms in both consumers, escaped
archive output, ordinary text, nulls, truncation and retained episode links.
These are isolated logic tests, not a real-browser or live-deployment test.

Python coverage includes entity decoding, script/style removal, JSON-LD round
trips with Unicode and backslashes, embedded comment markers in old JSON-LD,
ambiguous/missing/reversed markers, and two-run publication stability. Normal
formatted show notes, summary text, audio URLs and JSON output are checked.

Verification on 2026-10-20: all six Python tests and both JavaScript suites pass;
JavaScript syntax and whitespace checks pass. The same regression tests fail
against original commit c2f141eb4301ee46a0141e191e5d73dd03a44a32, detecting the
unsafe DOM parsing and archive marker/replacement behavior.

The prepared changes cover only the summary-to-HTML and archive JSON-LD findings.
Dependency/publishing permissions and transcription URL validation are unchanged.
Before a future deployment, run an isolated browser smoke test and verify the
production hosting/source configuration. No deployment is part of these tests.
