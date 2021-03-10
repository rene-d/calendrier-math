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
import subprocess

from render import render  # readme2tex


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


def stage(filename):
    if "GIT_INDEX_FILE" not in os.environ:
        return
    branch_name = (
        subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])
        .decode()
        .strip()
    )
    if branch_name == "main":
        subprocess.run(["git", "add", filename])
        print(f"staged {filename}")


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize("NFKD", input_str)
    only_ascii = nfkd_form.encode("ASCII", "ignore")
    return only_ascii.decode()


def render_latex_on(readme):
    def repl_render_ml(m):
        latex = m[1].strip()
        url = f"https://render.githubusercontent.com/render/math?math={quote(latex)}"
        return f"![latexml]({url})"

    readme = re.sub(r"(?s)\$\$(.+?)\$\$", repl_render_ml, readme)  # (?s) = flag DOTALL

    def repl_render(m):
        latex = m[1]
        url = f"https://render.githubusercontent.com/render/math?math={quote(latex)}&mode=inline"
        return f"![latex]({url})"

    readme = re.sub(r"\$(.+?)\$", repl_render, readme)

    return readme


def render_latex_off(readme):
    def repl_latex_ml(m):
        url = m[1]
        return f"$$\n{unquote(url)}\n$$"

    def repl_latex(m):
        url = m[1]
        return f"${unquote(url)}$"

    readme = re.sub(
        r"!\[latexml\]\(https://render\.githubusercontent\.com/render/math\?math=(.+?)\)",
        repl_latex_ml,
        readme,
    )
    readme = re.sub(
        r"!\[latex\]\(https://render\.githubusercontent\.com/render/math\?math=(.+?)&mode=inline\)",
        repl_latex,
        readme,
    )

    return readme


def inline_python_off(readme):

    # suppression du script
    readme = re.sub(
        r"(\[[\w\s]+\]\(([\d\w]+\.py)\).+?\n)(\n```python\n[^`]+```\n)",
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
        try:
            script = Path(py).read_text().strip()
        except FileNotFoundError:
            print("fichier manquant:", Path(py).absolute())
            exit(2)
        return f"{line}\n```python\n{script}\n```\n"

    readme = re.sub(
        r"(\[[\w\d\s]+\]\((\d\d\.py)\).+?\n)",
        repl,
        readme,
        re.DOTALL,
    )

    return readme


def create_month(month, year):

    if year == CURRENT_YEAR:
        year_subdir = f"{year}/"
    else:
        year_subdir = ""

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
                    cols.append(f"[{d.day:02d}]({solutions_link[d.day]}) 🖥")
                    done_month += 1

                elif d.day in solutions_text:
                    cols.append(f"[{d.day:02d}]({solutions_link[d.day]})")
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
            url = f"https://img.shields.io/static/v1?label=fini&message={done_month}/{total_month}&color=success&style=flat-square"
        else:
            url = f"https://img.shields.io/static/v1?label=en%20cours&message={done_month}/{total_month}&color=informational&style=flat-square"
        md.insert(
            1,
            f"[![{done_month}/{total_month}]({url})]({year_subdir}{month_norm}/)",  # jekyll n'enlève pas README.md :/
        )
        md.insert(1, "")

    else:
        md[
            0
        ] += f" ({done_month} {'réalisés' if done_month > 1 else 'réalisé'} parmi {total_month} défis)"

    md.append("")

    return (done_month, total_month), "\n".join(md)


def readme2tex():
    """ Modifie un README.md mensuel en appelant une fonction. """

    cwd = os.getcwd()

    for month in range(1, 13):

        month_name = MONTHS[month - 1]
        month_lower = month_name.lower()
        month_norm = remove_accents(month_lower)

        solutions_md = Path(month_norm) / "INPUT.md"
        if not solutions_md.exists():
            continue

        print(f"render {solutions_md}")
        # cwd = os.getcwd()
        # os.chdir(Path(month_norm))
        render(
            solutions_md,
            solutions_md.parent / "README.md",
            svgdir=solutions_md.parent / "svgs",
            packages=("amsmath", "amssymb", "amsthm", "tikz"),
            nocdn=True,
            use_valign=True,
        )
        # os.chdir(cwd)


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

        stage(solutions_md)


def make_full_year(year):
    """  """

    cwd = os.getcwd()

    readme_year = "# Calendrier Mathématique {year}\n"

    for month in range(1, 13):

        month_name = MONTHS[month - 1]
        month_lower = month_name.lower()
        month_norm = remove_accents(month_lower)

        solutions_md = Path(month_norm) / f"README.md"
        if not solutions_md.exists():
            continue

        readme = solutions_md.read_text()
        readme = re.sub(r"^# Calendrier Mathématique", r"##", readme, re.DOTALL)
        readme = re.sub(r"\n(\[Solutions 20.*README.md\)\n)", r"", readme, re.DOTALL)
        readme = re.sub(r"\n(#+ )", r"\n#\1", readme, re.DOTALL)

        readme_year += "\n" + readme
        # print(readme)
        # exit()

    return readme_year


def generate_calendar(root_dir, year):

    # prépare les README.md mensuels
    patch_readme(inline_python_on)
    patch_readme(render_latex_on)
    readme2tex()

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
        readme_begin += f"![{done_total}/{total}](https://img.shields.io/static/v1?label=solutions&message={progress}&color=blueviolet&style=flat-square)\n\n"
    else:
        readme_begin += (
            f"\n### Avancement\n\nNombre de solutions: {done_total} / {total}\n\n"
        )

    readme = readme_begin + readme

    # le calendrier a été modifié: on l'enregistre
    if hash != hashlib.md5(readme.encode()).hexdigest():
        readme_md.write_text(readme)
        # si on est appelé comme hook Git, on stage le fichier
        stage("README.md")

    # (root_dir / f"{year}.md").write_text(make_full_year(year))


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

    root_dir = Path(root_dir)

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
        root_dir = Path.cwd()
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
    parse.add_argument("-f", "--file", help="Fichier à traiter")
    args = parse.parse_args()

    if args.file:

        content = Path(args.file).read_text()
        patched = content

        if args.tex_on:
            patched = render_latex_on(patched)
        elif args.tex_off:
            patched = render_latex_off(patched)

        if args.python_on:
            patched = inline_python_on(patched)
        elif args.python_off:
            patched = inline_python_off(patched)

        if patched != content:
            Path(args.file).rename(Path(args.file + ".bak"))
            Path(args.file).write_text(patched)
            print(f"écriture de {Path(args.file)}")

    elif args.month:
        print(prepare_month_template(args.month, args.year))

    elif args.init:
        process_years(args.root, args.year, init_year)

    else:

        if args.tex_on:
            process_years(
                args.root,
                args.year,
                lambda root_dir, year: patch_readme(render_latex_on),
            )
        elif args.tex_off:
            process_years(
                args.root,
                args.year,
                lambda root_dir, year: patch_readme(render_latex_off),
            )

        if args.python_on:
            process_years(
                args.root,
                args.year,
                lambda root_dir, year: patch_readme(inline_python_on),
            )
        elif args.python_off:
            process_years(
                args.root,
                args.year,
                lambda root_dir, year: patch_readme(inline_python_off),
            )

        if (
            not args.tex_on
            and not args.tex_off
            and not args.python_on
            and not args.python_off
        ):
            process_years(args.root, args.year, generate_calendar)


if __name__ == "__main__":
    main()


# latex = input("LaTeX ? ")
# url =f"https://render.githubusercontent.com/render/math?math={quote(latex)}&mode=inline"
