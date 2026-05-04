const archiveGrid = document.getElementById('episodeArchiveGrid');
const archiveStatus = document.getElementById('episodeArchiveStatus');
const episodeSearch = document.getElementById('episodeSearch');
const themeFilter = document.getElementById('themeFilter');

const fallbackImage = '../assets/images/featured-episode-8.jpg';
const themeLabels = [
  'Civic Leadership',
  'Business & Entrepreneurship',
  'Arts & Culture',
  'Restoration & Second Chances',
  'Youth & Family',
  'Faith, Purpose & Resilience',
  'Sports, Mindset & Performance',
  'Community Builders',
];

const normalizeBrandRefs = (value) => {
  return String(value || '')
    .replace('https://voicesofokc.org', 'https://www.voicesofokc.com')
    .replace('http://voicesofokc.org', 'https://www.voicesofokc.com')
    .replace('www.voicesofokc.org', 'www.voicesofokc.com')
    .replace('voicesofokc.org', 'voicesofokc.com')
    .replace('info@voicesofokc.org', 'info@voicesofokc.com');
};

const escapeHtml = (value) => {
  return String(value || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
};

const slugify = (value) => {
  return String(value || '')
    .toLowerCase()
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/&/g, 'and')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
};

const youtubeThumbnailFromUrl = (value) => {
  const url = String(value || '');
  const match = url.match(/(?:v=|youtu\.be\/|embed\/|shorts\/)([a-zA-Z0-9_-]{6,})/);
  return match ? `https://i.ytimg.com/vi/${match[1]}/maxresdefault.jpg` : '';
};

const isYoutubeThumbnail = (value) => /(?:i\.ytimg\.com|img\.youtube\.com)\/vi\//.test(String(value || ''));

const getEpisodeArtwork = (episode) => {
  return youtubeThumbnailFromUrl(episode.youtube_url)
    || (isYoutubeThumbnail(episode.thumbnail_url) ? episode.thumbnail_url : '')
    || (isYoutubeThumbnail(episode.artwork_url) ? episode.artwork_url : '')
    || fallbackImage;
};

const stripHtml = (value) => {
  const tmp = document.createElement('div');
  tmp.innerHTML = normalizeBrandRefs(value);
  return (tmp.textContent || tmp.innerText || '').replace(/\s+/g, ' ').trim();
};

const trimSummary = (value) => {
  const text = stripHtml(value);
  if (text.length <= 190) return text;
  const clipped = text.slice(0, 187);
  return `${clipped.slice(0, clipped.lastIndexOf(' ')).trim() || clipped}...`;
};

const formatDate = (value) => {
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return '';
  return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
};

const deriveThemes = (episode) => {
  if (Array.isArray(episode.theme_tags) && episode.theme_tags.length) return episode.theme_tags;
  const haystack = `${episode.title || ''} ${episode.summary || ''}`.toLowerCase();
  const themes = [];
  if (/mayor|policy|justice|public safety|leadership|state|city/.test(haystack)) themes.push('Civic Leadership');
  if (/founder|entrepreneur|business|company|startup|practice/.test(haystack)) themes.push('Business & Entrepreneurship');
  if (/storytelling|artist|creative|film|culture|podcast/.test(haystack)) themes.push('Arts & Culture');
  if (/redemption|restore|second|justice|healing|hope|rebuilding/.test(haystack)) themes.push('Restoration & Second Chances');
  if (/student|youth|family|mentor|next generation|young/.test(haystack)) themes.push('Youth & Family');
  if (/faith|purpose|resilience|calling|hope/.test(haystack)) themes.push('Faith, Purpose & Resilience');
  if (/sports|coach|performance|pressure|wrestling|mindset/.test(haystack)) themes.push('Sports, Mindset & Performance');
  if (/community|mentor|neighbor|oklahoma city|okc/.test(haystack)) themes.push('Community Builders');
  return [...new Set(themes)].slice(0, 3);
};

const deriveGuest = (episode) => {
  if (episode.guest_name) return episode.guest_name;
  const title = episode.title || '';
  const onMatch = title.match(/:\s*([^:|]+?)\s+on\s+/i);
  if (onMatch) return onMatch[1].trim();
  const pipeMatch = title.match(/\|\s*([^|]+)$/);
  if (pipeMatch) return pipeMatch[1].trim();
  return 'VOICES of OKC';
};

const buildEpisodeHref = (episode) => {
  if (episode.site_path) return `../${episode.site_path}`;
  if (episode.site_url) return episode.site_url;
  return episode.episode_url || episode.podbean_url || '#';
};

const isExternal = (href) => /^https?:\/\//.test(href) && !href.includes('voicesofokc.com');

const matchesEpisode = (episode, search, activeTheme) => {
  const themes = deriveThemes(episode);
  const themeMatch = activeTheme === 'all' || themes.some((theme) => slugify(theme) === activeTheme);
  if (!themeMatch) return false;
  if (!search) return true;
  const haystack = [
    episode.title,
    episode.summary,
    episode.guest_name,
    episode.guest_title,
    episode.guest_organization,
    ...themes,
  ].join(' ').toLowerCase();
  return haystack.includes(search.toLowerCase());
};

