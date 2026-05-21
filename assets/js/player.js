const audio = document.getElementById('siteAudio');
const toggle = document.getElementById('audioToggle');
const toggleLabel = document.getElementById('audioToggleLabel');
const seek = document.getElementById('audioSeek');
const currentEl = document.getElementById('audioCurrent');
const durationEl = document.getElementById('audioDuration');
const titleEl = document.getElementById('audioTitle');
const spotifyLink = document.getElementById('audioSpotify');
const appleLink = document.getElementById('audioApple');
const youtubeLink = document.getElementById('audioYoutube');
const episodeLink = document.getElementById('audioEpisode');
const note = document.getElementById('audioStatusNote');
const audioPlayer = document.getElementById('audioPlayer');

const featuredImage = document.getElementById('featuredEpisodeImage');
const featuredTitle = document.getElementById('featuredEpisodeTitle');
const featuredDescription = document.getElementById('featuredEpisodeDescription');
const featuredButton = document.getElementById('featuredEpisodeButton');
const featuredYouTube = document.getElementById('featuredEpisodeYoutube');
const featuredApple = document.getElementById('featuredEpisodeApple');
const featuredSpotify = document.getElementById('featuredEpisodeSpotify');
const featuredGuest = document.getElementById('featuredEpisodeGuest');

const latestEpisodeUrl = 'assets/data/latest-episode.json';
const episodesUrl = 'assets/data/episodes.json';
const siteConfigUrl = 'assets/data/site-config.json';
const youtubeChannelUrl = 'https://youtube.com/@voicesofokc';

const fmt = (sec) => {
  if (!Number.isFinite(sec)) return '0:00';
  const m = Math.floor(sec / 60);
  const s = Math.floor(sec % 60).toString().padStart(2, '0');
  return `${m}:${s}`;
};

const cleanText = (value) => String(value || '').replace(/\s+/g, ' ').trim();

const stripHtml = (value) => {
  if (!value) return '';
  const tmp = document.createElement('div');
  tmp.innerHTML = value;
  return (tmp.textContent || tmp.innerText || '').replace(/\s+/g, ' ').trim();
};

const truncateText = (value, limit = 360) => {
  const text = String(value || '').replace(/\s+/g, ' ').trim();
  if (text.length <= limit) return text;
  const clipped = text.slice(0, limit - 3);
  return `${clipped.slice(0, clipped.lastIndexOf(' ')).trim() || clipped}...`;
};

const youtubeThumbnailFromUrl = (value) => {
  const url = String(value || '');
  const match = url.match(/(?:v=|youtu\.be\/|embed\/|shorts\/)([a-zA-Z0-9_-]{6,})/);
  return match ? `https://i.ytimg.com/vi/${match[1]}/maxresdefault.jpg` : '';
};

