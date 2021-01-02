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
    solutions_md = Path(month_norm) / f"README.md"
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

    done_month = 0
    total_month = 0

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
                total_month += 1

                p = Path(month_norm) / f"{d.day:02d}.py"

                if p.exists() and d.day in solutions:
                    cols.append(f"[{d.day:2d}]({solutions_md}#{d.day}-{month_lower}) [🎮]({p})")
                    done_month += 1

                elif p.exists():
                    cols.append(f"{d.day:2d} [🎮]({p})")
                    done_month += 1

                elif d.day in solutions:
                    cols.append(f"[{d.day:2d}]({solutions_md}#{d.day}-{month_lower})")
                    done_month += 1

                else:
                    cols.append(f"{d.day:2d}")

            d += timedelta(days=1)

        md.append("| " + " | ".join(cols) + " |")

    md[0] += f" ({done_month}/{total_month})"

    return (done_month, total_month), "\n".join(md)


def main():
    year = 2021

    readme = Path("README.md").read_text()
    titre = f"## Solutions {year}\n\n"
    readme = readme[: readme.index(titre) + len(titre)]

    total = 0
    done_total = 0
    for month in range(1, 13):
        (done_month, total_month), md = create_month(month, year)
        total += total_month
        if done_month != 0:
            done_total += done_month
            readme += md
            readme += "\n"
            if done_month == total_month:
                print(f"{MONTHS[month-1]:<10}: {done_month:3} / {total_month:3} fini")
            else:
                print(f"{MONTHS[month-1]:<10}: {done_month:3} / {total_month:3}")

    print(f"{'total':<10}: {done_total:3} / {total:3}")

    readme += f"\n### Avancement\n\nNombre de solutions: {done_total} / {total}\n\n"

    Path("README.md").write_text(readme)


if __name__ == "__main__":
    main()