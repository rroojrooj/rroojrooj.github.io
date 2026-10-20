# rroojrooj.github.io

Rooj Rinchokechai's personal site. Plain HTML + CSS served by GitHub Pages, no build step.

## Start here

- `HANDOFF.md` is the source of truth for the redesign: decisions, current copy, the four design
  directions, the photos plan and the next steps. Read it before changing anything.
- `design/mockup/chosen-g/` is the chosen home layout (G · Mix 2) as real HTML/CSS. It is the
  build spec; open `index.html` in a browser.
- `design/mockup/*.dc.html` are the earlier canvas boards (Main = A Paper, VariantB = Index, VariantC = Letter,
  VariantD = Photo-first, plus Photos, Bookshelf and HomeMobile). They need the claude.ai canvas
  runtime, so read them as specs; don't serve them. `design/research/*.md` explain the choices.
- Work on branch `redesign`. Don't push to or merge into `master` without asking. `gh-pages` is the
  old, broken al-folio build; ask before deleting it.

## Ground rules

- Minimal, academic, text-first. Little text; every line earns its place. Show the side of Rooj that
  isn't on the CV.
- Plain HTML/CSS, no framework, no build step. Self-host the fonts (no Google Fonts request).
- Never: icons, pill buttons, cards, hover lifts, hero sections, numbered headings, animation, sticky
  nav, a theme toggle. Dark mode follows the system setting.
- The current `index.html`, `assets/` and `404.html` are a rejected first draft. Replace them; don't
  build on them.
- Photos: strip all EXIF (including GPS) before committing.
- The repo is public. Don't commit private notes or session transcripts.

## Checking a change

Screenshots at desktop and phone width, in light and dark; no horizontal scroll; every link resolves;
valid HTML.

## gstack

Use gstack's `/browse` for web browsing and screenshots. Never use `mcp__claude-in-chrome__*` tools.

Useful here:
- `/design-consultation`, `/plan-design-review` — settle the direction before building
- `/design-html` — turn the approved mockup into final HTML/CSS
- `/design-review` — visual QA on the built pages, with fixes
- `/qa` or `/qa-only` — test the site in a real browser
- `/review` before merging; `/ship` to open the PR
- `/context-save` / `/context-restore` — carry state between sessions

## GBrain Configuration (configured by /setup-gbrain)
- Mode: local-stdio
- Engine: postgres
- Config file: ~/.gbrain/config.json (mode 0600)
- Setup date: 2026-10-20
- MCP registered: yes
- Artifacts sync: full
- Current repo policy: read-write
