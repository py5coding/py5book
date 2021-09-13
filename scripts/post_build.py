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
import re
from pathlib import Path
import shutil


BUILD_DIR = Path("_build/html/")

GITHUB_EDIT_LINK_REGEX = re.compile(
    r"https://github.com/hx2A/py5book/edit/main/reference/([^\.]*)\.rst"
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

for refdoc in BUILD_DIR.glob("reference/*.html"):
    with open(refdoc, "r") as f:
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

        new_link = f'https://github.com/hx2A/py5generator/edit/main/py5_docs/Reference/api_en/{stem}.txt'
        html = html.replace(original_link, new_link)

        # fix new issue link to point to py5generator repo
        html = html.replace('https://github.com/hx2A/py5book/issues/new?', 'https://github.com/hx2A/py5generator/issues/new?')

        with open(refdoc, "w") as f:
            f.write(html)


shutil.rmtree(BUILD_DIR / "files")
shutil.copytree("files", BUILD_DIR / "files")
