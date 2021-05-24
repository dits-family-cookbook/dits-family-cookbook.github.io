#!/usr/bin/env python

import os
import re
import sys
import subprocess
import tempfile
from pathlib import Path


import attr
from attr import attrs, attrib
from jinja2 import Environment

E = Environment()

@attrs
class Recipe:
    title = attrib()
    category = attrib()
    preamble = attrib()
    ingredients = attrib()
    directions = attrib()

def md2recipe(filepath):
    with open(filepath) as f:
        md = f.read()
    m = re.search(r'(title:.*)', md)
    title = m.groups()[0].split(':')[1].strip()    
    tex = subprocess.run(["pandoc", "-t", "latex", filepath], capture_output=True).stdout.decode()
    m = re.search(r'(.*)(\\hypertarget.ingredients.*)(\\hypertarget.directions.*)', tex, re.DOTALL)    
    preamble = m.groups()[0].strip()
    ingredients = m.groups()[1].strip()
    directions = m.groups()[2].strip()
    

    return Recipe(
        title=title,
        category=filepath.parent,
        preamble=preamble,
        ingredients=ingredients,
        directions=directions
    )

    

def recipe2tex(recipe):
    with open("recipe.tex.j2") as f:
        t = E.from_string(f.read())
    return t.render(recipe=recipe)


def tex2pdf(name, category, tex):
    tex_dir = Path("pdf") / Path(category)
    if not tex_dir.exists():
        os.makedirs(tex_dir)
    tex_path = tex_dir / Path(name)
    with open(tex_path, "w") as f:
        f.write(tex)    
    subprocess.run(["pdflatex", name], cwd=tex_dir.absolute())

if __name__ == "__main__":
    p = Path(sys.argv[1])    
    r = md2recipe(p)
    tex = recipe2tex(r)
    tex2pdf(p.name.replace(".md", ".tex"), r.category, tex)
