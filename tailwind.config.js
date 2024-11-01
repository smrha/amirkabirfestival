/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    fontFamily: {
      'DanaRegular': 'DanaRegular',
    },
    container: {
      padding: {
        DEFAULT: '15px'
      }
    },
    screens: {
      sm: '480px',
      md: '768px',
      lg: '976px',
      xl: '1440px',
    },
    colors: {
      primary: {
        "50": "#ecfeff",
        "100": "#cffafe",
        "200": "#a5f3fc",
        "300":"#67e8f9",
        "400":"#22d3ee",
        "500":"#06b6d4",
        "600":"#0891b2",
        "700":"#0e7490",
        "800":"#155e75",
        "900":"#164e63",
        "950":"#083344"
      },
      secondary: '#808080',
      accent: {
        DEFAULT: '#1cbccf',
        secondary: '#18abbc',
        tertiary: '#90c6cd',
      },
      gray: '#e8f0f1',
    },
    boxShadow: {
      custom1: '0px 2px 40px 0px rgba(8, 70, 78, 0.08)',
      custom2: '0px 0px 30px 0px rgba(8, 73, 81, 0.06)',
    },
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

