#!/bin/bash

gnuplot -persist > /dev/null 2>&1 << EOF
  set title "Lift Curve"
  set xlabel "Angle of Attack (deg)"
  set ylabel "Lift Coefficient"

  plot  "80grit.dat" using 1:2 title '80 grit' with linespoints,\
      "120grit.dat" using 1:2 title '120 grit' with linespoints,\
      "180grit.dat" using 1:2 title '180 grit' with linespoints
EOF
