/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#1e293b', // --color-primary
          light: '#334155',   // --color-primary-light
        },
        accent: {
          DEFAULT: '#c9a961', // --color-accent
          light: '#d4b574',   // --color-accent-light
        },
        surface: {
          DEFAULT: '#f8fafc', // --color-surface
          elevated: '#ffffff', // --color-surface-elevated
        },
        text: {
          primary: '#0f172a', // --color-text-primary
          secondary: '#475569', // --color-text-secondary
          muted: '#64748b',   // --color-text-muted
        },
        border: {
          DEFAULT: '#e2e8f0', // --color-border
          light: '#f1f5f9',
        },
        success: '#059669',
        warning: '#d97706',
        error: '#dc2626'
      },
      fontFamily: {
        serif: ['Crimson Text', 'serif'],
        sans: ['Inter', 'sans-serif'],
        mono: ['SF Mono', 'monospace'],
      },
      backgroundImage: {
        'hero-gradient': 'linear-gradient(135deg, #f8fafc 0%, #fefefe 100%)',
        'radial-glow': 'radial-gradient(circle at 30% 70%, rgba(201, 169, 97, 0.1) 0%, transparent 50%)',
      }
    },
  },
  plugins: [],
}
