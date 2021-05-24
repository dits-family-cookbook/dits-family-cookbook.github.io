#!/usr/bin/env python


import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from datetime import datetime

import attr
from attr import attrib, attrs
from jinja2 import Environment

E = Environment()
TEMP_DIR = Path(tempfile.TemporaryDirectory().name)

os.makedirs(TEMP_DIR)

@attrs
class Recipe:
    title = attrib()
    category = attrib()
    preamble = attrib()
    ingredients = attrib()
    directions = attrib()


def md2recipe(md_path):
    """
    Convert markdown file to recipe class
    """    
    with open(md_path) as f:
        md = f.read()
    m = re.search(r"(title:.*)", md)
    title = m.groups()[0].split(":")[1].strip()
    tex = subprocess.run(
        ["pandoc", "-t", "latex", md_path], capture_output=True
    ).stdout.decode()
    m = re.search(
        r"(.*)(\\hypertarget.ingredients.*)(\\hypertarget.directions.*)", tex, re.DOTALL
    )
    preamble = m.groups()[0].strip()
    ingredients = m.groups()[1].strip()
    directions = m.groups()[2].strip()

    return Recipe(
        title=title,
        category=md_path.parent,
        preamble=preamble,
        ingredients=ingredients,
        directions=directions,
    )


def recipe2tex(recipe):
    """
    Convert recipe class to tex string
    """
    with open("page.tex.j2") as f:
        t = E.from_string(f.read())
    return t.render(
        page_title=recipe.title,
        page_preamble=recipe.preamble,
        page_left=recipe.ingredients,
        page_right=recipe.directions
    )

def make_chapter_tex(title, preamble=None, omit_date=True):
    with open("page.tex.j2") as f:
        t = E.from_string(f.read())
    return t.render(
        omit_date=omit_date,
        page_title=title,
        page_preamble=preamble,
        page_left=None,
        page_right=None
    )


def tex2pdf(tex, name):
    """
    Convert tex string to pdf document
    """
    tex_name = name + ".tex"
    pdf_name = name + ".pdf"
    with open(TEMP_DIR / tex_name, "w") as f:
        f.write(tex)
    subprocess.run(["pdflatex", name], cwd=TEMP_DIR, capture_output=True)


if __name__ == "__main__":
    tex = make_chapter_tex("Dit's Cookbook", preamble=None, omit_date=False)
    tex2pdf(tex, "cover")
    p = Path(sys.argv[1])
    r = md2recipe(p)
    tex = recipe2tex(r)
    tex2pdf(tex, p.stem)
    print(f"Files written to {TEMP_DIR}")