const renderThemeFilters = () => {
  if (!themeFilter) return;
  themeFilter.innerHTML = [
    '<button class="filter-pill" type="button" data-theme="all" aria-pressed="true">All</button>',
    ...themeLabels.map((theme) => (
      `<button class="filter-pill" type="button" data-theme="${slugify(theme)}" aria-pressed="false">${escapeHtml(theme)}</button>`
    )),
  ].join('');
};

const renderEpisodes = (episodes) => {
  if (!archiveGrid) return;
  const search = episodeSearch ? episodeSearch.value.trim() : '';
  const activeButton = themeFilter ? themeFilter.querySelector('[aria-pressed="true"]') : null;
  const activeTheme = activeButton ? activeButton.dataset.theme : 'all';
  const visible = episodes.filter((episode) => matchesEpisode(episode, search, activeTheme));

  if (archiveStatus) {
    archiveStatus.textContent = visible.length === 1 ? '1 conversation shown' : `${visible.length} conversations shown`;
  }

  if (!visible.length) {
    archiveGrid.innerHTML = `
      <article class="card-surface">
        <span class="eyebrow">No episodes found</span>
        <h2 class="title-md">Try another theme or search term.</h2>
      </article>
    `;
    return;
  }

  archiveGrid.innerHTML = visible.slice(0, 24).map((episode, index) => {
    const artwork = getEpisodeArtwork(episode);
    const title = episode.title || `Episode ${index + 1}`;
    const summary = trimSummary(episode.summary) || 'Listen to the latest conversation from VOICES of OKC.';
    const href = buildEpisodeHref(episode);
    const externalAttrs = isExternal(href) ? ' target="_blank" rel="noreferrer"' : '';
    const guest = deriveGuest(episode);
    const meta = [guest, episode.guest_organization].filter(Boolean).join(' · ');
    const date = formatDate(episode.published_at);
    const themes = deriveThemes(episode).slice(0, 3);
    const label = episode.episode_number ? `Episode ${episode.episode_number}` : (index === 0 ? 'Latest episode' : 'Episode');

    return `
      <article class="episode-card episode-archive-card">
        <a class="episode-card-media" href="${escapeHtml(href)}"${externalAttrs}>
          <img loading="lazy" src="${escapeHtml(artwork)}" alt="${escapeHtml(title)} artwork for VOICES of OKC" />
        </a>
        <div class="episode-card-body">
          <span class="guest-role">${escapeHtml(label)}</span>
          <h2 class="episode-card-title">${escapeHtml(title.toUpperCase())}</h2>
          <div class="episode-date">${escapeHtml([meta, date].filter(Boolean).join(' · '))}</div>
          <div class="tag-list">${themes.map((theme) => `<span class="tag">${escapeHtml(theme)}</span>`).join('')}</div>
          <p>${escapeHtml(summary)}</p>
          <div class="episode-card-actions">
            <a class="button-outline" href="${escapeHtml(href)}"${externalAttrs}>View Episode</a>
            <a class="button-outline" href="${escapeHtml(episode.podbean_url || episode.episode_url || href)}" target="_blank" rel="noreferrer">Podbean</a>
          </div>
        </div>
      </article>
    `;
  }).join('');
};

async function loadEpisodes() {
  if (!archiveGrid) return;

  renderThemeFilters();

  try {
    const res = await fetch('../assets/data/episodes.json', { cache: 'no-store' });
    if (!res.ok) throw new Error('episodes data unavailable');
    const data = await res.json();
    const episodes = Array.isArray(data.episodes) ? data.episodes : [];
    if (!episodes.length) throw new Error('no episodes found');

    renderEpisodes(episodes);

    if (episodeSearch) {
      episodeSearch.addEventListener('input', () => renderEpisodes(episodes));
    }

    if (themeFilter) {
      themeFilter.addEventListener('click', (event) => {
        const button = event.target.closest('[data-theme]');
        if (!button) return;
        themeFilter.querySelectorAll('[data-theme]').forEach((item) => item.setAttribute('aria-pressed', 'false'));
        button.setAttribute('aria-pressed', 'true');
        renderEpisodes(episodes);
      });

      const requestedTheme = new URLSearchParams(window.location.search).get('theme');
      if (requestedTheme) {
        const requestedButton = Array.from(themeFilter.querySelectorAll('[data-theme]')).find((item) => item.dataset.theme === requestedTheme);
        if (requestedButton) {
          themeFilter.querySelectorAll('[data-theme]').forEach((item) => item.setAttribute('aria-pressed', 'false'));
          requestedButton.setAttribute('aria-pressed', 'true');
          renderEpisodes(episodes);
        }
      }
    }
  } catch (error) {
    if (archiveStatus) archiveStatus.textContent = 'Episode sync needs attention';
    archiveGrid.innerHTML = `
      <article class="episode-card episode-archive-card">
        <div class="episode-card-media"><img src="${fallbackImage}" alt="Fallback artwork for VOICES of OKC" /></div>
        <div class="episode-card-body">
          <span class="guest-role">Episode archive</span>
          <h2 class="episode-card-title">EPISODE SYNC NOT READY YET</h2>
          <p>Run the “Update Podbean episode data” workflow in GitHub Actions to populate the latest episode thumbnails and links automatically.</p>
          <a class="button-outline" href="../index.html">Back Home</a>
        </div>
      </article>
    `;
  }
}

loadEpisodes();
