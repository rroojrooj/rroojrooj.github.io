---
# gstack: design-md-format=spec
name: Rooj Rinchokechai
description: A quiet, text-first personal page set like a well-made paper, warmed by a few photos of life outside work.
colors:
  surface: "#FBF9F3"
  text: "#1C1B19"
  text-muted: "#6E6B64"
  rule: "#E5E1D6"
  link-underline: "#BDB8AC"
  photo-placeholder: "#ECE7DB"
  photo-placeholder-text: "#8F8A7F"
  surface-dark: "#161512"
  text-dark: "#E8E5DC"
  text-muted-dark: "#9A968C"
  rule-dark: "#2E2C27"
  link-underline-dark: "#5A574F"
  photo-placeholder-dark: "#24221E"
  photo-placeholder-text-dark: "#77736A"
typography:
  display:
    fontFamily: Source Serif 4
    fontWeight: 600
    fontSize: 34px
    lineHeight: 1.2
    letterSpacing: -0.01em
  display-phone:
    fontFamily: Source Serif 4
    fontWeight: 600
    fontSize: 30px
  heading:
    fontFamily: Source Serif 4
    fontWeight: 600
    fontSize: 20px
    lineHeight: 1.3
  intro:
    fontFamily: Source Serif 4
    fontSize: 20px
    lineHeight: 1.55
  body:
    fontFamily: Source Serif 4
    fontWeight: 400
    fontSize: 18px
    lineHeight: 1.6
  meta:
    fontFamily: Source Serif 4
    fontSize: 16px
  nav:
    fontFamily: Source Serif 4
    fontSize: 15px
  caption:
    fontFamily: Source Serif 4
    fontSize: 14px
    lineHeight: 1.4
rounded:
  none: 0px
spacing:
  2xs: 4px
  xs: 8px
  sm: 10px
  md: 18px
  lg: 26px
  section: 52px
  section-phone: 44px
  column: 640px
  column-wide: 1040px
  label-column: 112px
  label-column-phone: 88px
  gutter: 20px
components:
  link:
    textColor: "{colors.text}"
    underlineColor: "{colors.link-underline}"
    underlineThickness: 1px
    underlineOffset: 3px
  link-hover:
    underlineColor: "{colors.text}"
  nav-link:
    textColor: "{colors.text-muted}"
  nav-current:
    textColor: "{colors.text}"
  footer:
    textColor: "{colors.text-muted}"
    borderTopColor: "{colors.rule}"
  thumb:
    width: 92px
    widthPhone: 64px
    rounded: "{rounded.none}"
  photo-placeholder:
    backgroundColor: "{colors.photo-placeholder}"
    textColor: "{colors.photo-placeholder-text}"
    rounded: "{rounded.none}"
---

# Rooj Rinchokechai

## Overview

