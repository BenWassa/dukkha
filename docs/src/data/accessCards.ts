export type AccessCardItem = {
  title: string
  icon: string
  painPoint: string
  description: string
  link: string
}

export const accessCards: AccessCardItem[] = [
  {
    title: 'Focus Sprint',
    icon: '/images/icons/focus-target.svg',
    painPoint: 'Constant Distraction',
    description: 'Master your dopamine compass and break free from variable reward schedules that hijack attention.',
    link: '/site/attention.html#protocol-the-focus-sprint-7-day-experiment',
  },
  {
    title: 'Recovery Reset',
    icon: '/images/icons/moon2.svg',
    painPoint: 'Burnout & Exhaustion',
    description: 'Restore your dopamine baseline through strategic sleep optimization and stress management protocols.',
    link: '/site/recovery.html#protocol-the-recovery-reset-48-hour-experiment',
  },
  {
    title: 'Myth Busting',
    icon: '/images/icons/myth-busting.svg',
    painPoint: 'Confusion & Misinformation',
    description: 'Expose the lies we tell ourselves about dopamine, motivation, and reward.',
    link: '/site/myths.html',
  },
]
