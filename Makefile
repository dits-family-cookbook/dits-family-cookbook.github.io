SHELL=/bin/bash

all: recipes.json recipes-list

.PHONY: recipes.json
recipes.json:
	venv/bin/python recipes2json.py > recipes.json

.PHONY: recipes-list
recipes-list:
	find recipes/ -iname "*.yml" | sed 's|^recipes/||g' | sed 's|.md$$||g' | awk -F / '{print $$(NF-1) " :: " $$NF}' | sort > recipes-list.txt

book:
	sudo apt install texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-humanities

