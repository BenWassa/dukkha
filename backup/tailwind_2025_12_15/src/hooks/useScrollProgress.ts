import { useEffect, useState } from 'react'

export function useScrollProgress({ visibleThreshold = 0 } = {}) {
  const [progress, setProgress] = useState(0)
  const [visible, setVisible] = useState(false)

  useEffect(() => {
    function update() {
      const h = document.body.scrollHeight - window.innerHeight
      const y = window.scrollY || window.pageYOffset
      const r = h > 0 ? y / h : 0
      setProgress(r)
      setVisible(y > (visibleThreshold || 0))
    }
    update()
    window.addEventListener('scroll', update, { passive: true })
    window.addEventListener('resize', update, { passive: true })
    return () => {
      window.removeEventListener('scroll', update)
      window.removeEventListener('resize', update)
    }
  }, [visibleThreshold])

  return { progress, visible }
}
