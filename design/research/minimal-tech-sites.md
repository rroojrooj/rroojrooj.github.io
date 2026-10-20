# Research: minimal personal sites of engineers and founders

_Final report from a research agent, 20 October 2026. That environment's network blocked most personal domains, so most pages were read from their public GitHub source._

**Method note:** The sandbox blocked every personal domain. WebFetch got DNS failures and curl got a 403 from the proxy, so I couldn't load the live pages. What I did instead:
- **Read the actual source on GitHub** for Simon Willison, Gwern, Maggie Appleton and Flexoki (Steph Ango's palette). Design values for these are exact.
- **Used search results from each site** (bios and page structure) for Collison, Ango, Karpathy, Luu, Graham, Robinson and Coursey.
- **Filled in visual details from memory** where marked **(≈)**. A 2-minute browser check would confirm them.

I dropped four candidates:
- **Rauno:** an OS-style portfolio with a dock and sounds, not text-first.
- **Bret Victor:** the current homepage is an image collage.
- **Julia Evans and Paco:** too little could be verified.

## Sites

**1. Paul Graham — paulgraham.com (≈)**
- **Homepage:** a left column of image links (Essays, H&P, Books, YC, Arc, Bel, Lisp, Bio, RSS…), one picture and a one-line "new" note. The real homepage is /articles.html: one long list of titles, no dates or blurbs, with three "if you're not sure, start with…" picks at the top.
- **Intro:** none. There's a separate short Bio page.
- **Visual:** a table layout about 435px wide, small Verdana, nav text drawn as images, white background, no dark mode, not responsive.
- **Borrow:** the list of titles as the whole site, the "start here" picks, and "Thanks to … for reading drafts" lines.
- **Dated:** text as images, tiny type, no mobile layout. It works despite the design.

**2. Patrick Collison — patrickcollison.com** (page names confirmed; visuals ≈)
- **Homepage:** a few factual lines (Stripe, Arc Institute, grew up in Ireland, MIT), then links to one page per topic: Advice, Bookshelf, Fast, Questions, Labs, Progress, Culture, People, Dispatches.
- **Visual:** small, quiet type, lots of white space, no photo and almost no colour.
- **Borrow:** "a page per obsession":
  - /bookshelf: "I've only read about half"
  - /questions
  - /fast
  - /advice, split by age band. It even says "If you're 20–30: I don't know yet."
- **Weak:** small, low-contrast text, and few dates, so you can't tell how fresh pages are.

**3. Dan Luu — danluu.com (≈)**
- **Homepage:** a one-line header of links, then a newest-first list of titles. Nothing else.
- **Intro:** none on the homepage. /about is a long, candid career history.
- **Visual:** the browser's default serif, almost no CSS, no JavaScript.
- **Borrow:** instant loading, content only, a frank About page.
- **Doesn't work:** lines run the full window width. People publish user styles just to make it narrower.

**4. Gwern — gwern.net (source-verified)**
- **Homepage:** a one-line intro ("AI, psychology & statistics"), then dense multi-column lists: Newest, Popular, Notable, then topics.
- **Fonts:** Source Serif 4 for text, Source Sans 3 for interface bits, IBM Plex Mono for code.
- **Size and width:** 20px base (18px on mobile); line-height rises from 1.45 to 1.6 as screens widen; max-width 935px.
- **Colour and links:** black on white. Links are #333 with a 1px drawn underline that skips descenders. Hover is #888 and visited links are greyed to #666.
- **Headings and text:** a centred small-caps H1 and an uppercase H2 with a dotted rule. Text is justified and hyphenated on desktop.
- **Extras:** sidenotes on very wide screens, dark and reader modes, popups.
- **Borrow:**
  - Monochrome links marked by underline, not colour.
  - Per-page metadata: created/modified dates, status, confidence.
  - /me (about) and /design (colophon).
- **Too much for a newcomer:** heavy JavaScript, and the density needs a large body of writing.

**5. Simon Willison — simonwillison.net (source-verified)**
- **Homepage:** title, then About · Newsletter · TILs · Tools and a search box; a tab bar (Entries/Links/Quotes/Notes); a stream grouped by day; a "Highlights" sidebar; a footer with Disclosures, Colophon, year archives and a theme toggle.
- **Fonts:** Helvetica Neue for text, Georgia for headings.
- **Layout:** 940px overall, a 560px main column plus a 280px sidebar, stacking below 800px.
- **Colour and links:** black on #fdfdfd. Links are #0303bb with a 1px bottom border that turns dotted on hover; visited is #636.
- **Dark mode:** follows the system setting, plus an auto/light/dark toggle with a script that stops the page flashing.
- **Borrow:** TILs ("today I learned") and link posts as low-effort output, the Disclosures and Colophon pages, the three-way theme toggle.
- **Dated:** purple gradient bars and classic blog clutter.

**6. Steph Ango — stephango.com** (page names and palette verified; layout ≈)
- **Homepage:** his name and a plain list of short essays. Pages include About, Now, Projects, Topics and Subscribe.
- **About intro:** "I'm Steph. You may also know me as kepano, currently the CEO of Obsidian. Previously I co-founded Lumi and Inkodye." A colophon follows: written in Obsidian, built with Jekyll, hosted on Netlify.
- **Visual:** Flexoki, a palette he made for this site:
  - background #FFFCF0, text #100F0F
  - warm greys #6F6E69 and #B7B5AC
  - muted ink accents such as #205EA6 (blue) and #AF3029 (red)
  - light and dark modes; no photo or decoration
- **Borrow:** /now; /style ("Style is consistent constraint"); short essays revised over time; warm off-white instead of pure #fff.

**7. Maggie Appleton — maggieappleton.com (source-verified)**
- **Homepage:**
  - A hero: "Maggie makes visual essays about programming, design, and anthropology."
  - A subline: "Designer, anthropologist, and mediocre developer…"
  - A "Garden" explainer.
  - A three-column grid: Essays (cards), Notes (titles with growth icons), Patterns, and Library ("Books I've read and books I like the idea of having read").
- **Fonts:** Canela serif, Lato sans, IBM Plex Mono.
- **Size:** fluid 20–22px base; the H1 grows to about 82px.
- **Colour:** cream #f6f5f1 background, #353534 text, crimson links #5f023e with no underline.
- **Dark mode and motion:** a warm dark mode (#1c1b18); fade-in animations and hover scaling.
- **Borrow:** maturity labels on notes (seedling, budding, evergreen), which let a beginner publish unfinished thinking; the Library page.
- **Not minimal:** the cards, big hero and animation only work because she draws her own illustrations.

**8. Andrej Karpathy — karpathy.ai** (structure confirmed; visuals ≈)
- **Homepage:** a single page with a photo, a short bio, a timeline (Stanford PhD and CS231n, OpenAI, Tesla), teaching, and projects (micrograd, ConvNetJS). Side pages: books, favourite tweets, blog.
- **Visual:** hand-written HTML, a narrow centred column, plain styling.
- **Borrow:** the classic academic homepage, with the CV as a timeline.
- **Dated:** mixed thumbnail sizes look hand-rolled.

**Also worth a look:** Lee Robinson (leerob.com) uses flat one-word URLs, including a "Things I Believe" page at /beliefs. Paco Coursey (paco.me) splits his site into Writing and Craft (interaction experiments).

## Synthesis

**1. Content patterns, most common first**
1. A 1–3 sentence first-person intro: role, focus, where you are now.
2. A writing list: titles only, at most a year beside each.
3. An About page with a colophon.
4. Curated lists: bookshelf, questions, advice.
5. Projects, one line each.
6. A /now page.
7. Low-effort formats: TILs, notes labelled with their status.

For a new graduate: intro → 3–5 selected projects (include the dissertation) → writing, even if it's only two posts → one curated list (reading, or "questions I'm thinking about") → email, GitHub and a CV PDF. Add /now and a colophon as small extras. Skip anything that needs volume, such as category indexes, streams or a sidebar.

**2. What "minimal done well" has in common**
- **Line length:** 60–75 characters, or roughly a 36–42rem single column. Simon's main column is 560px.
- **Text:** 17–20px body, line-height 1.45–1.6, and only 2–3 heading sizes.
- **Fonts:** at most two. For an academic feel, a serif for text (Source Serif 4, Charter, Georgia) plus a mono or sans for metadata.
- **Colour:** near-black on off-white (#100F0F on #FFFCF0, or #353534 on #f6f5f1), greys for dates, and one accent for links or none at all (Gwern).
- **Links:** always underlined (thin, offset, skipping descenders), with a change of underline style on hover and a visible visited state.
- **Dark mode:** follow the system setting and use a warm dark (#1c1b18) rather than #000. A toggle is optional.
- **Spacing:** let space do the work instead of borders or boxes. At most one small photo.

**3. Signs a site came from a template**
- A full-screen "Hi, I'm X 👋" hero with typing animation and call-to-action buttons.
- Pill buttons, skill chips, logo walls, skill-percentage bars.
- Project card grids with thumbnails, shadows and lift on hover.
- Numbered headings like "01. About / 02. Experience", often with mono green-on-navy accents (the Brittany Chiang v4 clone look).
- Gradient text, blurred blobs, glassmorphism.
- Fade-ins on scroll, custom cursors, a sticky nav with a hamburger menu on a three-page site.
- Links shown by colour alone, low-contrast grey body text, tiny type (PG), unbounded line length (Luu).
- Big circular social icons, "Let's work together" sections, "Built with ❤️" footers.

**4. Top 3 references**
1. **gwern.net** for typography: serif text, monochrome, underlined links, small caps, page metadata, a colophon. Copy the restraint, not the JavaScript.
2. **patrickcollison.com** for content: a few factual lines, then curated pages that show curiosity without needing a big portfolio. This is ideal for a new graduate.
3. **stephango.com** for a modern calm: the warm paper palette, short essays, /now and a colophon. It shows minimal can feel warm rather than sterile.

Runner-up: karpathy.ai, for the CV-timeline academic homepage.

Sources:
- github.com/simonw/simonwillisonblog
- github.com/gwern/gwern.net
- github.com/MaggieAppleton/maggieappleton.com-V3
- github.com/kepano/flexoki
- swyx.io/css-100-bytes
- userstyles.world/style/13946
- Search results from: patrickcollison.com, stephango.com, karpathy.ai, leerob.com, paco.me, paulgraham.com, danluu.com, gwern.net/index
