#!/usr/bin/env python3

from datetime import datetime, timedelta
from pathlib import Path
import unicodedata
import re

MONTHS = (
    "Janvier",
    "Février",
    "Mars",
    "Avril",
    "Mai",
    "Juin",
    "Juillet",
    "Août",
    "Septembre",
    "Octobre",
    "Novembre",
    "Décembre",
)

DAYS = (
    "Lundi",
    "Mardi",
    "Mercredi",
    "Jeudi",
    "Vendredi",
    "Samedi",
    "Dimanche",
)


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize("NFKD", input_str)
    only_ascii = nfkd_form.encode("ASCII", "ignore")
    return only_ascii.decode()


def create_month(month, year=2021):

    month_name = MONTHS[month - 1]
    month_lower = month_name.lower()
    month_norm = remove_accents(month_lower)

    solutions = set()
    solutions_md = Path(month_norm) / f"{month_norm}.md"
    if solutions_md.exists():
        for line in solutions_md.open():
            m = re.match(fr"^## (\d+) {month_name}$", line.strip())
            if m:
                solutions.add(int(m[1]))

    md = []
    md.append(f"### {month_name}")
    md.append("")
    md.append("|".join(["", *DAYS, ""]))
    md.append("|".join(["", *["---"] * 7, ""]))

    # date de début du month
    d = datetime(year, month, 1)

    # date de fin (1er du month suivant)
    fin = datetime(year + month // 12, (month % 12) + 1, 1)

    # petit retour en arrière pour bien placer le 1er dans le semainier
    d -= timedelta(days=d.weekday())

    has_solution = False

    while d < fin:

        cols = []

        for i in range(7):

            if d.month != month:
                # on n'est pas encore le 1er du month
                cols.append("  ")

            elif d.weekday() >= 5:
                # samedi dimanche
                cols.append(f"*{d.day}*")

            else:
                p = Path(month_norm) / f"{d.day:02d}.py"
                if p.exists():
                    cols.append(f"[{d.day}]({p}) ⚙️")
                    has_solution = True
                elif d.day in solutions:
                    cols.append(f"[{d.day}]({solutions_md}#{d.day}-{month_lower})")
                    has_solution = True
                else:
                    cols.append(f"{d.day:2d}")

            d += timedelta(days=1)

        md.append("| " + " | ".join(cols) + " |")

    return has_solution, "\n".join(md)


def main():
    year = 2021

    readme = Path("README.md").read_text()
    titre = f"## Solutions {year}\n\n"
    readme = readme[: readme.index(titre) + len(titre)]

    for month in range(1, 13):
        ok, md = create_month(month, year)
        if ok:

            readme += md
            readme += "\n"

    Path("README.md").write_text(readme)


if __name__ == "__main__":
    main()