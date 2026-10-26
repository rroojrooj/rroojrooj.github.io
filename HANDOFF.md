# Handoff — personal site redesign

Last updated 20 October 2026, at the end of a Claude Code on the web session. This file is the source of
truth for picking the work back up.

## Where things stand

- **Branch `master`** (the only branch). The old al-folio theme is deleted. The first draft Rooj
  rejected (big hero, pill buttons, card grid, numbered headings) was replaced on 20 Oct 2026 by the
  **real site, built from layout G**, in **`docs/`**: `index.html`, `photos/index.html`,
  `bookshelf/index.html`, `404.html`, `assets/css/site.css`, self-hosted Source Serif 4 in
  `assets/fonts/` (OFL), and a monochrome favicon. No JavaScript except the home lead photo's
  random pick (26 Oct 2026), no workflow. Photos are
  placeholders until Rooj sends them, and empty photo slots are hidden by CSS on the live site
  (they appear as soon as a real `<img>` replaces the placeholder). Design tokens and rules are in
  `DESIGN.md`.
- **Live since 20 Oct 2026**: GitHub Pages serves `master` → `/docs`. Pushing to `master` publishes.
  Work on a branch and merge when ready.
  **Repo recreated 25 Oct 2026**: the GitHub repo was a fork of al-folio, so Rooj renamed it to
  `rroojrooj.github.io-old` and pushed `master` to a new, non-fork `rroojrooj.github.io` (Pages
  re-enabled on `master` → `/docs`). The new repo has no `gh-pages` or `redesign` branch; those exist
  only in the `-old` repo, which Rooj will delete himself. Checked at 390px and 1280px in light and dark: self-hosted font loads, no third-party requests,
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

## What Rooj wants

- Minimal and academic-leaning: text-first, generous spacing, nothing that looks like a template.
- **Show the side of him that isn't on his CV.** CV material is folded away or left to LinkedIn.
- Little text, and every line earns its place. Curate; don't include everything he sent.

## Decisions (made by Rooj)

