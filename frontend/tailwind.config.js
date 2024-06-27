module.exports = {
  darkMode: "class",
  content: ["./src/**/*.{js,ts,jsx,tsx}"],
  plugins: [require("daisyui", "tailwindcss-dark-mode")],
  daisyui: {
    themes: ["light", "dark"],
  },
};
