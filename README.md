# rroojrooj.github.io

Personal website of Rooj Rinchokechai — plain HTML and CSS, no build step.

## Editing

- `index.html` — all the content. Search for `[` to find placeholders still to fill in.
- `assets/css/style.css` — colours (top of the file), fonts and layout.
- `assets/js/main.js` — the light/dark toggle.

## Previewing locally

```sh
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Deploying

Every push to `master` runs `.github/workflows/deploy.yml`, which copies the site files to the
`gh-pages` branch. GitHub Pages serves that branch at https://rroojrooj.github.io.
