// Isolated JS regression tests. A forbidden DOM parser catches the original defect.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const root = path.resolve(__dirname, '..');
const payloads = ['<img src=x onerror=bad()>', '<svg onload=bad()>', '<iframe src=x></iframe>', '<script>bad()</script>', '&lt;img src=x onerror=bad()&gt;', '&amp;lt;svg onload=bad()&amp;gt;'];
for (const name of ['episodes', 'player']) {
  const source = fs.readFileSync(path.join(root, `assets/js/${name}.js`), 'utf8');
  const elements = {episodeArchiveGrid: {innerHTML: ''}, episodeArchiveStatus: {textContent: ''}};
  const context = vm.createContext({document: {
    getElementById: id => elements[id] || null,
    createElement: () => { throw new Error('Summary must not create or parse DOM elements'); },
  }});
  // Execute actual production definitions, omitting only loading/network side effects.
  const boundary = name === 'episodes' ? 'async function loadEpisodes()' : 'const youtubeThumbnailFromUrl';
  assert(source.includes(boundary));
  vm.runInContext(source.slice(0, source.indexOf(boundary)), context);
  const normalizer = source.includes('const normalizeSummary') ? 'normalizeSummary' : 'stripHtml';
  for (const payload of payloads) {
    context.input = payload;
    assert.equal(vm.runInContext(`${normalizer}(input)`, context), payload);
    if (name === 'episodes') {
      context.fixture = {title: 'Hope & Joy', summary: payload, site_path: 'episodes/hope/', podbean_url: 'https://example.test/hope'};
      vm.runInContext('renderEpisodes([fixture])', context);
      const escaped = payload.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;').replaceAll("'", '&#039;');
      assert(elements.episodeArchiveGrid.innerHTML.includes(`<p>${escaped}</p>`), 'Summary must be escaped at output');
      assert(elements.episodeArchiveGrid.innerHTML.includes('href="../episodes/hope/"'));
      assert.equal(elements.episodeArchiveStatus.textContent, '1 conversation shown');
    }
  }
  context.input = '  Hope & joy\nwith café  ';
  assert.equal(vm.runInContext(`${normalizer}(input)`, context), 'Hope & joy with café');
  assert.equal(vm.runInContext(`${normalizer}(null)`, context), '');
  if (name === 'episodes') {
    context.input = 'a '.repeat(150);
    assert(vm.runInContext('trimSummary(input).length', context) <= 190);
  } else {
    context.input = 'a '.repeat(250);
    assert(vm.runInContext('truncateText(normalizeSummary(input)).length', context) <= 360);
    assert(source.includes('featuredDescription.textContent = truncateText(cleanSummary)'));
  }
  console.log(`${name}: 6 hostile summaries, normal text, null and truncation passed`);
}
