import React from 'react'
import Hero from '../components/Hero'
import AccessCard from '../components/AccessCard'
import { accessCards } from '../data/accessCards'

export default function Home() {
  return (
    <>
      <Hero
        title="Project Dukkha"
        subtitle="A Field Guide to the Rewarded Animal"
        description="Understanding dopamine as a living, mythic force shaping culture, habits, motivation, and collective drift."
      />

      <section className="my-12">
        <h2 className="text-3xl font-serif mb-4">Navigate Your Journey</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {accessCards.map((c, i) => (
            <AccessCard key={i} {...c} />
          ))}
        </div>
      </section>
    </>
  )
}
