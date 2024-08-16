#!/bin/bash

# Check if the file Asgn1.tex exists
if [ -f "Asgn1.tex" ]; then
    echo "Running pdflatex on Asgn1.tex"
    pdflatex Asgn1.tex
else
    echo "Error: Asgn1.tex not found"
fi

evince Asgn1.pdf &