**Creative North Star:** a personal page that reads like a short, well-set academic paper, so the
person comes through in the words and a handful of photos rather than in decoration.
**Product context:** a personal site for a founder and engineer (Belfort, Wim's Lab) whose main job
is to show the side of Rooj that isn't on a CV. Readers are collaborators, founders and recruiters.
Plain HTML/CSS served from `docs/` by GitHub Pages.
**Mode per surface:** Home: Read. Photos: Experience. Bookshelf: Read. 404: Operate.
**Reference sites:** gwern.net (restraint, monochrome underlined links), patrickcollison.com (a few
facts, then curated pages), stephango.com (warm paper palette), jonbarron.info (structure). Research
is in `design/research/`.
**Key characteristics:**
- One narrow serif column; generous space instead of boxes and borders.
- Photos are informal and uneven (one wide, a few small floats, a loose collage), never a card grid.
- Links look like links everywhere: same colour as the text, thin underline.
- Dark mode is just the same page at night: the system decides, there is no switch.

## Colors

**Strategy:** Restrained. Near-black on warm off-white, one grey for metadata, no accent colour.
**Light or dark:** both, following the visitor's system setting; most visits are a quick read on a
phone, in whatever mode the phone is in.
Emphasis comes from weight (600 for names and headings) and from position, never from colour. The
underline colour is the only interaction signal; it darkens to the text colour on hover. The dark
palette keeps the same warmth and the same three-step hierarchy (text, muted, rule) rather than
inverting to pure black and white. Photo placeholders sit one step off the surface so they read as
"a photo goes here" without looking like a broken image.

## Typography

One family, Source Serif 4 (Adobe, SIL OFL), self-hosted as a single variable WOFF2 with weight and
optical-size axes, Latin subset. Optical sizing is on, so the name and the small captions each get
the cut drawn for their size. The serif is deliberate: it carries the academic, LaTeX-paper feel
the brief asked for. A cream-and-serif palette is on gstack's generic-default list; here it is an
explicit, approved choice (layout G), not a default. Georgia is the fallback. No italics are used,
so the italic file is not shipped. Only three heading sizes exist; everything else is body or
smaller.

## Layout

A single centred column. The Photos page widens so pictures have room; its intro and footer keep the
reading width. Below 520px the padding, the display size and the label column shrink, and the small
photos shrink with them. Sections are separated by space alone. "Outside work" is a two-column
definition list (label, line). Small photos float right inside the text they illustrate, so only
their own rows narrow on a phone. The Bristol Blockchain Society collage is one large photo beside
two stacked small ones: an intentional break from the column's regularity.

## Elevation & Depth

None. No shadows, no tints, no raised surfaces. The only line on the page is the footer's top rule.

## Shapes

Square corners everywhere, photos included. Nothing on the page is a pill, a card or a chip.

## Components

- **Links:** underlined at rest (not on hover only); hover darkens the underline; a visible
  focus-visible outline in the text colour.
- **Nav:** three plain words at the top of every page; the current page is the text colour and not a
  link; the others are muted links.
- **Dropdowns (`details`):** "Other projects" and "Background", closed by default, muted summary.
  The same pattern holds read-more detail inside an entry: Belfort's "Why I'm building it" sits
  under its one-line summary as a few short first-person paragraphs, indented on desktop and flush
  on phones.
- **Photos:** an `img` replaces each placeholder at the same aspect ratio. Captions read
  "Place, year" (home) or "Place, Month Year" (Photos page). EXIF, including GPS, is stripped first.
- **Footer:** one optional line of invitation, then "Last updated …".

## Do's and Don'ts

- Do keep every line earning its place: if a sentence can go, it goes.
- Do keep photos informal and varied in size; three to six on the home page at most.
- Do keep links underlined and the same colour as the text.
- Do let dark mode follow the system.
- Do keep the site plain HTML/CSS in `docs/`, with self-hosted fonts and no third-party requests.
- Don't add icons, pill buttons, cards, hover lifts, a hero section, numbered headings, animation,
  a sticky nav or a theme toggle.
- Don't add JavaScript, a build step or a framework.
- Don't use colour for emphasis or add an accent colour.
- Don't put CV material (job lists, dates, bootcamp stats) on the page; it lives on LinkedIn.
- Don't turn project entries into product pages: no feature lists or how-it-works. Write about the
  goal and the belief, in the first person, in short plain sentences that lead into each other.
  Never "my dream" or "the dream".

## Motion

- **Approach:** none. Nothing moves; the page loads and stays still.
- **Easing / duration:** not applicable.
- **The one authored moment:** the first photo landing under the intro.

## Decisions Log
| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-10-20 | Direction A (Paper): serif, warm off-white, monochrome underlined links, one column | Research on academic and minimal personal sites; Rooj's brief: minimal, academic, text-first |
| 2026-10-20 | Layout G (Mix 2): name and intro, one wide photo, small floated photos, Bristol Blockchain Society collage | Rooj liked B and C and wanted "no exactly fixed format"; G leads with identity and still shows a photo in the first screen |
| 2026-10-20 | No portrait of Rooj | Shown as variant D, not picked; earlier decision "no photo, for now" |
| 2026-10-20 | Self-host Source Serif 4 (opsz + wght, Latin, roman only) | No Google request; optical sizing matches the approved mockup; no italics used |
| 2026-10-20 | Publish `docs/` only | Keeps HANDOFF.md, CLAUDE.md and design material off the public website |
| 2026-10-20 | Belfort: a one-line belief plus a closed "Why I'm building it" dropdown (the work is slow, institutions have what individuals lack, so Belfort) | Built from Rooj's own words: investing can be easier, more efficient and more effective; individuals deserve institution-level intelligence at a lower price. Rejected along the way: feature rows ("not the product page"), a hard-to-read draft using "dream", and invented details |
