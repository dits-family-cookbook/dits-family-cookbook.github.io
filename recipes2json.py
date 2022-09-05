#!/usr/bin/env python

import json
import sys
import yaml
from pathlib import Path


def load_recipes(recipes_dir):
  r = []
  for recipe in recipes_dir.glob('*.yml'):
    with recipe.open("r") as f:
      r.append(yaml.safe_load(f))
  return sorted(r, key=lambda x: x["title"])


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
  recipes.append(
    {
      "category": "Baking & Desserts",
      "subcategory": "Cakes",
      "img": "cakes.jpg",
      "recipes":  load_recipes(Path("recipes/baking-and-desserts/cakes/"))
    }
  )
  recipes.append(
    {
      "category": "Baking & Desserts",
      "subcategory": "Cookies",
      "img": "cookies.jpg",
      "recipes":  load_recipes(Path("recipes/baking-and-desserts/cookies/"))
    }
  )
  recipes.append(
    {
      "category": "Baking & Desserts",
      "subcategory": "Desserts",
      "img": "desserts.jpg",
      "recipes":  load_recipes(Path("recipes/baking-and-desserts/desserts/"))
    }
  )

  print(json.dumps(recipes))
