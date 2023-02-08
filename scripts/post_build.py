# *****************************************************************************
#
#   Part of the py5 project
#   Copyright (C) 2020-2021 Jim Schmitz
#
#   This project is free software: you can redistribute it and/or modify it
#   under the terms of the GNU General Public License as published by the
#   Free Software Foundation, either version 3 of the License, or (at your
#   option) any later version.
#
#   This project is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
#   Public License for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program. If not, see <https://www.gnu.org/licenses/>.
#
# *****************************************************************************
import os
import re
from pathlib import Path
import shutil


BUILD_DIR = Path("_build/html/")

IMG_REGEX = re.compile(r'<img src=\"(images/[^\"]*)\"[^>]*>')
GITHUB_EDIT_LINK_REGEX = re.compile(
    r"https://github.com/py5coding/py5book/edit/main/reference/([^\.]*)\.rst"
)

GROUP_CASE_PAIRS = [
    ("sketch", "Sketch"),
    ("py5graphics", "Py5Graphics"),
    ("py5image", "Py5Image"),
    ("py5shape", "Py5Shape"),
    ("py5shader", "Py5Shader"),
    ("py5font", "Py5Font"),
    ("py5tools", "Py5Tools"),
    ("py5functions", "Py5Functions"),
    ("py5magics", "Py5Magics"),
]


###############################################################################
# MODIFY REFERENCE GITHUB LINKS
###############################################################################

for doc in BUILD_DIR.glob("**/*.html"):
    with open(doc, "r") as f:
        html = f.read()

    # fix edit page link to point to actual documentation source file in py5generator
    m = GITHUB_EDIT_LINK_REGEX.search(html)
    if m is not None:
        original_link = m.group(0)
        stem = m.group(1)

        # repair class or group name
        for lowercase, py5case in GROUP_CASE_PAIRS:
            if stem.startswith(lowercase):
                stem = stem.replace(lowercase, py5case)
                break

        new_link = f'https://github.com/py5coding/py5generator/edit/main/py5_docs/Reference/api_en/{stem}.txt'
        html = html.replace(original_link, new_link)

    # fix new issue link to point to py5generator repo
    html = html.replace('https://github.com/py5coding/py5book/issues/new?', 'https://github.com/py5coding/py5generator/issues/new?')

    with open(doc, "w") as f:
        f.write(html)

###############################################################################
# COPY EXTRA FILES
###############################################################################

if (BUILD_DIR / "files").exists():
    shutil.rmtree(BUILD_DIR / "files")
shutil.copytree("files", BUILD_DIR / "files")

shutil.copytree("tutorials/images", BUILD_DIR / "tutorials/images")

###############################################################################
# FIX 404.HTML PAGE
###############################################################################

with open(BUILD_DIR / "404.html") as f:
    html = f.read()

html = re.sub(r'(href|src)="([^"]*)"', r'\1="/\2"', html)

with open(BUILD_DIR / "404.html", 'w') as f:
    f.write(html)

###############################################################################
# COPY SUMMARY PAGE TO INDEX.HTML
###############################################################################

shutil.copy(BUILD_DIR / "reference/summary.html", BUILD_DIR / "reference/index.html")

###############################################################################
# REMOVE JUNK FILES
###############################################################################

os.remove(BUILD_DIR / "README.html")

for file in (BUILD_DIR / "reference").glob("include*"):
    os.remove(file)
