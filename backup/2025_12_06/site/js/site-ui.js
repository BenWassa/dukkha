(function() {
  // Collapse Notes & Citations (footnotes) by default so they don't show expanded on page load.
  // Individual page scripts still attach toggle handlers to the header to allow expanding.
  try {
    var _fnSections = document.querySelectorAll('.footnotes');
    _fnSections.forEach(function(s) { s.classList.add('collapsed'); });
  } catch (e) {
    // noop
  }
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

    // Align the progress container to the page content width (not full viewport)
    function alignProgressToContent() {
      var content = document.querySelector('.page-content') || document.querySelector('.container') || document.querySelector('main') || document.body;
      if (!content) return;
      var rect = content.getBoundingClientRect();
      // Position fixed element using viewport coordinates
      progress.style.left = rect.left + 'px';
      progress.style.width = rect.width + 'px';
      // remove any translate used by CSS centering
      progress.style.transform = 'none';
      // keep top aligned to nav if present
      if (nav) { progress.style.top = nav.offsetHeight + 'px'; }
    }

    var updateProgress = function() {
      var h = document.body.scrollHeight - window.innerHeight;
      var y = window.scrollY;
      var r = h > 0 ? y / h : 0;
      // set bar width as percentage of the progress container
      bar.style.width = (r * 100) + '%';
      if (y > showPoint) {
        progress.classList.add('visible');
      } else {
        progress.classList.remove('visible');
      }
    };

    // initial alignment and on resize
    alignProgressToContent();
    window.addEventListener('resize', alignProgressToContent, { passive: true });
    window.addEventListener('scroll', updateProgress, { passive: true });
    updateProgress();
  }

  // playful prompts
  var prompt = document.querySelector('.read-prompt');
  if (prompt && !sessionStorage.getItem('readPromptDismissed') && window.location.pathname.includes('attention.html')) {
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
      if (toggle) {
        try {
          var existing = toggle.getAttribute('href');
          // Only override if there is no href or it's a placeholder '#'
          if (!existing || existing === '#') {
            toggle.setAttribute('href', overviewPath);
          }
        } catch (e) {
          // fallback: set href if getAttribute throws for any reason
          try { toggle.setAttribute('href', overviewPath); } catch (err) {}
        }
      }

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
  // After menu is built, ensure nav active state is applied (handles protocol subpages)
  try { setActiveNavState(); } catch (e) { /* noop */ }
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

      // Robust active-nav detection: mark top-level nav links and protocol subpage links as active
      function setActiveNavState() {
        var currentPath = window.location.pathname || window.location.href;
        // normalize to just pathname
        try { currentPath = new URL(window.location.href).pathname; } catch (e) {}

        function nameOf(path) { return (path || '').split('/').filter(Boolean).pop() || path; }

        // mark top-level links
        document.querySelectorAll('.nav-link').forEach(function(link) {
          try {
            var href = link.getAttribute('href') || '';
            if (!href || href === '#') return;
            var resolved = new URL(href, window.location.href).pathname;
            // exact match
            if (resolved === currentPath) {
              link.classList.add('active');
              return;
            }
            // match by filename
            if (nameOf(resolved) === nameOf(currentPath)) {
              link.classList.add('active');
              return;
            }
            // protocols parent should be active for any /protocols/ subpage
            if (nameOf(resolved) === 'protocols.html' && currentPath.indexOf('/protocols/') !== -1) {
              link.classList.add('active');
              return;
            }
            // clear other links
            link.classList.remove('active');
          } catch (e) { /* noop */ }
        });

        // mark specific protocol submenu item (if present)
        if (menu) {
          Array.prototype.slice.call(menu.querySelectorAll('a')).forEach(function(a) {
            try {
              var href = a.getAttribute('href') || '';
              var resolved = new URL(href, window.location.href).pathname;
              if (resolved === currentPath || nameOf(resolved) === nameOf(currentPath)) {
                a.classList.add('active');
                // also ensure the parent toggle shows active so user sees category highlighted
                var toggle = document.querySelector('.nav-dropdown__toggle');
                if (toggle) toggle.classList.add('active');
              } else {
                a.classList.remove('active');
              }
            } catch (e) { /* noop */ }
          });
        }
      }

      // Run once now in case menu was synchronous or already present
      try { setActiveNavState(); } catch (e) {}

      function getItems() {
        return Array.prototype.slice.call(menu.querySelectorAll('a'));
      }
      function open() {
        dropdown.classList.add('open');
        // preserve any existing aria-expanded attribute set in markup; do not overwrite

        // Position the dropdown correctly relative to the toggle button
        var rect = toggle.getBoundingClientRect();
        menu.style.left = rect.left + 'px';
        menu.style.top = (rect.bottom + 8) + 'px'; // 8px margin
      }
      function close() {
        dropdown.classList.remove('open');
        // preserve aria-expanded attribute
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

  // Replace footer contact mailto link with a GitHub icon link (site-wide)
  try {
    var footerLinks = document.querySelector('.footer-links');
    if (footerLinks) {
      var mailto = footerLinks.querySelector('a[href^="mailto:"]');
      if (mailto) {
        // Candidate paths to the white GitHub mark SVG. We'll try each until one loads.
        var candidates = [
          'images/icons/github-mark/github-mark-white.svg',
          '../images/icons/github-mark/github-mark-white.svg',
          '../../images/icons/github-mark/github-mark-white.svg',
          '/docs/images/icons/github-mark/github-mark-white.svg',
          '/images/icons/github-mark/github-mark-white.svg'
        ];

        function tryLoad(index) {
          if (index >= candidates.length) {
            // fallback: use the first candidate without waiting
            insertGhLink(candidates[0]);
            return;
          }
          var testSrc = candidates[index];
          var tester = new Image();
          var done = false;
          tester.onload = function() {
            if (done) return; done = true;
            insertGhLink(testSrc);
          };
          tester.onerror = function() {
            if (done) return; done = true;
            // try next candidate
            tryLoad(index + 1);
          };
          // small timeout in case network stalls (use setTimeout to fallback)
          var to = setTimeout(function() {
            if (done) return; done = true;
            tryLoad(index + 1);
          }, 400);
          // start loading
          tester.src = testSrc;
        }

        function insertGhLink(src) {
          try {
            var ghLink = document.createElement('a');
            ghLink.href = 'https://github.com/BenWassa/dukkha';
            ghLink.target = '_blank';
            ghLink.rel = 'noopener noreferrer';
            ghLink.className = 'github-link';
            var img = document.createElement('img');
            img.src = src;
            img.alt = 'GitHub';
            img.className = 'github-icon';
            // ensure the image uses the white mark; if src doesn't indicate white, we prefer explicit file
            if (!/white/i.test(src)) img.src = src;
            ghLink.appendChild(img);
            mailto.parentNode.replaceChild(ghLink, mailto);
          } catch (e) {
            // final fallback — do nothing
          }
        }

        // kick off attempts
        tryLoad(0);
      }
    }
  } catch (e) { /* noop */ }

})();
