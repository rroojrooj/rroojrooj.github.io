# Handoff — personal site redesign

Last updated 20 October 2026, at the end of a Claude Code on the web session. This file is the source of
truth for picking the work back up.

## Where things stand

- **Branch `redesign`** (this branch). The old al-folio theme is deleted.
  `index.html`, `assets/`, `404.html`, `README.md` and `.github/workflows/deploy.yml` here are a
  **first draft that Rooj rejected** as too template-like (big hero, pill buttons, card grid, numbered
  headings). Replace them; don't build on them.
- **Mockup**: a claude.ai Design canvas (private to Rooj):
  https://claude.ai/artifact/FVK9oM4JTpb43BF54LX2Mi. Its source is copied to `design/mockup/`:
  - `Main.dc.html` — direction **A · Paper** (has `dark` and `typeface` tweaks)
  - `VariantB.dc.html` — **B · Index**
  - `VariantC.dc.html` — **C · Letter**
  - `VariantD.dc.html` — **D · Photo-first**
  - `Photos.dc.html`, `Bookshelf.dc.html` — the other two pages (styled as A)
  - `HomeMobile.dc.html` — A at phone width in dark mode

  These are "Design Component" files: ordinary HTML with inline styles. `{{c.bg}}`-style holes are
  theme colours set in each file's `<script>` block. They need the canvas runtime to render, so read
  them as specs; don't serve them.
