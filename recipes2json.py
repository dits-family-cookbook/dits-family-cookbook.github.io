#!/usr/bin/env python

import json
import sys
import yaml
from pathlib import Path

from slugify import slugify

def load_recipes(recipes_dir):
  r = []
  for recipe in recipes_dir.glob('*.yml'):
    with recipe.open("r") as f:      
      data = yaml.safe_load(f)
      data["key"] = slugify(f"{recipe.parent.name}-{recipe.stem}")
      if not data.get("images"):
        data["images"] = []
      r.append(data)
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
      "subcategory": "Misc",
      "img": "desserts.jpg",
      "recipes":  load_recipes(Path("recipes/baking-and-desserts/desserts/"))
    }
  )
  recipes.append(
    {
      "category": "Breads",
      "subcategory": "",
      "img": "breads.jpg",
      "recipes":  load_recipes(Path("recipes/breads/"))
    }
  )
  recipes.append(
    {
      "category": "Canning",
      "subcategory": "",
      "img": "canning.jpg",
      "recipes":  load_recipes(Path("recipes/canning/"))
    }
  )
  recipes.append(
    {
      "category": "Miscellaneous",
      "subcategory": "",
      "img": "misc.jpg",
      "recipes":  load_recipes(Path("recipes/miscellaneous/"))
    }
  )
  recipes.append(
    {
      "category": "Main Courses",
      "subcategory": "",
      "img": "mains.jpg",
      "recipes":  load_recipes(Path("recipes/main-dishes/"))
    }
  )
  recipes.append(
    {
      "category": "Salads",
      "subcategory": "",
      "img": "salads.jpg",
      "recipes":  load_recipes(Path("recipes/salads/"))
    }
  )
  recipes.append(
    {
      "category": "Soups & Stews",
      "subcategory": "",
      "img": "soups-and-stews.jpg",
      "recipes":  load_recipes(Path("recipes/soups-and-stews/"))
    }
  )

  print(json.dumps(recipes))
