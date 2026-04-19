const audio = document.getElementById('siteAudio');
const toggle = document.getElementById('audioToggle');
const toggleLabel = document.getElementById('audioToggleLabel');
const seek = document.getElementById('audioSeek');
const currentEl = document.getElementById('audioCurrent');
const durationEl = document.getElementById('audioDuration');
const titleEl = document.getElementById('audioTitle');
const player = document.getElementById('audioPlayer');
const spotifyLink = document.getElementById('audioSpotify');
const appleLink = document.getElementById('audioApple');
const youtubeLink = document.getElementById('audioYoutube');
const episodeLink = document.getElementById('audioEpisode');
const note = document.getElementById('audioStatusNote');

const fmt = (sec) => {
  if (!Number.isFinite(sec)) return '0:00';
  const m = Math.floor(sec / 60);
  const s = Math.floor(sec % 60).toString().padStart(2, '0');
  return `${m}:${s}`;
};

const updateProgress = () => {
  const duration = Number.isFinite(audio.duration) && audio.duration > 0 ? audio.duration : 0;
  const current = Number.isFinite(audio.currentTime) ? audio.currentTime : 0;
  const pct = duration ? (current / duration) * 100 : 0;
  seek.value = pct;
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
    const res = await fetch('assets/data/latest-episode.json', { cache: 'no-store' });
    if (!res.ok) throw new Error('latest episode data unavailable');
    const episode = await res.json();

    if (episode.title) titleEl.textContent = episode.title;
    if (episode.spotify_url) spotifyLink.href = episode.spotify_url;
    if (episode.apple_url) appleLink.href = episode.apple_url;
    if (episode.youtube_url) youtubeLink.href = episode.youtube_url;
    if (episode.episode_url) episodeLink.href = episode.episode_url;

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
loadLatestEpisode();