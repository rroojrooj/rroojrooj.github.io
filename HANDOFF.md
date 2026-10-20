# Handoff — personal site redesign

Last updated 20 October 2026, at the end of a Claude Code on the web session. This file is the source of
truth for picking the work back up.

## Where things stand

- **Branch `redesign`** (this branch). The old al-folio theme is deleted. The first draft Rooj
  rejected (big hero, pill buttons, card grid, numbered headings) was replaced on 20 Oct 2026 by the
  **real site, built from layout G**, in **`docs/`**: `index.html`, `photos/index.html`,
  `bookshelf/index.html`, `404.html`, `assets/css/site.css`, self-hosted Source Serif 4 in
  `assets/fonts/` (OFL), and a monochrome favicon. No JavaScript, no workflow. Photos are
  placeholders until Rooj sends them, and empty photo slots are hidden by CSS on the live site
  (they appear as soon as a real `<img>` replaces the placeholder). Design tokens and rules are in
  `DESIGN.md`.
- **Live since 20 Oct 2026**: `redesign` was fast-forwarded into `master` and GitHub Pages switched to
  `master` → `/docs`. Pushing to `master` now publishes. Keep working on `redesign` (or a branch)
  and merge when ready. The old `gh-pages` branch still exists; ask Rooj before deleting it.
  Checked at 390px and 1280px in light and dark: self-hosted font loads, no third-party requests,
  no horizontal scroll, no console errors, all internal links resolve.
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
- **Direction chosen (20 Oct 2026, local session): G · Mix 2** — direction A's type and colours,
  with photos mixed in loosely (Rooj liked B and C: "no exactly fixed format"). The real-HTML
  mockup is in `design/mockup/chosen-g/` (`index.html` + `base.css`, `preview.png` shows desktop
  light and phone dark). It is the spec for the build. All seven variants compared (A Strip,
  B Plate, C Margin, D Portrait, E Contact sheet, F/G mixes) live in gstack's design folder,
  `~/.gstack/projects/rroojrooj-rroojrooj.github.io/designs/home-photos-20261020/`.
- **Waiting on Rooj**: the photos (see "Home page photo slots" below), and approval of the copy.
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
| Hosting | GitHub Pages **deploy from branch `master` / `/docs`** (changed from root on 20 Oct 2026 so the notes and mockups stay off the website). Rooj agreed to change this in Settings → Pages. |
| Stats | Yes. Proposed GoatCounter (free, no cookies, so no cookie banner); needs Rooj to sign up and send the site code. |
| Layout | **G · Mix 2**: name, intro, then one wide photo; small photos floated inside the rows they illustrate; Bristol Blockchain Society block with a loose collage. No rigid grid. |
| Bristol Blockchain Society | Its own block on Home with **a few photos** from running the society. Separate from the Photos page (pictures Rooj took over the years). |
| Photo of Rooj | Still no portrait (variant D was shown and not picked). |

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
   giant tortoises." Then the wide photo (layout G).
3. **Now**
   - **Belfort** · Founder · 2025–now — "I believe investing can be far easier and more effective than
     it is today." Links: [belfortagent.xyz](https://www.belfortagent.xyz) ·
     [@BelfortResearch](https://x.com/BelfortResearch)
     Below it, a closed **"Why I'm building it"** dropdown: three short first-person paragraphs that
     read as one story. The work is slow (6+ years as a fundamental investor; ideas, research,
     deciding and keeping up all take too much time and effort), institutions have the technology and
     teams while individuals usually don't (they deserve the same level of intelligence), and that's
     why Belfort exists (institution-level support for anyone who invests seriously, without the price).
     **Rooj's core message, in Rooj's words:** the investing journey can be easier, more efficient and
     more effective; retail investors should get the same technology and intelligence as institutions,
     at a lower price. Write from that. Notes on this copy: plain, easy sentences that connect; don't
     invent habits or details Rooj didn't give; **never "my dream" / "the dream"**.
     **Rule from Rooj: this is a personal page, not the product page.** Belfort copy here is about
     Rooj's goal, vision and mission, never feature lists or how it works. (A feature-row version was
     tried and rejected on 20 Oct 2026.)
     (Rewritten 20 Oct 2026: the old line repeated the intro's "AI analyst for individual investors".
     Rooj's positioning, as background only: every investing tool waits to be asked; Belfort knows the
     investor (holdings, style, themes, reasons for owning), works before being asked from primary
     sources, remembers what each company said across years, and backs every claim with its source,
     saying so when it can't prove something. Longer term it aims to do a personal fund analyst's
     whole job: ideas and memos before buying, live valuation, price alerts and supply-chain news
     while holding, pre- and post-earnings briefs, and tracking whether management delivers. Don't
     paste this onto the site.)
   - **Wim's Lab** · Co-founder & head chef · 2025–now — "Premium high-protein gelato. One of four
     co-founders; I create every flavour." Link: [Instagram](https://www.instagram.com/wimslab_icecream/)