- **Waiting on Rooj**: pick a direction (or a mix, e.g. A plus D's photo strip), send photos, and
  approve the copy below.
- **Live site today**: the `gh-pages` branch, built from al-folio in Dec 2023. It's broken because
  every asset loads from `/home/...` (`baseurl: /home`). `master` still has the old theme and a
  `deploy.yml` that isn't valid YAML.

## What Rooj wants

- Minimal and academic-leaning: text-first, generous spacing, nothing that looks like a template.
- **Show the side of him that isn't on his CV.** CV material is folded away or left to LinkedIn.
- Little text, and every line earns its place. Curate; don't include everything he sent.

## Decisions (made by Rooj)

| Topic | Decision |
|---|---|
| Name / place | Rooj Rinchokechai · Bangkok, Thailand |
| Links | workwithrooj@gmail.com · [LinkedIn](https://www.linkedin.com/in/roojrin) · [GitHub](https://github.com/rroojrooj). **No personal X.** Belfort's [@BelfortResearch](https://x.com/BelfortResearch) is fine. |
| Featured | Only **Belfort** and **Wim's Lab**. Every other project goes in a collapsed dropdown. |
| Pages | Home, **Photos** (pictures he's taken over the years; must be easy to add more), **Bookshelf** |
| Bookshelf | Titles only, grouped by genre. **No ratings, reviews, or read/reading status.** |
| Not wanted (for now) | CV PDF, blog/writing section, photo of himself, Thai version |
| Look | Serif, warm off-white, monochrome underlined links, dark mode follows the system (no toggle) |
| Footer | "Last updated" date |
| Domain | Keep `rroojrooj.github.io` |
| Hosting | GitHub Pages **deploy from branch `master` / root**. Rooj agreed to flip this in Settings → Pages himself. |
| Stats | Yes. Proposed GoatCounter (free, no cookies, so no cookie banner); needs Rooj to sign up and send the site code. |

## Stack (see `design/research/tech-stack.md`)

Plain HTML + CSS, no build step, nothing to rot. Self-host the fonts (no Google Fonts request).
Add `.nojekyll`. Deploy from the branch and delete the workflow. If a real blog ever appears, move to
Hugo with hand-written layouts. Avoid al-folio and Hugo Blox, which repeat the old failure.

## Home page copy (current draft; Rooj may still edit)

Order matters: identity → both sides in two sentences → the two things he's building → the
non-CV side as the main section → everything else folded away.

1. **Rooj Rinchokechai** / Bangkok, Thailand / workwithrooj@gmail.com · LinkedIn · GitHub
2. Intro: "I'm building Belfort, an AI analyst for individual investors, and making high-protein
   gelato at Wim's Lab. Away from work, I run marathons, play too much golf and look after three
   giant tortoises."
3. **Now**
   - **Belfort** · Founder · 2025–now — "An AI analyst for individual investors — from finding an
     idea to telling you, after every earnings report, whether your reasons for owning it still hold.
     Fund-grade research, priced for everyone." Links: [belfortagent.xyz](https://www.belfortagent.xyz) ·
     [@BelfortResearch](https://x.com/BelfortResearch)
     (Context: Belfort aims to do a personal fund analyst's whole job: idea discovery and memos
     before buying, a live valuation and price alerts while holding, supplier, customer and competitor
     news, pre- and post-earnings briefs, and tracking whether management delivers. Don't paste this
     onto the site; it's background for the copy.)
   - **Wim's Lab** · Co-founder & head chef · 2025–now — "Premium high-protein gelato. One of four
     co-founders; I create every flavour." Link: [Instagram](https://www.instagram.com/wimslab_icecream/)
4. **Outside work** (label → line)
   - Running → Marathons in Tokyo and Cape Town.
   - Golf → Addicted enough to start building my own simulator, [Open-Birdie](https://github.com/rroojrooj/Open-Birdie).
   - Also → Bouldering, Olympic weightlifting, scuba diving.
   - Music → Guitar and vocals. Queen, the Beatles, Bob Dylan, John Mayer, Eric Clapton, B.B. King, Oasis, Taylor Swift.
   - At home → A chocolate Labrador, a beagle and three Aldabra giant tortoises.
   - On my mind → Meaning, happiness and wealth, and how they fit together.
   - Reading → The bookshelf · Photos → Pictures I've taken
5. Dropdown **Other projects** (`<details>`, closed by default)
   - Closed-loop DDoS detection · 2025 — Final-year group project at Bristol: ML detectors,
     simulated attacks and automated retraining.
     [code](https://github.com/rroojrooj/RP3-ML-DDoS-Detection-Final) ·
     [report](https://github.com/rroojrooj/RP3-ML-DDoS-Detection-Final/blob/main/paper-ML_DDoS_Detection.pdf)
   - Bangkok childcare centres · 2024 — Put the records of 271 public childcare centres in one place
     for the city. [code](https://github.com/rroojrooj/BMA_ChildCenters)
   - Fluid Options · 2022 — An options market where buyers stream premiums. Won Superfluid's Best
     DeFi Hack at ETHOnline. [showcase](https://ethglobal.com/showcase/fop-fluid-options-jjg01)
6. Dropdown **Background** — "BEng Computer Science and Electronics, University of Bristol (First
   Class, 2025). Founded the Bristol Blockchain Society. Before Belfort: SCB 10X, Token Unlocks,
   Kiatnakin Phatra, TISCO and the Bangkok Metropolitan Administration. More on LinkedIn."
7. Footer: "Happy to hear from anyone working on AI, investing or good food." / "Last updated …"

Deliberately left off: a YC mention (it could read as YC-backed), the full experience timeline,
the foundation programme and the bootcamp stats. Some personal notes Rooj shared are intentionally
not on the site; they're in the private transcripts.

## Bookshelf (titles only, by genre)

- **Investing**: The Intelligent Investor · The Most Important Thing Illuminated · University of
  Berkshire Hathaway · Buffettology · The Richest Man in Babylon
- **Business**: Zero to One · The Lean Startup · The Hard Thing About Hard Things · Blitzscaling ·
  Trillion Dollar Coach · Competitive Strategy · Principles · The Art of War
- **Biography & memoir**: Titan · When Breath Becomes Air · Tuesdays with Morrie
- **Psychology**: Man's Search for Meaning · Outliers · Talking to Strangers · Men Are from Mars,
  Women Are from Venus
- **Fiction**: Pachinko · The Kite Runner · Norwegian Wood · Men Without Women · If Cats Disappeared
  from the World · The Catcher in the Rye · Lord of the Flies · Of Mice and Men · What We Talk About
  When We Talk About Love · The Alchemist · The Five People You Meet in Heaven
- **Thrillers**: Verity · Origin

(His Goodreads paste was cut off after *The Richest Man in Babylon*, so there may be more.)

## Design directions (same content in each)

- **A · Paper** (recommended): one 640px column, Source Serif 4 at 18px / 1.6, h1 34px/600, h2
  20px/600, labels in a 112px left column for "Outside work".
  - Light: bg `#FBF9F3`, text `#1C1B19`, muted `#6E6B64`, rule `#E5E1D6`, underline `#BDB8AC`
  - Dark: bg `#161512`, text `#E8E5DC`, muted `#9A968C`, rule `#2E2C27`, underline `#5A574F`
  - Links: same colour as the text, 1px underline, 3px offset
- **B · Index**: white, Inter 16px, IBM Plex Mono uppercase labels in a 160px left column, rows
  split by thin rules. The most structured.
- **C · Letter**: no headings; five short paragraphs and a "— Rooj" sign-off. EB Garamond 21px on
  cream `#F6F1E7`. The most personal.
- **D · Photo-first**: three 4:5 photos across the top, then a large Newsreader intro beside the
  details (Inter body). The strongest if the photos are good.

Never: icons, pill buttons, cards, hover lifts, hero sections, numbered headings, animation, sticky
nav, a theme toggle.

## Photos page plan

- Files at `photos/<year>/<slug>.jpg`. Resize to about 2000px on the long edge, plus a roughly 800px
  thumbnail. **Strip all EXIF, including GPS location.** Captions read "Place, Month Year". Newest
  year first; each image links to the full-size file. No JS lightbox.
- Adding a photo = drop in the file and add one `<figure>` line. Document the steps in the README. A
  small local helper script (resize + strip EXIF) is fine as long as the site itself stays build-free.

## Next steps

1. Rooj picks a direction (or a mix) and sends photos with place and year.
2. Rebuild `index.html`, `photos/index.html`, `bookshelf/index.html`, `404.html` and one stylesheet
   with self-hosted fonts. Delete `.github/workflows/deploy.yml` and the old draft CSS/JS.
3. Check it: screenshots at desktop and phone width in light and dark, no horizontal scroll, every
   link resolves, valid HTML.
4. Add GoatCounter once Rooj has the code.
5. Push, then merge to `master` (ask Rooj whether he wants a PR). Rooj sets Pages → Deploy from
   branch → `master` / root. Check the live site, then ask before deleting the `gh-pages` branch.

## Reference

- `design/research/academic-homepages.md` — Jon Barron, Sasha Rush, Shunyu Yao and others
- `design/research/minimal-tech-sites.md` — Gwern, Patrick Collison, Steph Ango and others
- `design/research/tech-stack.md` — why plain HTML, and how to deploy
