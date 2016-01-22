#!/usr/bin/python

"""
Gives figures for comparison to other rotor models.
Inputs:
1. rotor radius (m)
2. thrust (N)
"""

import sys
import math

def power_mt(radius, thrust):
  density = 1.18
  area = 0.5*math.pi*radius**2
  power = math.sqrt( thrust**3 / 2 / density / area )
  return power

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print "Correct input arguments: <rotor radius (m)> <rotor thrust (N)>"
    sys.exit()
  radius = float(sys.argv[1])
  thrust = float(sys.argv[2])

  power = power_mt(radius, thrust)

  print "Thrust: "+str(thrust)+" N"
  print "Power: "+str(power)+" W"
  print "Thrust efficiency: "+str( thrust / power * 1000.0 )+" N/kW"