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
})();
