SHELL=/bin/bash

install:
	bundle install

view:
	bundle exec jekyll serve

book:
	sudo apt install texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-humanities
