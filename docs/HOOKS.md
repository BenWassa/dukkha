# Hooks and Refactor Strategy

This document describes refactor targets from `site/js/site-ui.js` into React hooks and components.

## Hooks to Implement

### useScrollProgress

- Tracks `window.scroll` and returns progress value (0..1) and whether progress bar should be visible.
- It also exposes a `ref` for the container (if needed) to align the progress bar width.

Example:
```ts
import { useEffect, useState } from 'react';

export function useScrollProgress() {
  const [value, setValue] = useState(0);
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const update = () => {
      const h = document.body.scrollHeight - window.innerHeight;
      const y = window.scrollY || window.pageYOffset;
      setValue(h > 0 ? y / h : 0);
      // visible threshold can come from params
      setVisible(y > 300);
    };
    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update, { passive: true });
    update();
    return () => {
      window.removeEventListener('scroll', update);
      window.removeEventListener('resize', update);
    };
  }, []);
  return { value, visible };
}
```

### useDropdown

- Simple hook to show/hide a dropdown, manage key navigation and trap focus if open.
- Returns `open`, `toggle`, `close`, and `ref`.

### ScrollToTop component

- For React Router v6: `useEffect` to scroll to top on route change.

Example:
```tsx
import { useEffect } from 'react';
import { useLocation } from 'react-router-dom';

export default function ScrollToTop() {
  const { pathname } = useLocation();
  useEffect(() => window.scrollTo(0, 0), [pathname]);
  return null;
}
```

---

## Migration tips

- Keep `site-ui.js` behavior (menus, progress bar) as reference while migrating. Implement unit tests for the hooks to catch regressions.
- Replace `fetch(manifest.json)` usage with a simple fetch in the NavBar component or include data as a JSON file in `public/` during the build and import it as `fetch('/protocols/manifest.json')`.
- For the `github` icon insertion fallback logic (detecting available paths), in React we can use `img` with fallback `onError` to set a different `src`.

If you'd like, I can scaffold the hooks and an example NavBar/Progress component to show how they integrate. Would you like me to scaffold these files now?