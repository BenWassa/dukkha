(function() {
  'use strict';

  // Navigation dropdown functionality
  function initDropdown() {
    var dropdown = document.querySelector('.nav-dropdown');
    if (!dropdown) return;

    var toggle = dropdown.querySelector('.nav-dropdown__toggle');
    var menu = dropdown.querySelector('.nav-dropdown__menu');
    
    if (!toggle || !menu) return;

    // Don't dynamically populate - use existing HTML structure

    // Dropdown state management
    var isOpen = false;
    var closeTimeout;

    function open() {
      if (isOpen) return;
      clearTimeout(closeTimeout);
      isOpen = true;
      dropdown.classList.add('open');
      // preserve any existing aria-expanded value; do not overwrite so hover CSS remains primary
    }

    function close() {
      if (!isOpen) return;
      isOpen = false;
      dropdown.classList.remove('open');
      // preserve aria-expanded attribute
    }

    function delayedClose() {
      closeTimeout = setTimeout(close, 250);
    }

    // Event listeners
    // Hover functionality
    dropdown.addEventListener('mouseenter', function() {
      clearTimeout(closeTimeout);
      open();
    });

    dropdown.addEventListener('mouseleave', function() {
      delayedClose();
    });

    // Click functionality (for touch devices)
    toggle.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      if (isOpen) {
        close();
      } else {
        open();
      }
    });

    // Close on outside click
    document.addEventListener('click', function(e) {
      if (!dropdown.contains(e.target)) {
        close();
      }
    });

    // Close on escape key
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && isOpen) {
        close();
        toggle.focus();
      }
    });

    // Keyboard navigation
    toggle.addEventListener('keydown', function(e) {
      if (e.key === 'ArrowDown' || e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        open();
        var firstItem = menu.querySelector('a');
        if (firstItem) firstItem.focus();
      }
    });

    menu.addEventListener('keydown', function(e) {
      var items = menu.querySelectorAll('a');
      var currentIndex = Array.from(items).indexOf(document.activeElement);

      switch (e.key) {
        case 'ArrowDown':
          e.preventDefault();
          var nextIndex = currentIndex < items.length - 1 ? currentIndex + 1 : 0;
          items[nextIndex].focus();
          break;
        case 'ArrowUp':
          e.preventDefault();
          var prevIndex = currentIndex > 0 ? currentIndex - 1 : items.length - 1;
          items[prevIndex].focus();
          break;
        case 'Escape':
          e.preventDefault();
          close();
          toggle.focus();
          break;
      }
    });
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initDropdown);
  } else {
    initDropdown();
  }

  // Scroll-to-top / hash behavior for nav links on root index
  (function navScrollTopBehaviorIndex() {
    try {
      var navLinks = document.querySelectorAll('.nav-link');
      if (!navLinks || !navLinks.length) return;

      navLinks.forEach(function(a) {
        a.addEventListener('click', function(e) {
          var href = a.getAttribute('href');
          if (!href) return;
          if (href.charAt(0) === '#') {
            e.preventDefault();
            if (href === '#home' || href === '#') {
              window.scrollTo({ top: 0, behavior: 'smooth' });
              history.replaceState(null, '', '#home');
              return;
            }
            var id = href.slice(1);
            var target = document.getElementById(id);
            if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            return;
          }
          // Cross-page: set flag to scroll to top on next load
          try { sessionStorage.setItem('scrollToTop', '1'); } catch (err) {}
        });
      });

      if (sessionStorage.getItem('scrollToTop')) {
        try { window.scrollTo(0, 0); } catch (e) {}
        try { sessionStorage.removeItem('scrollToTop'); } catch (e) {}
      }
    } catch (e) {}
  })();

  // Ensure nav links scroll to top when they target the current page (e.g., '#home' or same-path links)
  function ensureNavScrollTop() {
    document.querySelectorAll('.nav-link').forEach(function(link) {
      link.addEventListener('click', function(e) {
        try {
          var href = link.getAttribute('href') || '';
          var url = new URL(href, window.location.href);
          if (url.pathname === window.location.pathname) {
            // same page target - smooth scroll to top and prevent default anchor jump
            e.preventDefault();
            window.scrollTo({ top: 0, behavior: 'smooth' });
            // update hash in the address bar if necessary (but avoid page reload)
            if (url.hash && url.hash !== window.location.hash) {
              history.replaceState(null, '', url.hash);
            } else if (!url.hash) {
              history.replaceState(null, '', url.pathname + window.location.search);
            }
          }
        } catch (err) {
          // if URL parsing fails, do nothing and allow default navigation
        }
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', ensureNavScrollTop);
  } else {
    ensureNavScrollTop();
  }
})();
