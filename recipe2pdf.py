#!/usr/bin/env python

import re
import sys
import subprocess

import attr
from attr import attrs, attrib
from jinja2 import Environment

E = Environment()

@attrs
class Recipe:
    title = attrib()
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
        preamble=preamble,
        ingredients=ingredients,
        directions=directions
    )

def recipe2pdf(recipe):
    with open("recipe.tex.j2") as f:
        t = E.from_string(f.read())
    print(t.render(recipe=recipe))    


if __name__ == "__main__":
    r = md2recipe(sys.argv[1])
    recipe2pdf(r)
