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
      toggle.setAttribute('aria-expanded', 'true');
    }

    function close() {
      if (!isOpen) return;
      isOpen = false;
      dropdown.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
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
})();
