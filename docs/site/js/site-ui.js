(function() {
  // reading progress
  var bar = document.querySelector('.read-progress__bar');
  if (bar) {
    var updateProgress = function() {
      var h = document.body.scrollHeight - window.innerHeight;
      var y = window.scrollY;
      var r = h > 0 ? y / h : 0;
      bar.style.transform = 'scaleY(' + r + ')';
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

    function buildMenu(list) {
      menu.innerHTML = '';
      var first = document.createElement('li');
      var firstLink = document.createElement('a');
      firstLink.href = overviewPath;
      firstLink.textContent = 'All Protocols';
      firstLink.setAttribute('role', 'menuitem');
      first.appendChild(firstLink);
      menu.appendChild(first);
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

    toggle.addEventListener('click', function(e) {
      e.preventDefault();
      var isOpen = dropdown.classList.toggle('open');
      toggle.setAttribute('aria-expanded', isOpen);
      if (isOpen) { getItems()[0] && getItems()[0].focus(); }
    });
    toggle.addEventListener('keydown', function(e) {
      if (e.key === 'ArrowDown') { e.preventDefault(); open(); getItems()[0] && getItems()[0].focus(); }
    });
    dropdown.addEventListener('mouseenter', open);
    dropdown.addEventListener('mouseleave', close);

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
