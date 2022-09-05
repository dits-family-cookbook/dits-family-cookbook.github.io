#!/usr/bin/env python

import json
import sys
import yaml
from pathlib import Path


def load_recipes(recipes_dir):
  r = []
  for recipe in recipes_dir.glob('*'):
    with recipe.open("r") as f:
      r.append(yaml.safe_load(f))
  return r


if __name__ == "__main__":
  recipes = []
  recipes.append(
    {
      "category": "Baking & Desserts",
      "subcategory": "Bars",
      "img": "bars.jpg",
      "recipes":  load_recipes(Path("recipes/baking-and-desserts/bars/"))
    }
  )
  print(json.dumps(recipes))
