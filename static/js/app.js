/* jshint esversion: 8 */
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

        form.addEventListener('submit', (e) => {
            // Validate before letting the browser submit normally
            if (!vid || !vid.value) {
                e.preventDefault();
                alert('No product selected. Please refresh and try again.');
                return;
            }
            if (!qty || !validQty(qty)) {
                e.preventDefault();
                alert('Please enter a whole number quantity of 1 or more.');
                if (qty) qty.focus();
                return;
            }
            // No preventDefault() here → default POST + server redirect to cart
        });

        // Live guard against invalid qty input
        if (qty) {
            qty.addEventListener('input', () => {
                if (!validQty(qty)) {
                    qty.setCustomValidity('Please enter a whole number of 1 or more.');
                } else {
                    qty.setCustomValidity('');
                }
            });
        }
    });
})();
