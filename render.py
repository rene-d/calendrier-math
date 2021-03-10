# https://github.com/rene-d/readme2tex

import hashlib
import os
import random
import re
import sys
import tempfile
import xml.etree.ElementTree as ET
from subprocess import check_output, DEVNULL
from xml.sax.saxutils import quoteattr
import logging
from pathlib import Path

envelope = r"""%% processed with readme2tex
\documentclass{article}
%s
\usepackage{geometry}
\pagestyle{empty}
\geometry{paperwidth=250mm, paperheight=16383pt, left=0pt, top=0pt, textwidth=426pt, marginparsep=20pt, marginparwidth=100pt, textheight=16263pt, footskip=40pt}
\begin{document}
%s%s
\end{document}
"""


def rendertex(engine, string, packages, temp_dir, block):
    if engine != "latex":
        raise Exception("Not Implemented")
    source = envelope % (
        "\n".join(r"\usepackage{%s}" % "".join(package) for package in packages),
        "a" if not block else "",
        string,
    )
    name = hashlib.md5(string.encode("utf-8")).hexdigest()
    source_file = os.path.join(temp_dir, name + ".tex")
    with open(source_file, "w") as file:
        file.write(source)

    try:
        check_output(
            [
                engine,
                "-shell-escape",
                "-output-directory=" + temp_dir,
                "-interaction=nonstopmode",
                "-halt-on-error",
                source_file,
            ],
            stderr=sys.stdout,
        )
    except:
        logging.warning("'%s' has warnings during compilation. See %s/%s", string, temp_dir, name)
    dvi = os.path.join(temp_dir, name + ".dvi")
    svg = check_output(["dvisvgm", "-v0", "-a", "-n", "-s", dvi])
    return svg, dvi, name


def svg2png(svg):
    pass


#     # assume that 'cairosvg' exists
#     import cairosvg

#     cairosvg.svg2png(url=svg, write_to=svg[:-4] + ".png", dpi=250)
#     return svg[:-4] + ".png"


def extract_equations(content):
    next = lambda n: (content.find("$", n), content.find(r"\begin", n))
    cursor = 0
    lines = [line for line in content.splitlines()]
    while True:
        dollar, begin = next(cursor)
        if dollar == -1:
            dollar = "-1"
        if begin == -1:
            begin = "-1"
        if dollar == "-1" and begin == "-1":
            break
        if dollar != "-1" and (begin == "-1" or dollar < begin):
            # found a $, see if it's $$
            if dollar > 0 and content[dollar - 1] == "\\":
                cursor = dollar + 1
                continue
            # get this line
            cummulative = 0
            line = 0
            for line, string in enumerate(lines):
                cummulative += len(string) + 1
                if dollar < cummulative:
                    break
            if lines[line].startswith("   "):
                cursor = dollar + 2
                continue
            if len(content) > dollar and content[dollar + 1] == "$":
                ## find the next $$
                cursor = content.find("$$", dollar + 2) + 2
                if cursor == 1:
                    cursor = dollar + 1
                    continue
                yield content[dollar:cursor], dollar, cursor, True
            else:
                cursor = content.find("$", dollar + 1) + 1
                if cursor == 0:
                    cursor = dollar + 1
                    continue
                yield content[dollar:cursor], dollar, cursor, False
        else:
            cummulative = 0
            line = 0
            for line, string in enumerate(lines):
                cummulative += len(string) + 1
                if begin < cummulative:
                    break
            if lines[line].startswith("   "):
                cursor = begin + 6
                continue
            leftover = content[begin + 6 :]
            if not leftover:
                break
            match = re.match(r"\{.+?\}", leftover)
            if not match:
                cursor = begin + 6
                continue
            end_marker = "\\end" + match.group()
            end = content.find(end_marker, begin)
            if end == -1:
                cursor = begin + 6
                continue
            cursor = end + len(end_marker)
            yield content[begin:cursor], begin, cursor, True


