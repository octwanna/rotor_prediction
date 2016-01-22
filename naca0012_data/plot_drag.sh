#!/bin/bash

gnuplot -persist > /dev/null 2>&1 << EOF
  set title "Drag Curve"
  set xlabel "Angle of Attack (deg)"
  set ylabel "Drag Coefficient"

  plot  "80grit.dat" using 1:3 title '80 grit' with linespoints,\
      "120grit.dat" using 1:3 title '120 grit' with linespoints,\
      "180grit.dat" using 1:3 title '180 grit' with linespoints
EOF
