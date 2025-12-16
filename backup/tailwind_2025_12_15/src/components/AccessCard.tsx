import React from 'react'

export default function AccessCard({ title, icon, painPoint, description, link }: { title: string; icon: string; painPoint: string; description: string; link: string }) {
  return (
    <article className="access-card group bg-surface-elevated border border-border rounded-lg overflow-hidden shadow-sm hover:shadow-lg transition-transform transform hover:-translate-y-1">
      <div className="card-header flex items-start justify-between p-4 border-b border-border bg-gradient-to-br from-black/5 to-transparent">
        <div className="card-icon w-20 h-20 flex items-center justify-center">
          <img src={icon} alt="" className="w-12 h-12" />
        </div>
        <div className="card-pain-point text-right">
          <div className="pain-indicator text-sm uppercase">Struggling with</div>
          <div className="pain-text font-semibold text-base">{painPoint}</div>
        </div>
      </div>
      <div className="card-content p-4 flex flex-col gap-3">
        <h3 className="card-title text-2xl font-semibold">{title}</h3>
        <p className="card-theme italic text-accent">{title}</p>
        <p className="card-description text-text-secondary">{description}</p>
        <a href={link} className="card-cta inline-flex mt-4 px-4 py-3 rounded-lg bg-accent text-white font-semibold">Explore →</a>
      </div>
    </article>
  )
}
