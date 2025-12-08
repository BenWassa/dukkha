import { useEffect, useRef, useState } from 'react'

export function useDropdown(initialOpen = false) {
  const [open, setOpen] = useState(initialOpen)
  const ref = useRef<HTMLElement | null>(null)

  useEffect(() => {
    function handleClick(e: MouseEvent) {
      if (!ref.current) return
      if (ref.current.contains(e.target as Node)) return
      setOpen(false)
    }
    function handleKey(e: KeyboardEvent) {
      if (e.key === 'Escape') setOpen(false)
    }
    document.addEventListener('click', handleClick)
    document.addEventListener('keydown', handleKey)
    return () => {
      document.removeEventListener('click', handleClick)
      document.removeEventListener('keydown', handleKey)
    }
  }, [ref])

  return { open, setOpen, ref }
}
