# rroojrooj.github.io

Personal website of Rooj Rinchokechai: plain HTML and CSS, no JavaScript, no build step.

The website is everything in `docs/`. The rest of the repo (`HANDOFF.md`, `CLAUDE.md`, `DESIGN.md`,
`design/`) is notes and design material and is not published.

## Files

- `docs/index.html`: the home page.
- `docs/photos/index.html`: pictures taken over the years, newest year first.
- `docs/bookshelf/index.html`: book titles grouped by genre, each with its cover. The covers are in
  `docs/bookshelf/covers/`.
- `docs/404.html`: shown for any missing address (uses absolute paths).
- `docs/assets/css/site.css`: the one stylesheet. Colours are at the top; dark mode follows the
  visitor's system setting.
- `docs/assets/fonts/`: Source Serif 4 (variable, Latin subset), self-hosted, with its licence (`OFL.txt`).

Search for `[` or `class="ph"` to find placeholders still to fill in. Empty photo slots are hidden
on the live site by one CSS rule (`figure:has(.ph)` etc. in `site.css`): a slot appears as soon as
its placeholder is replaced with an `<img>`. A collage, or a year on the Photos page, appears once
all its placeholders are replaced.

## Adding photos

1. Remove all EXIF data, including GPS location.
2. Resize to about 2000px on the long edge. For the Photos page, also make an 800px thumbnail.
3. **Photos page:** save as `docs/photos/<year>/<slug>.jpg` and `docs/photos/<year>/<slug>-800.jpg`,
   then add one line to that year's gallery (newest first). The exact line is in the comment at the
   top of `docs/photos/index.html`. Captions read "Place, Year". Running photos go in
   `docs/photos/running/` and the Running section instead; race photos read "Race, Year · time".
4. **Home page:** save under `docs/assets/home/` and replace the matching placeholder
   `<div class="ph">` or `<span class="ph">` with an `<img>` of the same shape. The comment at the
   top of `docs/index.html` shows how.
5. Update the "Last updated" line in the footer.

## Adding a book

1. Find the book's common English edition on openlibrary.org and download its cover from
   `https://covers.openlibrary.org/b/id/<cover ID>-L.jpg`. Never link to the image there: the site
   makes no third-party requests.
2. Remove all metadata (EXIF and the rest).
3. Pick a slug from the title (`the-kite-runner`). Save the cover at its own size, at most 480px wide,
   as `docs/bookshelf/covers/<slug>-large.jpg`, and a 48×72 crop of it as
   `docs/bookshelf/covers/<slug>.jpg`.
4. Copy the line in the comment at the top of `docs/bookshelf/index.html` into the book's genre and
   fill in the slug, title, author and the large file's width and height.
5. Add the edition to `design/research/bookshelf-covers.md` and update the "Last updated" line.

## Previewing locally

```sh
cd docs && python3 -m http.server 8000
```

Then open http://localhost:8000.

## Deploying

GitHub Pages deploys from the `master` branch, `/docs` folder (Settings → Pages → Deploy from a
branch → `master` → `/docs`). There is no workflow; pushing to `master` publishes the site.