const normalizeEpisodeSlug = (value) => {
  const raw = cleanText(value);
  if (!raw) return '';

  let path = raw;
  try {
    path = new URL(raw, window.location.origin).pathname;
  } catch (error) {
    path = raw;
  }

  return path
    .replace(/^\/+|\/+$/g, '')
    .replace(/\/index\.html$/i, '')
    .replace(/^episodes\//i, '')
    .replace(/\/$/g, '');
};

const episodeMatchesSlug = (episode, slug) => {
  const target = normalizeEpisodeSlug(slug);
  if (!target) return false;

  return [
    episode.podbean_slug,
    episode.slug,
    episode.site_path,
    episode.site_url,
    episode.episode_url,
  ].some((value) => normalizeEpisodeSlug(value) === target);
};

const loadJson = async (url) => {
  const res = await fetch(url, { cache: 'no-store' });
  if (!res.ok) throw new Error(`${url} unavailable`);
  return res.json();
};

const renderFeaturedEpisode = (episode) => {
  if (!episode || !featuredTitle) return;

  const title = cleanText(episode.title);

  if (title) {
    featuredTitle.textContent = title;
  }

  if (featuredGuest && episode.guest_name) {
    const guestMeta = [episode.guest_name, episode.guest_title || episode.guest_organization].filter(Boolean).join(' · ');
    featuredGuest.textContent = guestMeta;
  }

  if (episode.summary && featuredDescription) {
    const cleanSummary = stripHtml(episode.summary);
    if (cleanSummary) featuredDescription.textContent = truncateText(cleanSummary);
  }

  const featuredArtwork = youtubeThumbnailFromUrl(episode.youtube_url)
    || episode.thumbnail_url
    || episode.artwork_url;
  if (featuredArtwork && featuredImage) {
    featuredImage.src = featuredArtwork;
    featuredImage.removeAttribute('srcset');
    featuredImage.alt = `${title || 'Featured episode'} artwork for VOICES of OKC`;
  }

  if (featuredSpotify && episode.spotify_url) {
    featuredSpotify.href = episode.spotify_url;
  }

  if (featuredApple && episode.apple_url) {
    featuredApple.href = episode.apple_url;
  }

  if (featuredYouTube) {
    featuredYouTube.href = episode.youtube_url || youtubeChannelUrl;
  }

  const localEpisodeUrl = episode.site_path || episode.site_url || episode.episode_url;

  if (localEpisodeUrl && featuredButton) {
    featuredButton.href = localEpisodeUrl;
    if (episode.site_path || episode.site_url) {
      featuredButton.removeAttribute('target');
      featuredButton.removeAttribute('rel');
    } else {
      featuredButton.target = '_blank';
      featuredButton.rel = 'noreferrer';
    }
  }
};

const loadFeaturedEpisode = async (latestEpisode) => {
  const config = await loadJson(siteConfigUrl).catch(() => ({}));
  const featuredSlug = cleanText(config.featured_episode_slug || (config.brand && config.brand.featured_episode_slug));

  if (!featuredSlug) {
    renderFeaturedEpisode(latestEpisode);
    return;
  }

  const episodeData = await loadJson(episodesUrl).catch(() => ({}));
  const episodes = Array.isArray(episodeData) ? episodeData : (episodeData.episodes || []);
  const featuredEpisode = episodes.find((episode) => episodeMatchesSlug(episode, featuredSlug));

  renderFeaturedEpisode(featuredEpisode || latestEpisode);
};

const isMobileViewport = () => window.matchMedia('(max-width: 680px)').matches;

const hideMobilePlayer = () => {
  if (!audioPlayer || !isMobileViewport()) return;
  audio.pause();
  setPlayState(false);
  audioPlayer.style.display = 'none';
  document.body.style.paddingBottom = '18px';
};

const wireMobileNavDismiss = () => {
  if (!audioPlayer) return;
  const navTargets = document.querySelectorAll('.nav a, .brand, .header-cta a, a[href^="#"]');
  navTargets.forEach((el) => {
    el.addEventListener('click', hideMobilePlayer);
    el.addEventListener('touchstart', hideMobilePlayer, { passive: true });
  });
};

const updateProgress = () => {
  const duration = Number.isFinite(audio.duration) && audio.duration > 0 ? audio.duration : 0;
  const current = Number.isFinite(audio.currentTime) ? audio.currentTime : 0;
  const pct = duration ? (current / duration) * 100 : 0;
  seek.value = pct;
  seek.style.setProperty('--progress', `${pct}%`);
  currentEl.textContent = fmt(current);
  durationEl.textContent = fmt(duration);
};

const setPlayState = (playing) => {
  toggleLabel.textContent = playing ? 'Pause' : 'Play';
  toggle.setAttribute('aria-label', playing ? 'Pause latest episode audio' : 'Play latest episode audio');
};

const setUnavailable = (message) => {
  toggle.disabled = true;
  seek.disabled = true;
  setPlayState(false);
  note.textContent = message;
};

async function loadLatestEpisode() {
  try {
    const episode = await loadJson(latestEpisodeUrl);

    const title = (episode.title || '').trim();
    const displayTitle = title ? title.toUpperCase() : '';

    if (displayTitle) {
      titleEl.textContent = displayTitle;
    }

    if (episode.spotify_url) {
      spotifyLink.href = episode.spotify_url;
    }

    if (episode.apple_url) {
      appleLink.href = episode.apple_url;
    }

    if (episode.youtube_url) {
      youtubeLink.href = episode.youtube_url;
    }

    const localEpisodeUrl = episode.site_path || episode.site_url || episode.episode_url;

    if (localEpisodeUrl) {
      episodeLink.href = localEpisodeUrl;
    }

    try {
      await loadFeaturedEpisode(episode);
    } catch (error) {
      renderFeaturedEpisode(episode);
    }

    if (!episode.audio_url) {
      setUnavailable('Audio source not set yet. Run the workflow or update latest-episode.json.');
      return;
    }

    audio.src = episode.audio_url;
    toggle.disabled = false;
    seek.disabled = false;
    note.textContent = episode.updated_at ? `Latest episode synced ${episode.updated_at}` : 'Latest episode ready to play.';
    audio.load();
  } catch (err) {
    setUnavailable('Unable to load latest episode data.');
  }
}

toggle.addEventListener('click', async () => {
  try {
    if (audio.paused) {
      await audio.play();
      setPlayState(true);
    } else {
      audio.pause();
      setPlayState(false);
    }
  } catch (err) {
    setUnavailable('Audio playback failed. Check the feed or source URL.');
  }
});

seek.addEventListener('input', (e) => {
  if (!Number.isFinite(audio.duration) || audio.duration <= 0) return;
  audio.currentTime = (Number(e.target.value) / 100) * audio.duration;
  updateProgress();
});

audio.addEventListener('timeupdate', updateProgress);
audio.addEventListener('durationchange', updateProgress);
audio.addEventListener('loadedmetadata', updateProgress);
audio.addEventListener('ended', () => {
  setPlayState(false);
  updateProgress();
});
audio.addEventListener('error', () => {
  setUnavailable('Audio source failed to load from the latest episode feed.');
});

setUnavailable('Loading latest episode...');
wireMobileNavDismiss();
loadLatestEpisode();
