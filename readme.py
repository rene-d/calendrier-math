#!/usr/bin/env python3

# à installer en hook de pre-commit
# ln -sf ../../readme.py .git/hooks/pre-commit

from datetime import datetime, timedelta
from pathlib import Path
import unicodedata
import re
import os
import hashlib
import argparse
from urllib.parse import quote, unquote

USE_BADGES = True
SHOW_SOLUTION = False
SHOW_SCREEN = True

CURRENT_YEAR = 2021

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


def render_latex_on(readme):
    def repl_render(m):
        latex = m[1]
        url = f"https://render.githubusercontent.com/render/math?math={quote(latex)}&mode=inline"
        return f"![latex]({url})"

    return re.sub(r"\$(.+?)\$", repl_render, readme)


def render_latex_off(readme):
    def repl_latex(m):
        url = m[1]
        return f"${unquote(url)}$"

    return re.sub(
        r"!\[latex\]\(https://render\.githubusercontent\.com/render/math\?math=(.+?)&mode=inline\)",
        repl_latex,
        readme,
    )


def inline_python_off(readme):

    # suppression du script
    readme = re.sub(
        r"(\[[\w\s]+\]\((\d\d\.py)\).+?\n)(\n```python\n[^`]*```\n)",
        r"\1",
        readme,
        re.DOTALL,
    )
    return readme


def inline_python_on(readme):

    readme = inline_python_off(readme)

    # ajout du script
    def repl(a):
        line, py = a.groups()
        script = Path(py).read_text().strip()
        return f"{line}\n```python\n{script}\n```\n"

    readme = re.sub(
        r"(\[[\w\s]+\]\((\d\d\.py)\).+?\n)",
        repl,
        readme,
        re.DOTALL,
    )

    return readme


