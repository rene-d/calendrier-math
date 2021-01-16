#!/usr/bin/env python3

# à installer en hook de pre-commit
# ln -sf ../../readme.py .git/hooks/pre-commit

from datetime import datetime, timedelta
from pathlib import Path
import unicodedata
import re
import os
import hashlib

USE_BADGES = True
SHOW_SOLUTION = False
SHOW_SCREEN = True

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

    solutions_link = dict()
    solutions_text = dict()
    solutions_md = Path(month_norm) / f"README.md"
    if solutions_md.exists():
        for line in solutions_md.open():
            line = line.strip()
            m = re.match(fr"^## (\d+) {month_name}$", line)
            if m:
                current_day = int(m[1])
                solutions_link[current_day] = f"{solutions_md}#{m[1]}-{month_lower}"
            else:
                m = re.match(fr"^## (\w+) (\d+) {month_name}$", line.strip())
                if m:
                    current_day = int(m[2])
                    solutions_link[
                        current_day
                    ] = f"{solutions_md}#{m[1].lower()}-{m[2]}-{month_lower}"

            m = re.match(f"^> réponse: (.*)$", line)
            if m:
                solutions_text[current_day] = m[1]

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
                cols.append(f"*{d.day:02d}*")

            else:
                total_month += 1

                p = Path(month_norm) / f"{d.day:02d}.py"

                if p.exists() and d.day in solutions_link and SHOW_SCREEN:
                    cols.append(f"[{d.day:02d}]({solutions_link[d.day]}) [🖥]({p})")
                    done_month += 1

                elif d.day in solutions_link:
                    cols.append(f"[{d.day:02d}]({solutions_link[d.day]})")
                    done_month += 1

                elif p.exists():
                    cols.append(f"{d.day:02d} [🖥]({p})")
                    done_month += 1

                else:
                    cols.append(f"{d.day:02d}")

                if SHOW_SOLUTION:
                    if d.day in solutions_text:
                        cols[-1] += "<br>" + solutions_text[d.day]

            d += timedelta(days=1)

        md.append("| " + " | ".join(cols) + " |")

    if USE_BADGES:
        if done_month == total_month:
            url = f"https://img.shields.io/static/v1?label=fini&message={done_month}/{total_month}&color=success"
        else:
            url = f"https://img.shields.io/static/v1?label=en%20cours&message={done_month}/{total_month}&color=informational"
        md.insert(1, f"[![{done_month}/{total_month}]({url})]({month_norm}/)")
        md.insert(1, "")

    else:
        md[
            0
        ] += f" ({done_month} {'réalisés' if done_month > 1 else 'réalisé'} parmi {total_month} défis)"

    md.append("")

    return (done_month, total_month), "\n".join(md)


def inline_python(month):

    month_name = MONTHS[month - 1]
    month_lower = month_name.lower()
    month_norm = remove_accents(month_lower)

    solutions_md = Path(month_norm) / f"README.md"
    if not solutions_md.exists():
        return

    readme = solutions_md.read_text()
    hash = hashlib.md5(readme.encode()).hexdigest()

    def repl(a):
        line, py, old = a.groups()
        script = (Path(month_norm) / py).read_text().strip()
        return f"{line}\n```python\n{script}\n```\n"

    new_readme = re.sub(
        r"(\[[\w\s]+\]\((\d\d\.py)\).+?\n)(\n```python\n.+?\n```\n)?",
        repl,
        readme,
        re.DOTALL,
    )

    if hash == hashlib.md5(new_readme.encode()).hexdigest():
        return

    solutions_md.write_text(new_readme)

    if "GIT_INDEX_FILE" in os.environ:
        if Path(os.environ["GIT_INDEX_FILE"]).is_file():
            os.system(f"git add {solutions_md}")
            print(f"staged {solutions_md}")


def main():
    year = 2021

    readme = Path("README.md").read_text()
    titre = f"## Solutions {year}\n\n"
    hash = hashlib.md5(readme.encode()).hexdigest()
    readme_begin = readme[: readme.index(titre) + len(titre)]

    readme = ""
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

    if USE_BADGES:
        progress = f"{done_total}/{total}%20%28{done_total/total*100:.0f}%25%29"
        readme_begin += f"![{done_total}/{total}](https://img.shields.io/static/v1?label=solutions&message={progress}&color=blueviolet)\n\n"
    else:
        readme_begin += (
            f"\n### Avancement\n\nNombre de solutions: {done_total} / {total}\n\n"
        )

    readme = readme_begin + readme

    if hash != hashlib.md5(readme.encode()).hexdigest():

        Path("README.md").write_text(readme)

        if "GIT_INDEX_FILE" in os.environ:
            if Path(os.environ["GIT_INDEX_FILE"]).is_file():
                os.system("git add README.md")
                print("staged README.md")

    for month in range(1, 13):
        inline_python(month)


if __name__ == "__main__":
    main()
