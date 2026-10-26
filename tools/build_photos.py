#!/usr/bin/env python3
"""Write the gallery part of docs/photos/index.html from tools/photos.json.

A local helper, not a build step: the site stays plain HTML, and this script only rewrites the
section between the build markers. Run it after editing tools/photos.json:

    python3 tools/build_photos.py

Layout: trips (newest first) are packed into full-width rows ("bands") where every photo shares
one height. A trip too wide for one band continues on bands of its own, and its caption sits
under its last band. The packing is redone for every filter (All, Running, ...), and CSS shows
the view that matches the link in the address bar, so filtering needs no JavaScript.
"""
import html
import json
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PHOTOS = ROOT / "docs" / "photos"
PAGE = PHOTOS / "index.html"
DATA = ROOT / "tools" / "photos.json"
START, END = "<!-- build_photos:start -->", "<!-- build_photos:end -->"

WIDTH = 1400        # gallery width at a 1440px window; bands scale with the window
TARGET = 400        # photo height the packing aims for at that width
PHOTO_GAP, TRIP_GAP = 6, 24   # must match .photos and .band gaps in site.css
MAX_PER_BAND = 7


def jpeg_size(path):
    """Width and height of a JPEG, read from its header (no image library needed)."""
    with open(path, "rb") as f:
        data = f.read()
    i = 2
    while i < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        length = struct.unpack(">H", data[i + 2:i + 4])[0]
        if marker in (0xC0, 0xC1, 0xC2):
            h, w = struct.unpack(">HH", data[i + 5:i + 9])
            return w, h
        i += 2 + length
    raise ValueError(f"no size in {path}")


def load():
    data = json.loads(DATA.read_text())
    for trip in data["trips"]:
        for p in trip["photos"]:
            p["w"], p["h"] = jpeg_size(PHOTOS / f"{p['src']}-800.jpg")
            p["ar"] = p["w"] / p["h"]
    return data


def band_height(items):
    """Photo height if these (trip index, photo) items fill one band."""
    trips = len({t for t, _ in items})
    gaps = TRIP_GAP * (trips - 1) + PHOTO_GAP * (len(items) - trips)
    return (WIDTH - gaps) / sum(p["ar"] for _, p in items)


def pack(trips):
    """Split the photos into bands near TARGET height, keeping trips in order."""
    items = [(t, p) for t, trip in enumerate(trips) for p in trip["photos"]]
    n = len(items)
    best, cut = [0.0] + [float("inf")] * n, [0] * (n + 1)
    for j in range(1, n + 1):
        for i in range(max(0, j - MAX_PER_BAND), j):
            chunk = items[i:j]
            h = band_height(chunk)
            cost = ((h - TARGET) / 40) ** 2
            if h > 640 or h < 230:
                cost += 400 + ((h - TARGET) / 20) ** 2
            starts_mid = i > 0 and items[i - 1][0] == items[i][0]
            ends_mid = j < n and items[j - 1][0] == items[j][0]
            if starts_mid:
                cost += 4
            # A trip that spills over a band never shares that band with another trip.
            if (starts_mid or ends_mid) and len({t for t, _ in chunk}) > 1:
                cost += 2000
            if best[i] + cost < best[j]:
                best[j], cut[j] = best[i] + cost, i
    bands, j = [], n
    while j > 0:
        bands.append(items[cut[j]:j])
        j = cut[j]
    return bands[::-1]


def caption(trip):
    meta = trip["year"] + (f" · {trip['time']}" if trip.get("time") else "")
    out = f'{html.escape(trip["name"])} <span class="meta">{html.escape(meta)}</span>'
    if trip.get("parts"):
        out += f'<span class="parts">{html.escape(trip["parts"])}</span>'
    if trip.get("note"):
        out += f'<span class="note">{html.escape(trip["note"])}</span>'
    return f"<figcaption>{out}</figcaption>"


def photo(p):
    return (f'<a style="--ar: {p["ar"]:.4f}" href="{p["src"]}.jpg"><img src="{p["src"]}-800.jpg" '
            f'alt="{html.escape(p["alt"])}" width="{p["w"]}" height="{p["h"]}" loading="lazy"></a>')


def render_view(view_id, trips):
    bands = pack(trips)
    groups_per_band = []
    for band in bands:
        groups = []
        for t, p in band:
            if groups and groups[-1][0] == t:
                groups[-1][1].append(p)
            else:
                groups.append((t, [p]))
        groups_per_band.append(groups)
    first_band, last_band = {}, {}
    for b, groups in enumerate(groups_per_band):
        for t, _ in groups:
            first_band.setdefault(t, b)
            last_band[t] = b
    # The caption goes under a trip's last band, unless the trip starts inside a band it shares
    # with other trips: then it goes right under that first part, so no photo looks unlabelled.
    caption_band = {t: (first_band[t] if len(groups_per_band[first_band[t]]) > 1 else last_band[t])
                    for t in first_band}
    out = []
    for b, groups in enumerate(groups_per_band):
        # A band that only continues the trip filling the band above sits tight against it.
        prev = groups_per_band[b - 1] if b else []
        cont = " cont" if prev and len(prev) == 1 and prev[0][0] == groups[0][0] else ""
        parts = []
        for t, ps in groups:
            total = sum(p["ar"] for p in ps)
            gaps = PHOTO_GAP * (len(ps) - 1)
            cap = "\n" + caption(trips[t]) if caption_band[t] == b else ""
            parts.append(f'<figure class="group" style="--sum: {total:.4f}; --gaps: {gaps}px">\n'
                         f'<div class="photos">\n' + "\n".join(photo(p) for p in ps) + f"\n</div>{cap}\n</figure>")
        out.append(f'<div class="band{cont}">\n' + "\n".join(parts) + "\n</div>")
    return f'<div class="view" data-view="{view_id}">\n' + "\n\n".join(out) + "\n</div>"


def main():
    data = load()
    filters, trips = data["filters"], data["trips"]
    targets = "".join(f'<span class="filter-target" id="{f["id"]}"></span>' for f in filters)
    links = "".join(f'<a href="#{f["id"]}">{html.escape(f["label"])}</a>' for f in filters)
    views = [render_view("all", trips)]
    for f in filters:
        if f["id"] != "all":
            views.append(render_view(f["id"], [t for t in trips if f["id"] in t["tags"]]))
    block = (f"{START}\n{targets}\n"
             f'<nav aria-label="Site"><a href="../">Home</a><span aria-current="page">Photos</span><a href="../bookshelf/">Bookshelf</a></nav>\n\n'
             f'<header class="page-intro">\n<h1>Photos</h1>\n<nav class="filters" aria-label="Show">{links}</nav>\n</header>\n\n'
             + "\n\n".join(views) + f"\n{END}")
    page = PAGE.read_text()
    a, b = page.index(START), page.index(END) + len(END)
    PAGE.write_text(page[:a] + block + page[b:])
    count = sum(len(t["photos"]) for t in trips)
    print(f"wrote {len(trips)} trips, {count} photos, {len(views)} views to {PAGE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
