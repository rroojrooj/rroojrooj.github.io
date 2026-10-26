#!/usr/bin/env python3
"""Write the GitHub contribution heatmap on docs/index.html.

Fetches the past year of contributions for one GitHub user and rewrites only the part of the home
page between the heatmap markers: a grid of plain <span> cells, one per day, which site.css draws
in ink tones (no green). It is a snapshot: run it again whenever you want it fresh:

    python3 tools/build_heatmap.py

It needs a token: GITHUB_TOKEN if set, otherwise the GitHub CLI's login (gh auth login).
"""
import html
import json
import os
import subprocess
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "docs" / "index.html"
USER = "rroojrooj"
START, END = "<!-- build_heatmap:start -->", "<!-- build_heatmap:end -->"

QUERY = """query($login: String!) { user(login: $login) { contributionsCollection { contributionCalendar {
  totalContributions weeks { contributionDays { date contributionCount contributionLevel } } } } } }"""
LEVELS = {"NONE": 0, "FIRST_QUARTILE": 1, "SECOND_QUARTILE": 2, "THIRD_QUARTILE": 3, "FOURTH_QUARTILE": 4}


def token():
    if os.environ.get("GITHUB_TOKEN"):
        return os.environ["GITHUB_TOKEN"]
    return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True).stdout.strip()


def fetch():
    body = json.dumps({"query": QUERY, "variables": {"login": USER}}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", data=body, headers={
        "Authorization": f"bearer {token()}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    if "errors" in data:
        raise SystemExit(f"GitHub said: {data['errors']}")
    return data["data"]["user"]["contributionsCollection"]["contributionCalendar"]


def render(cal):
    total = cal["totalContributions"]
    cells = []
    weeks = cal["weeks"]
    for i, week in enumerate(weeks):
        days = week["contributionDays"]
        # The first week can start mid-week: pad it so every column runs Sunday to Saturday.
        first = date.fromisoformat(days[0]["date"]).isoweekday() % 7
        cells += ['<span class="x"></span>'] * (first if i == 0 else 0)
        # Hover labels near either edge open inwards, so they never push past the page.
        edge = " l" if i < 8 else " r" if i >= len(weeks) - 8 else ""
        for d in days:
            n = d["contributionCount"]
            tip = f'{n or "No"} contribution{"" if n == 1 else "s"} · {date.fromisoformat(d["date"]):%-d %b %Y}'
            cells.append(f'<span class="c{LEVELS[d["contributionLevel"]]}{edge}" data-tip="{tip}"></span>')
    label = f"{total:,} contributions on GitHub in the past year"
    return (f'<figure class="heatmap">\n'
            f'<div class="cells" role="img" aria-label="{html.escape(label)}">{"".join(cells)}</div>\n'
            f'<figcaption>{total:,} contributions on <a href="https://github.com/{USER}">GitHub</a> '
            f'in the year to {date.today():%B %Y}</figcaption>\n'
            f'</figure>')


def main():
    page = PAGE.read_text()
    head, rest = page.split(START)
    _, tail = rest.split(END)
    PAGE.write_text(f"{head}{START}\n{render(fetch())}\n{END}{tail}")
    print("wrote the heatmap to docs/index.html")


if __name__ == "__main__":
    main()
