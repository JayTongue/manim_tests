#!/bin/bash
SCENES=$(grep -v '^\s*#' slides.py | grep -oP '(?<=^class )\w+(?=\(.*Slide)' | tr '\n' ' ')
echo "Rendering scenes: $SCENES"

# manim -qm slides.py $SCENES
# manim-slides convert $SCENES slides.html

manim -qh slides.py $SCENES
manim-slides convert --one-file $SCENES one_shot_slides.html