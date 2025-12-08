import React from 'react'
import NavBar from './components/NavBar'
import Hero from './components/Hero'
import AccessCard from './components/AccessCard'

const cards = [
  { title: 'Focus Sprint', icon: '/images/icons/focus-target.svg', painPoint: 'Constant Distraction', description: 'Master your dopamine compass and break free from variable reward schedules that hijack attention.', link: '/site/attention.html#protocol-the-focus-sprint-7-day-experiment' },
  { title: 'Recovery Reset', icon: '/images/icons/moon2.svg', painPoint: 'Burnout & Exhaustion', description: 'Restore your dopamine baseline through strategic sleep optimization and stress management protocols.', link: '/site/recovery.html#protocol-the-recovery-reset-48-hour-experiment' },
  { title: 'Myth Busting', icon: '/images/icons/myth-busting.svg', painPoint: 'Confusion & Misinformation', description: 'Expose the lies we tell ourselves about dopamine, motivation, and reward.', link: '/site/myths.html' },
]

export default function App() {
  return (
    <div className="bg-surface min-h-screen text-text-primary">
      <NavBar />
      <main className="max-w-6xl mx-auto px-6">
        <Hero title="Project Dukkha" subtitle="A Field Guide to the Rewarded Animal" description="Understanding dopamine as a living, mythic force shaping culture, habits, motivation, and collective drift." />

        <section className="my-12">
          <h2 className="text-3xl font-serif mb-4">Navigate Your Journey</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {cards.map((c, i) => (
              <AccessCard key={i} {...c} />
            ))}
          </div>
        </section>
      </main>
    </div>
  )
}
