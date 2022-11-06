/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./blog_codemy/**/*.html'],
  theme: {
    screens: {
      'mobile': '480px',
      'tablet': '768px',
      'smScr': '976px',
      'lgScr': '1440px',
    },
    extend: {
      backgroundImage: {
        'hero': "url('../blog_codemy/stars.png')",
      },
      colors: {
        brightRed: 'hsl(12, 88%, 59%)',
        brightRedLight: 'hsl(12, 88%, 69%)',
        brightRedSupLight: 'hsl(12, 88%, 95%)',
        darkBlue: 'hsl(228, 39%, 23%)',
        darkGrayishBlue: 'hsl(227, 12%, 61%)',
        veryDarkBlue: 'hsl(233, 12%, 13%)',
        veryPaleRed: 'hsl(13, 100%, 96%)',
        veryLightGray: 'hsl(0, 0%, 98%)',
      },
    },
  },
  plugins: [],
}