4. **Outside work** (label → line)
   - Running → Marathons in Tokyo and Cape Town, 2026. Shorter races in Sydney, New York, Bath and Bristol.
     (Facts from Rooj: Tokyo Marathon 2026, Cape Town Marathon 2026, TCS Sydney Marathon 10k 2025,
     TCS New York Marathon 5k 2025, Bath Half 2024 and 2025, Bristol 10k 2025.)
   - Golf → Addicted enough to start building my own simulator, [Open-Birdie](https://github.com/rroojrooj/Open-Birdie).
   - Also → Bouldering, Olympic weightlifting, scuba diving.
   - Music → Guitar and vocals. Queen, the Beatles, Bob Dylan, John Mayer, Eric Clapton, B.B. King, Oasis, Taylor Swift.
   - At home → A chocolate Labrador, a beagle and three Aldabra giant tortoises.
   - On my mind → Meaning, happiness and wealth, and how they fit together.
   - Reading → The bookshelf · Photos → Pictures I've taken
   - **Bristol Blockchain Society** (own block after Outside work): "I started it at university in
     2022 and ran it for two years." + a collage (1 big, 2 small), captioned "Bristol, 2022–2024".
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
   Class, 2025). Before Belfort: SCB 10X, Token Unlocks,
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

## Home page photo slots (layout G)

| Slot | Shape | Suggested subject |
|---|---|---|
| Wide photo under the intro | 3:2 landscape, full column width | One photo Rooj loves, captioned "Place, year" |
| Thumb beside Wim's Lab | square, ~92px | A gelato |
| Thumb beside Running | square | A marathon |
| Thumb beside At home | square | The tortoises |
| Bristol Blockchain Society | 1 big + 2 small (4:3) | Society events, the team, a talk |

Same rules as the Photos page: strip EXIF/GPS, resize. On phones the thumbs shrink to ~64px and
only their own rows narrow.

## Photos page plan

- Files at `photos/<year>/<slug>.jpg`. Resize to about 2000px on the long edge, plus a roughly 800px
  thumbnail. **Strip all EXIF, including GPS location.** Captions read "Place, Month Year". Newest
  year first; each image links to the full-size file. No JS lightbox.
- Adding a photo = drop in the file and add one `<figure>` line. Document the steps in the README. A
  small local helper script (resize + strip EXIF) is fine as long as the site itself stays build-free.

## Next steps

1. ~~Rooj picks a direction~~ (done: G). Rooj sends photos with place and year, including the
   Bristol Blockchain Society ones.
2. ~~Rebuild the pages with one stylesheet and self-hosted fonts; delete the workflow and old
   draft~~ (done 20 Oct 2026).
3. ~~Check it~~ (done; see "Where things stand"). Re-check after the photos go in.
3a. Swap the placeholders for Rooj's photos (README.md "Adding photos"), strip EXIF first.
4. Add GoatCounter once Rooj has the code.
5. ~~Merge to `master` and set Pages → `master` → `/docs`~~ (done 20 Oct 2026, fast-forward, at
   Rooj's request). After each later change: merge to `master`, check the live site. Ask before
   deleting the old `gh-pages` branch.

## Reference

- `design/research/academic-homepages.md` — Jon Barron, Sasha Rush, Shunyu Yao and others
- `design/research/minimal-tech-sites.md` — Gwern, Patrick Collison, Steph Ango and others
- `design/research/tech-stack.md` — why plain HTML, and how to deploy
