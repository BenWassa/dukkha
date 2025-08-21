(function() {
  'use strict';

  // Navigation dropdown functionality
  function initDropdown() {
    var dropdown = document.querySelector('.nav-dropdown');
    if (!dropdown) return;

    var toggle = dropdown.querySelector('.nav-dropdown__toggle');
    var menu = dropdown.querySelector('.nav-dropdown__menu');
    
    if (!toggle || !menu) return;

    // Protocol items - these should match the actual protocol pages
    var protocols = [
      { name: 'Digital Detox Protocol', url: 'protocols/digital-detox-protocol.html' },
      { name: 'Mindfulness & Awareness Protocol', url: 'protocols/mindfulness-awareness-protocol.html' },
      { name: 'Nutrition & Supplementation Protocol', url: 'protocols/nutrition-supplementation-protocol.html' },
      { name: 'Sleep Optimization Protocol', url: 'protocols/sleep-optimization-protocol.html' },
      { name: 'Stress Management Protocol', url: 'protocols/stress-management-protocol.html' }
    ];

    // Populate dropdown menu
    menu.innerHTML = protocols.map(function(protocol) {
      return '<li><a href="site/' + protocol.url + '" role="menuitem">' + protocol.name + '</a></li>';
    }).join('');

    // Dropdown state management
    var isOpen = false;

    function open() {
      if (isOpen) return;
      isOpen = true;
      dropdown.classList.add('open');
      toggle.setAttribute('aria-expanded', 'true');
      
      // Position dropdown correctly
      var rect = toggle.getBoundingClientRect();
      menu.style.position = 'fixed';
      menu.style.top = (rect.bottom + window.scrollY) + 'px';
      menu.style.left = rect.left + 'px';
    }

    function close() {
      if (!isOpen) return;
      isOpen = false;
      dropdown.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    }

    function toggle_dropdown() {
      if (isOpen) {
        close();
      } else {
        open();
      }
    }

    // Event listeners
    toggle.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      toggle_dropdown();
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