def render(
    readme,
    output="README_GH.md",
    engine="latex",
    packages=("amsmath", "amssymb"),
    svgdir="svgs",
    branch=None,
    user=None,
    project=None,
    nocdn=True,
    htmlize=False,
    use_valign=False,
    rerender=False,
    pngtrick=False,
    bustcache=False,
    non_interactive=False,
):
    if htmlize:
        nocdn = True
        branch = None
        try:
            import markdown
        except:
            logging.error("Cannot render markdown, make sure that the markdown package is installed.")
            return

    temp_dir = tempfile.mkdtemp("", "readme2tex-")
    content = Path(readme).read_text()
    equations = list(extract_equations(content))
    svgdir = Path(svgdir)
    output = Path(output)

    working_branch = None
    if not nocdn or branch:
        try:
            working_branch = check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode("utf-8").strip()

            # Make replacements
            if not user or not project:
                try:
                    # git remote get-url origin
                    giturl = check_output(["git", "remote", "-v"]).strip().decode("utf-8").splitlines()[0]
                    start = giturl.find(".com/") + 5
                    userproj = giturl[start:]
                    end = userproj.find(".git")
                    user, project = userproj[:end].split("/")
                except:
                    raise Exception("Please specify your github --username and --project.")
        except:
            logging.warn("Not in a git repository, please enable --nocdn")
            nocdn = True

    if nocdn:
        svg_url = svgdir / "{name}.svg"

        docdir = output.parent
        up_dir = Path()
        while True:
            try:
                svg_url = (up_dir / svgdir.relative_to(docdir)).as_posix()
                break
            except ValueError:
                if docdir == ".":
                    logging.fatal("Cannot find svgs relative path to svgdir")
                docdir = docdir.parent
                up_dir /= ".."
    else:
        svg_url = "https://cdn.jsdelivr.net/gh/{user}/{project}@{branch}/{svgdir}/{name}.svg"
    if pngtrick:
        svg_url = svg_url[:-4] + ".png"

    ##################################################################################################################
    #
    equation_map = {}
    seen = {}
    has_changes = False
    for equation, start, end, block in equations:
        name = hashlib.md5(equation.encode("utf-8")).hexdigest()

        # is the expression already in the document?
        if name in seen:
            logging.debug(f"duplicate: {equation} {start} {end} {block}")
            equation_map[(start, end)] = equation_map[seen[name]]
            continue

        seen[name] = (start, end)

        # Check if this already exists
        svg = None
        svg_path = svgdir / (name + ".svg")

        if not rerender:
            if branch and branch != working_branch:
                # use Git show if we use a dedicated branch
                try:
                    svg = check_output(["git", "show", f"{branch}:{svg_path}"], stderr=DEVNULL)
                except Exception:
                    logging.info(f"Cannot find {branch}:{svg_path}")
            else:
                # otherwise read from file
                if svg_path.is_file():
                    svg = svg_path.read_bytes()

            try:
                if svg:
                    xml = ET.fromstring(svg)
                    offset = float(xml.attrib["{https://github.com/leegao/readme2tex/}offset"])
                    short_equation = equation[:20].replace("\n", "␤")
                    logging.debug(f"cached {name} {short_equation} {offset} {start} {end}")
                    equation_map[(start, end)] = (svg, name, None, offset)
                    continue
            except Exception:
                logging.warning(f"cached SVG file for {svg_path} is corrupt, rerendering.")

        #############################################################################################################
        # LaTex rendering
        #
        short_equation = equation[:20].replace("\n", "␤")
        logging.debug(f"render: {short_equation} {name}")

        svg, dvi, name = rendertex(engine, equation, packages, temp_dir, block)

        xml = ET.fromstring(svg)
        attributes = xml.attrib
        gfill = xml.find("{http://www.w3.org/2000/svg}g")
        if not gfill:
            # the right namespace begins with http://
            gfill = xml.find("{https://www.w3.org/2000/svg}g")
        gfill.set("fill-opacity", "0.9")
        if not block:
            uses = gfill.findall("{http://www.w3.org/2000/svg}use")
            if not uses:
                uses = gfill.findall("{https://www.w3.org/2000/svg}use")
            use = uses[0]
            # compute baseline off of this dummy element
            x = use.attrib["x"]
            y = float(use.attrib["y"])
            viewBox = [float(a) for a in attributes["viewBox"].split()]  # min-x, min-y, width, height
            baseline_offset = viewBox[-1] - (y - viewBox[1])
            newViewBox = list(viewBox)
            newViewBox[0] = min(list(float(next.attrib["x"]) for next in uses if next.attrib["x"] != x) or [float(x)])
            newViewBox[-2] -= abs(newViewBox[0] - viewBox[0])
            gfill.remove(use)

            if use_valign:
                xml.set("viewBox", " ".join(map("{:.6f}".format, newViewBox)))
                xml.set("width", f"{newViewBox[-2]:.6f}pt")
            else:
                top = y - newViewBox[1]
                bottom = baseline_offset
                if top > bottom:
                    # extend the bottom
                    height = 2 * top
                    xml.set("height", f"{height:.6f}pt")
                    newViewBox[-1] = height
                    xml.set("viewBox", " ".join(map("{:.6f}".format, newViewBox)))
                else:
                    # extend the top
                    height = 2 * bottom
                    xml.set("height", f"{height:.6f}pt")
                    newViewBox[-1] = height
                    newViewBox[1] -= height - bottom - top
                    xml.set("viewBox", " ".join(map("{:.6f}".format, newViewBox)))
                    pass
        else:
            baseline_offset = 0

        xml.set("readme2tex:offset", f"{baseline_offset:.6f}")
        xml.set("xmlns:readme2tex", "https://github.com/leegao/readme2tex/")
        svg = ET.tostring(xml)

        has_changes = True
        equation_map[(start, end)] = (svg, name, dvi, baseline_offset)

    ##################################################################################################################
    # generate the markdown by replacing LaTeX by <img>
    #
    equations = sorted(equations, key=lambda x: (x[1], x[2]))[::-1]
    new = content
    for equation, start, end, block in equations:
        svg, name, dvi, off = equation_map[(start, end)]
        if abs(off) < 1e-2:
            off = 0
        xml = ET.fromstring(svg)
        attributes = xml.attrib

        scale = 1.65
        height = float(attributes["height"][:-2]) * scale
        width = float(attributes["width"][:-2]) * scale
        url = svg_url.format(user=user, project=project, branch=branch, svgdir=svgdir, name=name)
        tail = []
        if bustcache:
            tail.append("%x" % random.randint(0, 1e12))
        img = '<img alt=%s src="%s%s" %s width="%spt" height="%spt"/>' % (
            '"LaTeX"',  # quoteattr(equation),
            url,
            "?%s" % ("&".join(tail)) if tail else "",
            ('valign="%spx"' % (-off * scale) if use_valign else 'align="middle"'),
            width,
            height,
        )
        if block:
            img = '<p align="center">%s</p>' % img
        new = new[:start] + img + new[end:]

    md = None
    if branch and branch != working_branch:
        # if we use a dedicated branch, we use Git to get content
        try:
            md = check_output(["git", "show", f"{branch}:{output}"], stderr=DEVNULL).decode("utf-8")
        except Exception:
            logging.info(f"Cannot find {branch}:{output}")
    else:
        # otherwise read the file
        if output.is_file():
            md = output.read_text()
    if md != new:
        has_changes = True
    else:
        logging.debug(f"{output} up to date")

    ##################################################################################################################
    # something has changed ?
    #
    if has_changes or htmlize:
        stashed = None
        checkouted = False

        try:
            # we stash and change the branch if needed
            if branch and branch != working_branch:
                # is there something to stash ?
                if check_output(["git", "status", "--short"]).decode("utf-8").strip():
                    if not non_interactive and (
                        input(
                            "There are unstaged files, would you like to stash them? "
                            "(They will be automatically unstashed.) [Y/n]"
                        )
                        .lower()
                        .startswith("n")
                    ):
                        logging.error("Aborting.")
                        return

                    logging.info("Stashing...")
                    check_output(["git", "stash", "save", "--all", "rendertex"])
                    for line in check_output(["git", "stash", "list"]).decode().splitlines():
                        if line.endswith("rendertex"):
                            stashed = line.split(":")[0]
                            logging.debug(f"stash: {stashed}")

                # switch the branch
                logging.info(f"Checking out {branch}")
                check_output(["git", "checkout", "-B", branch])
                checkouted = True

            # write the svg files
            svgdir.mkdir(exist_ok=True, parents=True)
            for equation, start, end, _ in equations:
                svg, name, dvi, off = equation_map[(start, end)]
                if dvi:
                    (svgdir / f"{name}.svg").write_bytes(svg)
                    if pngtrick:
                        svg2png(svgdir / f"{name}.svg")

            # write the markdown
            output.parent.mkdir(exist_ok=True, parents=True)
            if not output.is_file() or output.read_text() != new:
                logging.debug(f"write {output}")
                output.write_text(new)
            if htmlize:
                (output + ".html").write_text(markdown.markdown(new))

            if checkouted:
                status = check_output(["git", "status", "-s"]).decode("utf-8").strip()
                if status:
                    logging.info(status)
                    logging.info("Committing changes...")
                    check_output(["git", "add", svgdir])
                    check_output(["git", "add", output])
                    if htmlize:
                        check_output(["git", "add", output + ".html"])
                    check_output(["git", "commit", "-m", "readme2latex render"])
                else:
                    logging.info("No changes were made.")

        except Exception as e:
            logging.error("%s", e)

            if checkouted:
                try:
                    logging.info("Cleaning up.")
                    check_output(["git", "clean", "-fdx"])
                    check_output(["git", "reset", "--hard"])
                except Exception as e_:
                    logging.fatal(
                        f"{e_}\n\nCould not cleanup branch {branch} or unstashing.\nMake sure that you cleanup manually."
                    )

        finally:
            try:
                if checkouted:
                    logging.info(f"Switching back to the original branch {working_branch}")
                    check_output(["git", "checkout", working_branch])

                if stashed:
                    logging.info(f"Unstashing {stashed}...")
                    check_output(["git", "stash", "pop", stashed])

            except Exception as e_:
                logging.fatal(
                    "{e_}\n\nCould not cleanup branch {branch} or unstashing.\nMake sure that you cleanup and revert manually.",
                    e_,
                )


logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)
# render(
#     "toto.md",
#     output="docs/2021/README.md",
#     svgdir="docs/svgs",
#     packages=("tikz", "amsmath", "amssymb"),
#     branch="gh_pages",
#     nocdn=True,
#     non_interactive=True,
# )
