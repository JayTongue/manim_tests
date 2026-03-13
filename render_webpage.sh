#!/bin/bash

SCENES=$(grep -v '^\s*#' slides.py | grep -oP '(?<=^class )\w+(?=\(Slide\))' | tr '\n' ' ')
echo "Rendering scenes: $SCENES"

# manim -qm --disable_caching slides.py $SCENES
manim -qm  slides.py $SCENES
# manim -qm --flush_cache slides.py $SCENES
manim-slides convert $SCENES slides.html
