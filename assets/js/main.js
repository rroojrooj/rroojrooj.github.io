// Light/dark toggle. With no saved choice the page follows the OS setting.
const root = document.documentElement;
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');
const toggle = document.querySelector('.theme-toggle');

function currentTheme() {
  return root.dataset.theme || (prefersDark.matches ? 'dark' : 'light');
}

toggle.addEventListener('click', () => {
  const next = currentTheme() === 'dark' ? 'light' : 'dark';
  root.dataset.theme = next;
  try {
    localStorage.setItem('theme', next);
  } catch (e) {
    // Storage blocked (private mode etc.) — the toggle still works for this visit.
  }
});
