(() => {
  const script = document.currentScript;
  const configUrl = script ? new URL('../data/site-config.json', script.src) : new URL('/assets/data/site-config.json', window.location.origin);
  const fallbackEmail = 'info@voicesofokc.com';

  window.dataLayer = window.dataLayer || [];

  const cleanText = (value) => String(value || '').replace(/\s+/g, ' ').trim();

  const toEventName = (value) => {
    const base = cleanText(value)
      .toLowerCase()
      .replace(/&/g, 'and')
      .replace(/[^a-z0-9]+/g, '_')
      .replace(/^_+|_+$/g, '');
    return base || 'interaction';
  };

  const track = (eventName, payload = {}) => {
    const event = {
      event: eventName,
      page_path: window.location.pathname,
      page_title: document.title,
      ...payload,
    };
    window.dataLayer.push(event);

    if (typeof window.gtag === 'function') {
      window.gtag('event', eventName, payload);
    }

    if (typeof window.plausible === 'function') {
      window.plausible(eventName, { props: payload });
    }

    window.dispatchEvent(new CustomEvent('voices:analytics', { detail: event }));
  };

  window.voicesAutomation = { track };

  const buildMailto = (email, subject) => {
    const params = subject ? `?subject=${encodeURIComponent(subject)}` : '';
    return `mailto:${email}${params}`;
  };

  const setEmailTargets = (config) => {
    const brand = config.brand || {};
    const email = brand.email || fallbackEmail;
    const label = brand.email_label || 'VOICES of OKC Email';

    document.querySelectorAll('[data-site-email]').forEach((item) => {
      item.textContent = email;
    });

    document.querySelectorAll('[data-site-email-label]').forEach((item) => {
      item.textContent = label;
    });

    document.querySelectorAll('[data-site-email-link]').forEach((item) => {
      item.href = buildMailto(email);
      item.textContent = email;
    });
  };

  const appendHiddenField = (form, name, value) => {
    if (!value || form.querySelector(`input[name="${name}"]`)) return;
    const input = document.createElement('input');
    input.type = 'hidden';
    input.name = name;
    input.value = value;
    form.appendChild(input);
  };

  const renderEmbeddedForm = (shell, formConfig) => {
    if (!formConfig.embed_url) return false;
    const iframe = document.createElement('iframe');
    iframe.className = 'form-embed-frame';
    iframe.src = formConfig.embed_url;
    iframe.title = formConfig.label || 'VOICES of OKC form';
    iframe.loading = 'lazy';
    iframe.setAttribute('allowtransparency', 'true');
    iframe.setAttribute('frameborder', '0');

    const form = shell.querySelector('.form-embed');
    if (form) form.replaceWith(iframe);

    const note = shell.querySelector('.form-note');
    if (note) {
      note.textContent = 'This form is connected for submissions and follow-up routing.';
    }
    return true;
  };

  const wireForms = (config) => {
    const forms = config.forms || {};
    document.querySelectorAll('[data-form-key]').forEach((node) => {
      if (node.matches('form') && node.closest('.form-shell[data-form-key]')) return;
      const key = node.dataset.formKey;
      const form = node.matches('form') ? node : node.querySelector('form[data-form-key], .form-embed');
      const shell = node.matches('.form-shell') ? node : node.closest('.form-shell');
      const formConfig = forms[key] || {};
      const email = formConfig.fallback_email || (config.brand && config.brand.email) || fallbackEmail;
      const subject = formConfig.subject || `VOICES of OKC ${formConfig.label || 'Inquiry'}`;

      if (shell && renderEmbeddedForm(shell, formConfig)) return;

      if (form) {
        form.action = buildMailto(email, subject);
        form.method = 'post';
        form.enctype = 'text/plain';
        appendHiddenField(form, 'VOICES of OKC Email', email);
        appendHiddenField(form, 'Form Type', formConfig.label || key);
        form.addEventListener('submit', () => {
          track('form_submit_mailto', {
            form_key: key,
            form_label: formConfig.label || key,
            destination: email,
          });
        });
      }

      const note = shell ? shell.querySelector('.form-note') : null;
      if (note && !formConfig.embed_url) {
        note.innerHTML = `Submissions currently open a prepared email to <a data-site-email-link href="${buildMailto(email)}">${email}</a>. Add the ${formConfig.provider || 'Tally/Fillout'} embed URL in <code>assets/data/site-config.json</code> to route this into Airtable.`;
      }
    });
  };

  const inferTrackingPayload = (target) => {
    const text = cleanText(target.getAttribute('aria-label') || target.textContent);
    const href = target.getAttribute('href') || '';
    const location = target.closest('header') ? 'header'
      : target.closest('footer') ? 'footer'
      : target.closest('form') ? 'form'
      : target.closest('section') ? (target.closest('section').id || 'section')
      : 'page';

    return {
      cta_text: text,
      cta_href: href,
      cta_location: location,
    };
  };

  const wireTracking = () => {
    track('page_view', { path: window.location.pathname });

    document.addEventListener('click', (event) => {
      const target = event.target.closest('a, button');
      if (!target) return;
      const payload = inferTrackingPayload(target);
      const explicitName = target.dataset.track;
      const eventName = explicitName || `cta_${toEventName(payload.cta_text || payload.cta_href)}`;
      track(eventName, payload);
    });
  };

  const loadConfig = async () => {
    try {
      const response = await fetch(configUrl, { cache: 'no-store' });
      if (!response.ok) throw new Error('site config unavailable');
      return await response.json();
    } catch (error) {
      return {
        brand: {
          email: fallbackEmail,
          email_label: 'VOICES of OKC Email',
        },
        forms: {},
      };
    }
  };

  document.addEventListener('DOMContentLoaded', async () => {
    const config = await loadConfig();
    setEmailTargets(config);
    wireForms(config);
    wireTracking();
  });
})();
