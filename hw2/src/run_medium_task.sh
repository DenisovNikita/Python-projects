#!/usr/bin/env sh
python3 gen_latex_table_and_image.py
cd ../artefacts/medium/ || exit
pdflatex table_and_image.tex
latexmk -c