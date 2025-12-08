import React, { useState, useEffect, useRef } from 'react'

export default function NavBar() {
  const [open, setOpen] = useState(false)
  const toggleRef = useRef<HTMLButtonElement | null>(null)
  useEffect(() => {
    function handleKeydown(e: KeyboardEvent) {
      if (e.key === 'Escape') setOpen(false)
    }
    document.addEventListener('keydown', handleKeydown)
    return () => document.removeEventListener('keydown', handleKeydown)
  }, [])

  return (
    <nav className="fixed top-0 left-0 right-0 bg-transparent z-50">
      <div className="max-w-6xl mx-auto flex items-center gap-6 py-3 px-4">
        <div className="brand flex items-center gap-3">
          <div className="brand-symbol w-10 h-10 bg-accent rounded-full" aria-hidden="true"></div>
          <div className="font-serif font-semibold">Project Dukkha</div>
        </div>
        <ul className="ml-auto hidden md:flex gap-4 items-center">
          <li><a className="nav-link text-sm font-medium" href="#home">Home</a></li>
          <li><a className="nav-link text-sm font-medium" href="/site/attention.html">Focus &amp; Attention</a></li>
          <li><a className="nav-link text-sm font-medium" href="/site/recovery.html">Recovery &amp; Baseline</a></li>
          <li className="relative">
            <button ref={toggleRef} aria-expanded={open} onClick={() => setOpen(s => !s)} className="nav-link text-sm font-medium">
              Protocols
            </button>
            <ul className={`absolute right-0 mt-3 w-56 bg-white border border-border rounded-lg shadow-lg p-3 ${open ? 'block' : 'hidden'}`}>
              <li className="p-2"><a className="nav-dropdown__link" href="/site/protocols/digital-detox-protocol.html">Digital Detox Protocol</a></li>
              <li className="p-2"><a className="nav-dropdown__link" href="/site/protocols/sleep-optimization-protocol.html">Sleep Optimization Protocol</a></li>
            </ul>
          </li>
          <li><a className="nav-link text-sm font-medium" href="/site/library.html">Library</a></li>
        </ul>
      </div>
    </nav>
  )
}
