/* global fetch */
(function () {
  'use strict';

  const feedback = document.getElementById('feedback');

  function say(msg, type = 'info') {
    if (!feedback) return;
    feedback.classList.remove('visually-hidden');
    feedback.textContent = msg;
    feedback.dataset.type = type;
  }

  function validQty(input) {
    const n = Number(input.value);
    return Number.isFinite(n) && n >= 1 && Number.isInteger(n);
  }

  // Enhance add-to-cart forms (progressive enhancement)
  document.querySelectorAll('form.js-add-to-cart').forEach((form) => {
    const btn = form.querySelector('button[type="submit"]');
    const qty = form.querySelector('input[name="quantity"]');
    const vid = form.querySelector('input[name="variant_id"]');

    form.addEventListener('submit', async (e) => {
      // Let normal POST work if JS must not intercept (e.g., no fetch)
      e.preventDefault();

      // Basic input checks
      if (!vid || !vid.value) {
        say('No product selected. Please refresh and try again.', 'error');
        return;
      }
      if (!qty || !validQty(qty)) {
        say('Please enter a whole number quantity of 1 or more.', 'error');
        qty && qty.focus();
        return;
      }

      // Disable UI while sending
      btn.disabled = true;
      btn.setAttribute('aria-busy', 'true');

      try {
        // Build a FormData -> POST to the normal endpoint
        const fd = new FormData(form);
        const res = await fetch(form.action, {
          method: 'POST',
          headers: { 'X-Requested-With': 'XMLHttpRequest' },
          body: fd
        });

        if (!res.ok) throw new Error('Network response was not ok');
        // Try to read JSON; if not JSON, fall back to text
        let data;
        const ct = res.headers.get('content-type') || '';
        if (ct.includes('application/json')) {
          data = await res.json();
        } else {
          await res.text();
          data = { ok: true };
        }

        say('Added to cart. View your cart or continue browsing.', 'success');
        // Return focus to the “Add to bag” for keyboard continuity
        btn.focus();
      } catch (err) {
        console.error(err);
        say('Sorry, we could not add this item right now. Please try again.', 'error');
      } finally {
        btn.disabled = false;
        btn.removeAttribute('aria-busy');
      }
    });

    // Live guard against invalid qty input
    qty && qty.addEventListener('input', () => {
      if (!validQty(qty)) {
        qty.setCustomValidity('Please enter a whole number of 1 or more.');
      } else {
        qty.setCustomValidity('');
      }
    });
  });
})();
