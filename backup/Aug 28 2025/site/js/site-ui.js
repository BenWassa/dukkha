(function() {
  // reading progress
  var progress = document.querySelector('.read-progress');
  if (!progress) {
    progress = document.createElement('div');
    progress.className = 'read-progress';
    progress.setAttribute('aria-hidden', 'true');
    progress.innerHTML = '<div class="read-progress__bar"></div>';
    document.body.appendChild(progress);
  }
  var bar = progress.querySelector('.read-progress__bar');
  if (bar) {
    var nav = document.querySelector('.nav');
    var hero = document.querySelector('[class^="hero"]');
    var showPoint = 0;
    if (nav) { progress.style.top = nav.offsetHeight + 'px'; }
    if (hero && nav) { showPoint = hero.offsetHeight - nav.offsetHeight; }

    var updateProgress = function() {
      var h = document.body.scrollHeight - window.innerHeight;
      var y = window.scrollY;
      var r = h > 0 ? y / h : 0;
      bar.style.width = (r * 100) + '%';
      if (y > showPoint) {
        progress.classList.add('visible');
      } else {
        progress.classList.remove('visible');
      }
    };
    window.addEventListener('scroll', updateProgress, { passive: true });
    updateProgress();
  }

  // playful prompts
  var prompt = document.querySelector('.read-prompt');
  if (prompt && !sessionStorage.getItem('readPromptDismissed')) {
    var promptText = prompt.querySelector('.read-prompt__text');
    var closeBtn = prompt.querySelector('.read-prompt__close');
    var messages = [
      'Keep going—you\'re doing great.',
      'Halfway there!',
      'Almost finished!'
    ];
    var thresholds = [0.25, 0.5, 0.75];
    var shown = -1;
    var checkPrompt = function() {
      var h = document.body.scrollHeight - window.innerHeight;
      var y = window.scrollY;
      var r = h > 0 ? y / h : 0;
      var idx = -1;
      for (var i = 0; i < thresholds.length; i++) {
        if (r > thresholds[i] && i > shown) { idx = i; break; }
      }
      if (idx !== -1) {
        shown = idx;
        promptText.textContent = messages[idx];
        prompt.classList.add('active');
      }
    };
    window.addEventListener('scroll', checkPrompt, { passive: true });
    closeBtn.addEventListener('click', function() {
      prompt.classList.remove('active');
      sessionStorage.setItem('readPromptDismissed', '1');
    });
  }

  // nav dropdown
  var dropdown = document.querySelector('.nav-dropdown');
  if (dropdown) {
      var toggle = dropdown.querySelector('.nav-dropdown__toggle');
      var menu = dropdown.querySelector('.nav-dropdown__menu');
      var inProtocols = window.location.pathname.indexOf('/protocols/') !== -1;
      var basePath = inProtocols ? '' : 'protocols/';
      var overviewPath = inProtocols ? '../protocols.html' : 'protocols.html';
      if (toggle) { toggle.setAttribute('href', overviewPath); }

      function buildMenu(list) {
        menu.innerHTML = '';
        list.forEach(function(p) {
          var li = document.createElement('li');
          var a = document.createElement('a');
          a.href = basePath + p.filename;
          a.textContent = p.title;
          a.setAttribute('role', 'menuitem');
          li.appendChild(a);
          menu.appendChild(li);
        });
      }

      fetch(basePath + 'manifest.json')
        .then(function(r) { return r.json(); })
        .then(function(data) { buildMenu(data.protocols || []); })
        .catch(function() {
          buildMenu([
            {title:'Digital Detox Protocol', filename:'digital-detox-protocol.html'},
            {title:'Mindfulness & Awareness Protocol', filename:'mindfulness-awareness-protocol.html'},
            {title:'Nutrition & Supplementation Protocol', filename:'nutrition-supplementation-protocol.html'},
            {title:'Sleep Optimization Protocol', filename:'sleep-optimization-protocol.html'},
            {title:'Stress Management Protocol', filename:'stress-management-protocol.html'}
          ]);
        });

      function getItems() {
        return Array.prototype.slice.call(menu.querySelectorAll('a'));
      }
      function open() {
        dropdown.classList.add('open');
        toggle.setAttribute('aria-expanded', 'true');
        
        // Position the dropdown correctly relative to the toggle button
        var rect = toggle.getBoundingClientRect();
        menu.style.left = rect.left + 'px';
        menu.style.top = (rect.bottom + 8) + 'px'; // 8px margin
      }
      function close() {
        dropdown.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }

      toggle.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowDown') { e.preventDefault(); open(); getItems()[0] && getItems()[0].focus(); }
      });
      var closeTimeout;
      dropdown.addEventListener('mouseenter', function() {
        clearTimeout(closeTimeout);
        open();
      });
      dropdown.addEventListener('mouseleave', function() {
        closeTimeout = setTimeout(close, 250);
      });

    menu.addEventListener('keydown', function(e) {
      var items = getItems();
      var current = items.indexOf(document.activeElement);
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        items[(current + 1) % items.length].focus();
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        items[(current - 1 + items.length) % items.length].focus();
      } else if (e.key === 'Escape') {
        e.preventDefault();
        close();
        toggle.focus();
      } else if (e.key === 'Tab') {
        if (!e.shiftKey && current === items.length - 1) { e.preventDefault(); toggle.focus(); }
        if (e.shiftKey && current === 0) { e.preventDefault(); toggle.focus(); }
      }
    });
    document.addEventListener('click', function(e) {
      if (!dropdown.contains(e.target)) { close(); }
    });
  }

  // Ensure nav links scroll to top when targeting the current page
  function ensureNavScrollTopSite() {
    document.querySelectorAll('.nav-link').forEach(function(link) {
      link.addEventListener('click', function(e) {
        try {
          var href = link.getAttribute('href') || '';
          var url = new URL(href, window.location.href);
          if (url.pathname === window.location.pathname) {
            e.preventDefault();
            window.scrollTo({ top: 0, behavior: 'smooth' });
            if (url.hash && url.hash !== window.location.hash) {
              history.replaceState(null, '', url.hash);
            } else if (!url.hash) {
              history.replaceState(null, '', url.pathname + window.location.search);
            }
          }
        } catch (err) {
          // noop
        }
      });
    });
  }

  ensureNavScrollTopSite();
  // Ensure nav links behave by scrolling to top for hashes and across-page navigation
  (function navScrollTopBehavior() {
    try {
      var navLinks = document.querySelectorAll('.nav-link');
      if (!navLinks || !navLinks.length) return;

      navLinks.forEach(function(a) {
        a.addEventListener('click', function(e) {
          var href = a.getAttribute('href');
          if (!href) return;

          // In-page hash (e.g., #home) - smooth scroll
          if (href.charAt(0) === '#') {
            e.preventDefault();
            var id = href.slice(1);
            if (!id) {
              window.scrollTo({ top: 0, behavior: 'smooth' });
              history.replaceState(null, '', '#');
              return;
            }
            var target = document.getElementById(id);
            if (target) {
              target.scrollIntoView({ behavior: 'smooth', block: 'start' });
              history.replaceState(null, '', href);
            } else {
              // If element not found, go to top
              window.scrollTo({ top: 0, behavior: 'smooth' });
            }
            return;
          }

          // For cross-page links, set flag so the next page scrolls to top on load
          try { sessionStorage.setItem('scrollToTop', '1'); } catch (err) { /* ignore */ }
          // allow default navigation to proceed
        });
      });

      // On load, if flag set then scroll to top and clear it
      if (sessionStorage.getItem('scrollToTop')) {
        try {
          window.scrollTo(0, 0);
        } catch (e) {}
        try { sessionStorage.removeItem('scrollToTop'); } catch (err) {}
      }
    } catch (e) {
      // silent
    }
  })();

})();
