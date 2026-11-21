(() => {
  const dialog = document.querySelector('.scheduling-popup');
  if (!dialog || typeof dialog.showModal !== 'function') return;
  const frame = dialog.querySelector('iframe');
  let trigger;
  let previousOverflow;
  document.querySelectorAll('[data-scheduling-popup]').forEach((link) => {
    link.addEventListener('click', (event) => {
      if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      trigger = link;
      if (!frame.src) frame.src = link.href;
      previousOverflow = document.body.style.overflow;
      document.body.style.overflow = 'hidden';
      dialog.showModal();
    });
  });
  dialog.querySelector('[data-close-scheduling]').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', (event) => {
    const bounds = dialog.getBoundingClientRect();
    if (event.target === dialog && (event.clientX < bounds.left || event.clientX > bounds.right ||
        event.clientY < bounds.top || event.clientY > bounds.bottom)) dialog.close();
  });
  dialog.addEventListener('close', () => {
    document.body.style.overflow = previousOverflow;
    trigger?.focus({ preventScroll: true });
  });
})();
