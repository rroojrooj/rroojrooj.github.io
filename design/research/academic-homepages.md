# Research: academic personal homepages

_Final report from a research agent, 20 October 2026. That environment's network blocked most personal domains, so most pages were read from their public GitHub source._

**How I got the pages:** this session's network proxy blocked direct fetches of every personal domain, and only GitHub was reachable. For each site below I read the actual published HTML, CSS and markdown from its public GitHub Pages repo, which is the same code that is served live. karpathy.ai, the current jasonwei.net, lucasb.eyer.be, neelnanda.io, yann.lecun.com and Tao's UCLA page are not on GitHub, so I couldn't read them and used other sites instead.

## Sites

**1. Jon Barron – jonbarron.info** (source github.com/jonbarron/jonbarron_website, updated Oct 2026)
- **Sections:** name → bio → link row (Email / CV / Bio / Scholar / Twitter / Github) with photo on the right → Research (a one-paragraph interests statement) → about 110 papers → Micropapers → Recorded Talks → Academic Service → Teaching → footer saying "feel free to steal this source".
- **Bio:** 4 sentences in the first person ("I'm a principal research scientist at Google DeepMind… where I lead a small team that mostly works on NeRF"). It covers his role, products he worked on, his PhD and advisor, and one award. A third-person bio sits in a separate .txt file for event organisers.
- **Papers:** 160px thumbnail (swaps to a before/after image on hover), bold title, all authors linked with his own name in bold, italic venue and year, "project page / arXiv" links, and a 1–2 sentence plain-English takeaway. 20 key papers are on pale-yellow (#ffffd0) rows.
- **Design:** one page, 800px max width, Lato at 14px. Links are #1772d0 with no underline and turn orange on hover. Circular photo in a column about 37% wide. No nav.
- **Verdict:** very easy to scan. Dated: built with tables and inline styles, and the 14px text is small. Ben Mildenhall (bmild.github.io) uses the template almost unchanged.

**2. Sasha Rush – rush-nlp.com** (harvardnlp/rush-nlp, Oct 2026)
- **Sections:** 200px photo, name, "ML Researcher. NYC.", [cv], email/github/twitter/youtube → one-paragraph bio → 17 "notable" papers → a personal photo. Nav: Main / Blog / Group / Projects / Publications; all 114 papers are on their own page.
- **Bio:** 4 sentences in the first person ("I'm an ML researcher, programmer, and blogger…"), covering past roles and things he helped start.
- **Papers:** 150px thumbnail, title, authors, venue. No buttons.
- **Design:** 800px (50rem) column, Helvetica Neue 16px/1.5, #222 text, #2a7ae2 links that underline on hover, thin grey rules, CSS variables. The tables collapse on mobile.
- **Verdict:** Barron's structure in modern code. Weak spot: papers without an image get auto-generated placeholder thumbnails.

**3. Shunyu Yao – ysymyth.github.io** (Feb 2025)
- **Sections:** photo (220px, floated right) → bio → Selected work (11) → Online talks → Recent readings → "(last updated: Feb 2025)". Social icons in the footer.
- **Bio:** "I am a researcher at OpenAI. I study agents." That is the whole bio. His older bio and News section are commented out in the source.
- **Work list:** text only. Bold title / authors / venue (e.g. Oral) / [paper | repo | tweet | project]. It includes products and his PhD thesis, not just papers.
- **Design:** Jekyll Now theme, Helvetica 18px, links #4183C4. The 1000px container is too wide.
- **Verdict:** confident and short. The reading list adds personality.

**4. Yang Song – yang-song.net** (al-folio template, Jul 2026)
- **Sections:** name, role subtitle, square photo, 3-paragraph bio, 13 selected papers, social icons. Nav cut down to about / publications / blog; he switched off the template's news, cv, projects and teaching pages.
- **Bio:** first person. Role; his main contribution in plain words, linked to an explainer blog post and a Quanta article; award; fellowships; advisor.
- **Papers:** venue badge, title, authors, award, [Abs] [PDF] [Code] buttons, and an abstract that expands.
- **Design:** 800px, Roboto / Roboto Slab, one accent colour (Caltech orange), dark-mode toggle.
- **Verdict:** a good example of stripping down a heavy template. al-folio looks generic if left unchanged.

**5. Jason Wei – jasonwei20.github.io** (old site, now redirects to jasonwei.net, which I couldn't read)
- **Sections:** one-line bio ("I am a research scientist at Google Brain. I live in Mountain View, California.") → Vitæ | Scholar | Twitter → "Papers (see all)".
- **Papers:** two-column table with the venue ("NeurIPS '22") in a narrow left column, then title link, authors with his name in bold, and press links.
- **Extras:** a blog, notes, and "Embrace Behind-Events", a public list of his rejections (papers, internships, PhD programmes) from his undergrad years.
- **Design:** links in navy #191970.

**6. Petar Veličković – petar-v.com** (Cambridge, UK; May 2026)
- **Sections:** several pages: Home / Researching / Communicating / Advising / Experience / Contact, plus a sidebar of 9 social links.
- **Bio:** one long first-person paragraph ("Hello, and welcome to my home on the web! I'm Petar…") listing roles, PhD, research and about 25 press outlets.
- **News:** the "Latest research/news" box's newest item is from 2022, and its "Upcoming" event shows "over 2 years ago".
- **Design:** Computer Modern Serif, navy (#1F2E43) header, 1220px wide. His headshot changes to a neural-network-filtered version on hover. Google Map and live clock widgets.
- **Verdict:** the LaTeX typeface looks academic, and he uses British spelling. Dated: stale news, gimmick widgets, overloaded bio.

**7. Chris Olah – colah.github.io** (last updated Dec 2023)
- **Sections:** the site is mainly a blog. Dark navbar (Blog / About / Contact) → "Recent Exciting Things!" → 47 posts shown as 250px cards with cover images, grouped by topic.
- **Bio:** on the About page only: "I work on reverse engineering artificial neural networks into human understandable algorithms", plus his roles.
- **Design:** Computer Modern serif at 18px, justified text, a full-screen grass photo behind a see-through panel, black links.
- **Verdict:** one image per piece and topic groups work well. Dated: Bootstrap 3, icon fonts, background photo.

**8. Lilian Weng – lilianweng.github.io** (Hugo PaperMod theme, Jul 2026)
- **Sections:** nav Posts / Archive / Search / Tags / FAQ with a dark-mode toggle. Home says "Hi, this is Lilian. I'm documenting my learning notes in this blog since 2017." plus icons, then a post list (title, excerpt, date, reading time).
- **Design:** 720px column, system sans-serif 16px/1.6, near-black text on white, auto dark mode.
- **Verdict:** the best reading typography of the set, but there is no bio or project list on the front page.

## Synthesis

**1. Sections, ranked by how many of the 8 sites have them**

Essential for someone early-career:
- **Name and one-line role (8/8).**
- **Link row (8/8):** email, CV PDF, GitHub, LinkedIn or X. Add Google Scholar only once there is something on it.
- **First-person bio of 2–4 sentences (7/8 have one on the homepage).**
- **Photo (6/8).**
- **Selected work (6/8):** call it "Projects" and include the dissertation or final-year project, internships and open-source work, each with [code | report | demo] links.

Optional:
- **Writing or blog (4/8):** only if they will keep posting.
- **Talks, teaching or service (3/8):** for example TA or lab-demonstrator work, or student societies.
- **News:** only Petar shows one, and Yao and Song turned theirs off. Skip it, or keep at most 5 dated items.
- **One personal touch:** e.g. a reading list or a personal photo.
- **A "last updated" line.**

**2. What makes these feel minimal and academic**
- **Layout:** one centred column, 720–800px max, on one page. Use separate pages only for a long list or a blog.
- **Fonts:** one family. Sans-serif (Lato, Helvetica, Roboto, system fonts) is most common; Computer Modern or another serif gives a LaTeX feel. Body text 16–18px, line-height 1.4–1.6.
- **Colours:** white background, #222 text, grey (#666–#828282) for metadata, and one link colour (#1772d0, #2a7ae2 or #4183C4, or a single brand accent).
- **Links:** no underline, change on hover. Inline link rows are separated by " / " or " | ".
- **Photo:** 150–220px next to the bio, round or slightly rounded.
- **Each entry:** bold title → authors (own name bold) → italic venue and year → links in brackets → optional one-line takeaway → optional thumbnail of about 150px on the left.
- **Headings and decoration:** plain h2 at about 22–26px in normal weight, thin rules, lots of white space. Automatic dark mode (following the system setting) is a modern extra.

**3. Mistakes to avoid**
- Stale news or "upcoming" events, as on Petar's site.
- Widgets: maps, clocks, hover filters, placeholder thumbnails.
- Background photos and icon-heavy Bootstrap navbars, which look like 2014 (Olah).
- Copying Barron's table markup and 14px text, or copying the live HTML with someone else's analytics still in it. Barron's footer warns against this.
- Bios that turn into a wall of text listing press coverage.
- Leaving template pages switched on when they are empty, such as Publications, Teaching or Repositories.
- Lines wider than about 800px (Yao is 1000px, Petar 1220px).
- A third-person bio on the page itself. None of these sites does it; offer a separate bio file like Barron's instead.

**4. Top 3 references for an early-career graduate**
1. **Sasha Rush:** Barron's layout in clean, responsive, modern code. His "notable" list maps straight onto 3–6 projects with thumbnails.
2. **Shunyu Yao:** shows that a two-sentence bio and a text-only list with [code | report | demo] links can still look authoritative. It needs no images and no papers.
3. **Jon Barron:** the standard content structure: bio, links and photo; an interests statement; entries with one-line takeaways; highlighting for key work. Copy the structure, not the code.

Runner-up: **Lilian Weng**, for typography, if they plan to write regularly.
