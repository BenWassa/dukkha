import React from 'react'
import { Outlet } from 'react-router-dom'
import NavBar from './NavBar'

export default function Layout() {
  return (
    <div className="bg-surface min-h-screen text-text-primary">
      <NavBar />
      <main className="max-w-6xl mx-auto px-6 pt-24 pb-16">
        <Outlet />
      </main>
    </div>
  )
}