| Topic | Decision |
|---|---|
| Name / place | Rooj Rinchokechai · Bangkok, Thailand |
| Links | workwithrooj [at] gmail.com · [LinkedIn](https://www.linkedin.com/in/roojrin) · [GitHub](https://github.com/rroojrooj). **No personal X.** Belfort's [@BelfortResearch](https://x.com/BelfortResearch) is fine. |
| Featured | Only **Belfort** and **Wim's Lab**. Every other project goes in a collapsed dropdown. |
| Pages | Home, **Photos** (pictures he's taken over the years; must be easy to add more), **Bookshelf** |
| Bookshelf | Titles and authors (authors added 25 Oct 2026), grouped by genre, all on one laptop screen. **No ratings, reviews, or read/reading status.** |
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

1. **Rooj Rinchokechai** / Bangkok, Thailand / workwithrooj [at] gmail.com · LinkedIn · GitHub
2. Intro: "I'm building Belfort, an AI analyst for individual investors, and making high-protein
   gelato at Wim's Lab. Away from work, I run marathons, play too much golf and look after three
   giant tortoises." Then the wide photo (layout G).
3. **Now**
   - **Belfort** · Founder · since September 2025 — since 26 Oct 2026 one story with no dropdown
     (see "Home page changes, 26 October 2026" below). It opens with Rooj's investing story, in his words: started at 17, no bank account so he bought
     through his mum's account, first book *Buffettology*, then *The Intelligent Investor*; those books
     shaped how he thinks about wealth, business and investing and changed his life; thanks to Warren
     Buffett and the investors behind those ideas. (Replaced the line "I believe investing can be far
     easier and more effective than it is today.") Links: [belfortagent.xyz](https://www.belfortagent.xyz) ·
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
   - **Bristol Blockchain Society** (own block after Outside work): one paragraph in Rooj's words
     (rewritten 26 Oct 2026): started in 2021 in his foundation year, with little support (people
     heard "crypto" and told him to focus on his studies); his belief that blockchain could make
     finance permissionless; from nothing to a weekly workshop (DEXs, Solidity, governance, money
     markets) then the pub on the society; speakers from established companies; proudest of how far
     it came and the warm community. + a collage (1 big, 2 small), captioned "Bristol, 2021–2024"
     (end year 2024 carried over from the old caption; not yet reconfirmed).
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

## Bookshelf (titles and authors, by genre)

The list lives in `docs/bookshelf/index.html`; that file is the source of truth. On 25 Oct 2026 Rooj
sent the rest of the list (the Goodreads paste had been cut off) and asked for authors and for the
whole shelf to fit on one screen. The genres now flow into columns, and three
genres were added: Self-help, Classics, Textbooks. Authors for "Ice Cream" (Goff & Hartel) and
"Introduction to Computer Security" (Goodrich & Tamassia) are best guesses; confirm with Rooj.
There are 50 books (an earlier count of 51 included the example line in the page's comment).

**Covers (26 Oct 2026, at Rooj's request).** Each book has a small 24×36 cover left of its title.
Hovering a cover, or tabbing to it, shows a 200px version beside it; clicking or tapping opens a
320px version alone on the page (a click, tap or Esc closes it). It is `<img popover>` plus CSS, no
JavaScript, and it is the one hover effect on the site (logged in DESIGN.md). Files are in
`docs/bookshelf/covers/`: `<slug>.jpg` (48×72) and `<slug>-large.jpg` (the scan's own size, at
most 480px wide), with metadata stripped. 1.7 MB in all, but the page itself only loads the 67 KB of
small covers; a large one loads when it is first shown. 49 come from Open Library (common English
editions, chosen by eye), and Blitzscaling's jacket comes from the publisher (Penguin Random House),
because Open Library only has its title page. `design/research/bookshelf-covers.md` lists every
edition. The two guessed textbooks use: Ice Cream, 7th edition (Goff & Hartel, Springer, 2013; the
scan is the 2015 paperback); and Introduction to Computer Security, 1st edition (Goodrich & Tamassia,
Addison-Wesley, 2011).
To fit the covers on one screen, the column gap went from 28px to 24px, which gives five columns at
1280px (four columns had run to 817px); Rooj chose this over squeezing four columns. A design pass
the same day, which Rooj asked for, then kept each genre whole in one column, so every column starts
with its label. The gap between genres went from 18px to 14px, and titles and authors now wrap
balanced. At 1280×800 the last book ends at 777px. It no longer fits a 768px-tall window. At
1024×700 the shelf is four columns and scrolls, as it did before (1009px, against 829px before
covers). Checked in Chromium only. Safari 26+ and Firefox 147+ support the anchor positioning used
for the side-by-side preview; older browsers show the preview in the middle of the window instead.

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
  thumbnail. **Strip all EXIF, including GPS location.** Captions read "Place, Year". Newest
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
    Done 25 Oct 2026: the home wide photo (Koh Panyee pitch, also the link-preview image) and 18
    film photos on the Photos page (2019, 2020, 2022, 2025), picked by Rooj from Rooj's own film scans.
    Years come from the lab scan dates; captions are "Place, Year".
    Also 26 Oct 2026: 41 phone photos from Rooj's Strava (and two Cape Town Marathon photos Rooj
    sent) went on the Photos page: a **Running** section first (`docs/photos/running/`), then new
    2026 and 2024 sections. Race captions read "Race, Year · time"; the time is Strava's elapsed
    time. Race list and times: Tokyo Marathon 2026 (with Rooj's cousin) 4:12:11 · Cape Town
    Marathon 2026 (with Rooj's dad) 4:18:43 · New York City 5K 2025 24:24 · Sydney 10K 2025 49:40 ·
    Great Bristol Run 10K 2025 55:30 · Bath Half 2025 1:53:13 · Bath Half 2024 2:18:22 (no photos).
    Place guesses still to confirm: the dive photos as "Maldives" (no GPS) and the May 2026 run as
    "Pilanesberg, South Africa" (Strava only gives Moses Kotane municipality). The four Dive
    Terminal photos keep their watermark (Rooj confirmed they may be shared with it).
    The home running thumb is the Clifton Suspension Bridge at night (Rooj's pick).
    Still to come: the gelato and tortoise thumbs and the Bristol Blockchain Society collage.
4. Add GoatCounter once Rooj has the code.
5. ~~Merge to `master` and set Pages → `master` → `/docs`~~ (done 20 Oct 2026, fast-forward, at
   Rooj's request). After each later change: merge to `master`, check the live site.
6. ~~Remove the "forked from al-folio" label~~ (done 25 Oct 2026 by recreating the repo). Rooj deletes
   `rroojrooj.github.io-old` when ready.

## Reference

- `design/research/academic-homepages.md` — Jon Barron, Sasha Rush, Shunyu Yao and others
- `design/research/minimal-tech-sites.md` — Gwern, Patrick Collison, Steph Ango and others
- `design/research/tech-stack.md` — why plain HTML, and how to deploy

## Home page changes, 26 October 2026

- Order is now: intro → lead photo → Now → Bristol Blockchain Society → Outside work → folded
  Other projects and Background → footer.
- The lead photo is picked at random on each visit from six Photos-page pictures (Koh Panyee, Phang
  Nga Bay 2022, Kanchanaburi 2020, Bangkok 2019, Copenhagen 2019, Hokkaido 2019) and links to Photos.
  Without JavaScript it stays Koh Panyee, which is also the link-preview image.
- Thumbs: Running is now the two Cape Town Marathon medals (Rooj's and his dad's) and links to
  `/photos/#running`; Wim's Lab is the Tokyo Marathon medal with a tub of Matcha Coconut. Both are
  184px crops of the Photos-page files, saved without EXIF. The Clifton bridge thumb is gone.
- Now section (later the same day): Belfort is one story with no dropdown, in three paragraphs: the
  investing story; why Belfort (the work is slow, institutions have what individuals lack); and the
  first months of learning ("a lot of how-tos": building a product from scratch, LLMs and AI
  infrastructure, developer tools and working efficiently, UI and UX, modular and generic system
  design, agentic systems, taste). Start months from Rooj: Wim's Lab July 2025, Belfort September 2025 (first said October; corrected from his CV).
  Each entry now has its name as a heading, the role and month on a muted line, and a rule between.
- Layout, later again: "scan first, read later". Order is now intro → lead photo → Now (one line per
  project; Belfort's line is "Giving individual investors the kind of support only funds have today,
  without the price tag." plus a "Why I'm building it" link down the page) → **Experience** (visible:
  Education, Work) → Outside work → **Why I'm building Belfort** (the three-paragraph story) → Bristol
  Blockchain Society → folded Other projects → footer. The Background dropdown is gone.
- Belfort story fixes from Rooj: at 17 he had no *brokerage* account of his own (not bank account);
  the learning paragraph was rewritten as a story (knew the problem, not yet how to build; the
  how-tos; taste; "almost a year of how-tos").
- Experience, from Rooj's CV (26 Oct 2026), curated on purpose (Rooj: "don't use every, it will be
  noisy"): one row per role, year in the label column, organisation in bold, one clause each.
  Kept: BMA 2024 (271 childcare centres, 45 districts; the childcare project left Other projects),
  TISCO then Kiatnakin Phatra 2022–2023 (value investing and DCF at KKP), Token Unlocks 2022–2023
  (SCB 10X venture to startup; the site later passed a million monthly visits), Bristol BEng
  2022–2025 First Class Honours. Left out: high school, foundation-year grade, percentages, DAOSURV's
  name, the Belfort CV blurb (product-page language). The Society paragraph gained the partners
  (Coinbase, Aave, Chainlink, dYdX Foundation) and the governance arm (Arbitrum delegate, $300k+
  delegated voting power at peak, £30,000+ raised for the society).
- Dates settled by Rooj: Belfort started **September 2025**. The Society was being formed from 2021
  (foundation year) and became official in **September 2022**; he was president until May 2024, then
  head of governance and advisor until May 2026. Caption stays "Bristol, 2021–2024".
  Gelato photos for the Wim's Lab thumb are still to come.

- Tightened 26 Oct 2026 at Rooj's request ("to the point, no filler"): the Belfort story (185 words)
  and the Society story (157 words, now three short paragraphs: the doubt, what it became, the
  pride). Rooj's rule for all copy here: don't be sloppy, don't be noisy, get to the point. The intro
  now also says he loves music and art.
- Later the same day: the Belfort story moved back under Belfort as a closed "Why I'm building it"
  dropdown (Rooj's request), with the summary in text colour and the opened story set off by a thin
  rule on its left. The separate "Why I'm building Belfort" section is gone.
- The lead photo now has ← → arrows at the right of its caption (Rooj's request) to step through
  the six photos; the next photo is preloaded. Hidden without JavaScript.
- Film photos now name the camera (Rooj, 26 Oct 2026): Contax T2 for colour, Olympus XA for black
  and white. On the Photos page it is a `camera` field per trip in `tools/photos.json`, shown as a
  muted line under the trip caption; trips shot on both read "Contax T2 · Olympus XA". Rooj: name
  the camera only, don't write "black and white". Only the 18 film-scan photos (trips tagged
  `film`) get a camera; phone photos get none.
  The home lead-photo captions add the camera too ("Koh Panyee, 2022 · Olympus XA").
- Experience dates now carry months (from Rooj's CV), set at 15px so a range wraps in two lines.
- GitHub heatmap under Now (26 Oct 2026): a **snapshot**, not live (Rooj asked for the simplest
  version; no GitHub Action). `python3 tools/build_heatmap.py` fetches the past year through the
  GitHub CLI login and rewrites the part of `docs/index.html` between the `build_heatmap` markers:
  plain <span> cells in ink tones of the text colour, caption "N contributions on GitHub in the year
  to <Month Year>". Run it again to refresh.
- Bristol Blockchain Society: the placeholder collage is replaced by one real photo, the pub after a
  workshop, captioned "Bristol Blockchain Society, Bristol, 2025" (28 Feb 2025, from Rooj's HEIC, resized to 1600px, EXIF stripped). More society photos can
  bring the collage back.
- Heatmap, later: stronger ink steps (empty days in the rule colour, then 30%, 55%, 78% and 100% of
  the text colour, mixed with color-mix so hover labels stay solid) and a hover label on every day
  ("22 contributions · 14 May 2026"), pure CSS from each cell's data-tip. Labels near either edge
  open inwards. No accent colour, per DESIGN.md; Rooj asked whether the palette felt dull.
- Wim's Lab photos (26 Oct 2026, from Rooj): three flavour shots (matcha and coconut, chocolate with
  brownie, a cookie flavour with brownie and yellow cubes) cropped square around the cup, without
  the "wim's lab ice cream" header, at 360px in `docs/assets/home/wims-*.jpg`. They sit in a row of
  three under the Wim's Lab line. The Tokyo-medal gelato thumb is gone. Flavour names other than
  matcha and chocolate are unconfirmed, so the alt text describes what is visible.
- Heatmap is now Bristol red (Rooj's choice over terracotta and sepia): `--heat-0..4` tokens in
  site.css, light #EFECE4 → #F0D2D4 → #DE949A → #C4505B → #AB1F2D; dark #201F1B → #3F1A1E →
  #6E2530 → #AB1F2D → #E0626E. Empty days are a near-page tint so they no longer look like activity.
- The three gelato photos are recropped from the logo on each cup, so every cup is the same size and
  height and centred: matcha, chocolate, cookies (light, dark, light).
- Heatmap axis: month names over the week each month starts, with the year (2025, 2026) on a line
  above them, written by tools/build_heatmap.py. (The class is `yr`, not `year`: the Photos page
  hides any `.year` without an image.)
- Other projects is no longer folded (Rooj, 26 Oct 2026): a visible section at the bottom, above the
  footer, in the same year/name/one-line rows as Experience, set at 16px so it reads as a footnote.
- Experience, later (Rooj): full company names, a little more detail per role from the CV, work
  sorted newest first by real dates (BMA, Kiatnakin Phatra Financial Group, Token Unlocks, TISCO
  Financial Group), Education on its own under a small muted label (Bristol, Sep 2021 – May 2025,
  after a foundation year). The "More on LinkedIn" line is gone; LinkedIn is in the header.
- Education adds Patumwan Demonstration School, 2014 – 2021 (CV says Jan 2014 – Jan 2021; shown as years).
- Experience order is now Education first, then Work (Rooj). Each group has its own 18px heading,
  like the project names under Now, with a thin rule between the groups.
- Email is shown as plain text "workwithrooj [at] gmail.com" with no mailto link (Rooj, against spam bots); the notes and mockups mask it the same way.