def create_month(month, year):

    if year==CURRENT_YEAR:
        year_subdir=f"{year}/"
    else:
        year_subdir=""

    month_name = MONTHS[month - 1]
    month_lower = month_name.lower()
    month_norm = remove_accents(month_lower)

    solutions_link = dict()
    solutions_text = dict()
    solutions_md = Path(month_norm) / f"README.md"
    if solutions_md.exists():
        current_day = None
        for line in solutions_md.open():
            line = line.strip()
            m = re.match(fr"^## (\w+) (\d+) {month_name}$", line.strip())
            if m:
                current_day = int(m[2])
                solutions_link[
                    current_day
                ] = f"{year_subdir}{solutions_md}#{m[1].lower()}-{m[2]}-{month_lower}"

            m = re.match(f"^> réponse: (.*)$", line)
            if m and current_day:
                solutions_text[current_day] = m[1]
                current_day = None

    md = []
    md.append(f"### {month_name}")
    md.append("")
    md.append("|".join(["", *DAYS, ""]))
    md.append("|".join(["", *["---"] * 7, ""]))

    # date de début du mois
    d = datetime(year, month, 1)

    # date de fin (1er du montmoish suivant)
    fin = datetime(year + month // 12, (month % 12) + 1, 1)

    # petit retour en arrière pour bien placer le 1er dans le semainier
    d -= timedelta(days=d.weekday())

    done_month = 0
    total_month = 0

    while d < fin:

        cols = []

        for i in range(7):

            if d.month != month:
                # on n'est pas encore le 1er du mois
                cols.append("  ")

            elif d.weekday() >= 5:
                # samedi dimanche
                cols.append(f"*{d.day:02d}*")

            else:
                total_month += 1

                p = Path(month_norm) / f"{d.day:02d}.py"

                if p.exists() and d.day in solutions_text and SHOW_SCREEN:
                    cols.append(f"[{d.day:02d}]({solutions_link[d.day]}) [🖥]({p})")
                    done_month += 1

                elif d.day in solutions_text:
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


def patch_readme(repl_func):
    """ Modifie un README.md mensuel en appelant une fonction. """

    cwd = os.getcwd()

    for month in range(1, 13):

        month_name = MONTHS[month - 1]
        month_lower = month_name.lower()
        month_norm = remove_accents(month_lower)

        solutions_md = Path(month_norm) / f"README.md"
        if not solutions_md.exists():
            continue

        readme = solutions_md.read_text()
        hash = hashlib.md5(readme.encode()).hexdigest()

        os.chdir(solutions_md.parent)
        readme = repl_func(readme)
        os.chdir(cwd)

        os.getcwd()

        if hash == hashlib.md5(readme.encode()).hexdigest():
            continue

        solutions_md.write_text(readme)
        print(f"écrit {solutions_md}")

        if "GIT_INDEX_FILE" in os.environ:
            if Path(os.environ["GIT_INDEX_FILE"]).is_file():
                os.system(f"git add {solutions_md}")
                print(f"staged {solutions_md}")


def generate_calendar(root_dir, year):

    if year == CURRENT_YEAR:
        readme_md = root_dir / Path("README.md")
    else:
        readme_md = Path("README.md")

    readme = readme_md.read_text()
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

        readme_md.write_text(readme)

        if "GIT_INDEX_FILE" in os.environ:
            if Path(os.environ["GIT_INDEX_FILE"]).is_file():
                os.system("git add README.md")
                print("staged README.md")

    patch_readme(inline_python_on)
    patch_readme(render_latex_on)


def prepare_month_template(month, year):

    d = datetime(year, month, 1)

    md = []
    md.append(f"# Calendrier Mathématique {MONTHS[month-1]} {year}")
    md.append("")

    while d.month == month:
        if d.weekday() < 5:
            md.append(f"## {DAYS[d.weekday()]} {d.day} {MONTHS[month-1]}")
            md.append("")
        d += timedelta(days=1)

    return "\n".join(md)


def init_year(root_dir, year):
    for month in range(1, 13):

        month_name = MONTHS[month - 1]
        month_lower = month_name.lower()
        month_norm = remove_accents(month_lower)

        solutions_md = Path(month_norm) / f"README.md"
        if not solutions_md.exists():
            solutions_md.parent.mkdir(exist_ok=True, parents=True)
            solutions_md.write_text(prepare_month_template(month, year))
            print(f"créé: {solutions_md}")


def process_years(root_dir, year, func):
    """ Appelle la fonction sur l'année spécifiée ou sur toutes les années. """

    root_dir=Path(root_dir)

    def chdir(year):
        print(f"----- Année {year} -----")
        os.chdir(root_dir / f"{year}")

    if year:
        chdir(year)
        func(root_dir, year)
    else:

        year = CURRENT_YEAR
        while (root_dir / f"{year}").is_dir():
            chdir(year)
            func(root_dir, year)
            year -= 1


def main():
    if "GIT_INDEX_FILE" in os.environ:
        root_dir = Path(os.environ["GIT_INDEX_FILE"]).parent.parent
    else:
        root_dir = Path(__file__).parent.resolve()

    parse = argparse.ArgumentParser(
        description="Outil Calendrier Mathématique",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parse.add_argument("--root", default=root_dir, help="répertoire racine")
    parse.add_argument("-y", "--year", type=int, help="année")
    parse.add_argument("-m", "--month", type=int, help="prépare le README.md du mois")
    parse.add_argument("-i", "--init", action="store_true", help="initialise une année")
    parse.add_argument("-x", "--tex-on", action="store_true", help="TeX on")
    parse.add_argument("-X", "--tex-off", action="store_true", help="TeX off")
    parse.add_argument("-p", "--python-on", action="store_true", help="Python on")
    parse.add_argument("-P", "--python-off", action="store_true", help="Python off")
    args = parse.parse_args()

    if args.month:
        print(prepare_month_template(args.month, args.year))

    elif args.init:
        process_years(args.root, args.year, init_year)

    elif args.tex_on:
        process_years(args.root, args.year, lambda root_dir, year: patch_readme(render_latex_on))

    elif args.tex_off:
        process_years(args.root, args.year, lambda root_dir, year: patch_readme(render_latex_off))

    elif args.python_on:
        process_years(args.root, args.year, lambda root_dir, year: patch_readme(inline_python_on))

    elif args.python_off:
        process_years(
            args.root, args.year, lambda root_dir, year: patch_readme(inline_python_off)
        )

    else:
        process_years(args.root, args.year, generate_calendar)


if __name__ == "__main__":
    main()


# latex = input("LaTeX ? ")
# url =f"https://render.githubusercontent.com/render/math?math={quote(latex)}&mode=inline"
