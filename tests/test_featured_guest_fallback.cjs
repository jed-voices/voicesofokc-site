// Home-page featured-episode kicker must stay populated even when the sync
// omits guest_name. Lesson: live Janelle Nightingale episode shipped without
// guest_name and the kicker went blank. Source of truth: assets/js/player.js.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const root = path.resolve(__dirname, '..');
const source = fs.readFileSync(path.join(root, 'assets/js/player.js'), 'utf8');

const context = vm.createContext({
  document: { getElementById: () => null },
  window: { matchMedia: () => ({ matches: false }) },
});

// Execute player.js production definitions up to loadLatestEpisode so deriveGuest is callable.
const boundary = 'async function loadLatestEpisode';
assert(source.includes(boundary), 'loadLatestEpisode boundary must exist in player.js');
vm.runInContext(source.slice(0, source.indexOf(boundary)), context);
assert.equal(
  vm.runInContext('typeof deriveGuest', context),
  'function',
  'player.js must export a deriveGuest helper so the kicker can fall back to the title when guest_name is missing',
);

const cases = [
  {
    label: 'uses guest_name when present',
    episode: { guest_name: 'Carey Conley', title: 'Life Needs Vision' },
    expected: 'Carey Conley',
  },
  {
    label: 'falls back to pipe form when guest_name is missing (Janelle Nightingale regression)',
    episode: { title: 'Seeing People Beyond Their Labels | Janelle Nightingale' },
    expected: 'Janelle Nightingale',
  },
  {
    label: 'falls back to "<Topic>: <Name> on ..." form',
    episode: { title: 'From Policy to People: Mayor David Holt on Oklahoma City' },
    expected: 'Mayor David Holt',
  },
  {
    label: 'returns show name when nothing parseable is present',
    episode: { title: 'Episode 42' },
    expected: 'VOICES of OKC',
  },
  {
    label: 'handles missing title without throwing',
    episode: {},
    expected: 'VOICES of OKC',
  },
];

for (const { label, episode, expected } of cases) {
  context.episode = episode;
  const actual = vm.runInContext('deriveGuest(episode)', context);
  assert.equal(actual, expected, `deriveGuest: ${label} (got ${JSON.stringify(actual)})`);
}

console.log(`featured-guest fallback: ${cases.length} cases passed`);
