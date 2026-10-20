# rroojrooj.github.io

Personal website of Rooj Rinchokechai: plain HTML and CSS, no JavaScript, no build step.

## Files

- `index.html`: the home page.
- `photos/index.html`: pictures taken over the years, newest year first.
- `bookshelf/index.html`: book titles grouped by genre.
- `404.html`: shown for any missing address (uses absolute paths).
- `assets/css/site.css`: the one stylesheet. Colours are at the top; dark mode follows the
  visitor's system setting.
- `assets/fonts/`: Source Serif 4 (variable, Latin subset), self-hosted, with its licence (`OFL.txt`).

Search for `[` or `class="ph"` to find placeholders still to fill in.

## Adding photos

1. Remove all EXIF data, including GPS location.
2. Resize to about 2000px on the long edge. For the Photos page, also make an 800px thumbnail.
3. **Photos page:** save as `photos/<year>/<slug>.jpg` and `photos/<year>/<slug>-800.jpg`, then add
   one line to that year's gallery (newest first). The exact line is in the comment at the top of
   `photos/index.html`. Captions read "Place, Month Year".
4. **Home page:** save under `assets/home/` and replace the matching placeholder `<div class="ph">`
   or `<span class="ph">` with an `<img>` of the same shape. The comment at the top of `index.html`
   shows how.
5. Update the "Last updated" line in the footer.

## Previewing locally

```sh
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Deploying

GitHub Pages deploys from the `master` branch, root folder (Settings → Pages → Deploy from a
branch). There is no workflow; pushing to `master` publishes the site.
