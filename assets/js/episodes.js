const archiveGrid = document.getElementById('episodeArchiveGrid');

const fallbackImage = '../assets/images/featured-episode-8.jpg';

const normalizeBrandRefs = (value) => {
  return String(value || '')
    .replace('https://voicesofokc.org', 'https://www.voicesofokc.com')
    .replace('http://voicesofokc.org', 'https://www.voicesofokc.com')
    .replace('www.voicesofokc.org', 'www.voicesofokc.com')
    .replace('voicesofokc.org', 'voicesofokc.com')
    .replace('info@voicesofokc.org', 'info@voicesofokc.com');
};

const trimSummary = (value) => {
  if (!value) return '';
  const tmp = document.createElement('div');
  tmp.innerHTML = normalizeBrandRefs(value);
  const text = (tmp.textContent || tmp.innerText || '').replace(/\s+/g, ' ').trim();
  return text.length > 170 ? `${text.slice(0, 167)}…` : text;
};

async function loadEpisodes() {
  if (!archiveGrid) return;

  try {
    const res = await fetch('../assets/data/episodes.json', { cache: 'no-store' });
    if (!res.ok) throw new Error('episodes data unavailable');
    const data = await res.json();
    const episodes = Array.isArray(data.episodes) ? data.episodes : [];
    if (!episodes.length) throw new Error('no episodes found');

    archiveGrid.innerHTML = episodes.slice(0, 10).map((episode, index) => {
      const artwork = episode.artwork_url || fallbackImage;
      const title = episode.title || `EPISODE ${index + 1}`;
      const summary = trimSummary(episode.summary) || 'Listen to the latest conversation from VOICES of OKC.';
      const href = episode.episode_url || '#';
      const label = index === 0 ? 'LATEST EPISODE' : 'EPISODE';
      return `
        <article class="guest-card">
          <div class="guest-card-image"><img src="${artwork}" alt="${title} artwork for VOICES of OKC" /></div>
          <div class="guest-card-copy">
            <span class="guest-role">${label}</span>
            <h2 class="episode-title" style="font-size:1.15rem;margin:0;">${title}</h2>
            <p>${summary}</p>
            <a class="button-outline" href="${href}" target="_blank" rel="noreferrer">Open episode</a>
          </div>
        </article>
      `;
    }).join('');
  } catch (error) {
    archiveGrid.innerHTML = `
      <article class="guest-card">
        <div class="guest-card-image"><img src="${fallbackImage}" alt="Fallback artwork for VOICES of OKC" /></div>
        <div class="guest-card-copy">
          <span class="guest-role">EPISODE ARCHIVE</span>
          <h2 class="episode-title" style="font-size:1.15rem;margin:0;">EPISODE SYNC NOT READY YET</h2>
          <p>Run the “Update Podbean episode data” workflow in GitHub Actions to populate the latest episode thumbnails and links automatically.</p>
          <a class="button-outline" href="../index.html">Back home</a>
        </div>
      </article>
    `;
  }
}

loadEpisodes();
