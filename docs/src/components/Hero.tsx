import React from 'react'

export default function Hero({ title, subtitle, description }: { title: string; subtitle?: string; description?: string }) {
  return (
    <section className="hero min-h-screen pt-24 grid grid-cols-1 md:grid-cols-2 items-center">
      <div>
        <h1 className="hero-title font-serif text-5xl leading-tight mb-4">{title}
          <span className="block text-accent font-serif text-2xl font-bold mt-2">{subtitle}</span>
        </h1>
        <p className="text-lg text-text-secondary mb-6">{description}</p>
        <div className="grid grid-cols-2 gap-3 max-w-lg">
          <a className="bg-accent text-white px-4 py-3 rounded-lg font-semibold text-center" href="#">Get Started</a>
          <a className="border border-border px-4 py-3 rounded-lg font-semibold text-center" href="#">Learn More</a>
        </div>
      </div>
      <div className="hero-visual flex justify-center items-center">
        <div className="compass-container w-72 h-72">
          <div className="compass-ring border-2 border-accent rounded-full w-full h-full relative animate-spin-slow"></div>
          <div className="compass-needle absolute w-1 h-40 bg-gradient-to-b from-accent to-gray-400 rounded-sm left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2"></div>
          <div className="compass-center absolute w-6 h-6 bg-accent rounded-full left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2"></div>
        </div>
      </div>
    </section>
  )
}
