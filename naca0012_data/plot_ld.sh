#!/bin/bash

# Plot lift-to-drag ratio.

gnuplot -persist > /dev/null 2>&1 << EOF
  set title "L/D Curve"
  set xlabel "Angle of Attack (deg)"
  set ylabel "L/D"

  plot  "80grit.dat" using 1:(\$2/\$3) title '80 grit' with linespoints,\
      "120grit.dat" using 1:(\$2/\$3) title '120 grit' with linespoints,\
      "180grit.dat" using 1:(\$2/\$3) title '180 grit' with linespoints
EOF
