#!/usr/bin/python

"""
Blade element theory.
Simple formulation for inflow velocity
Inputs:
1. rotor radius (m)
2. thrust (N)
"""

import sys
import math


def perf_bet(radius):
  # Parameters
  OMEGA = 500
  N = 1000
  NB = 2
  DENSITY = 1.18
  CL = 1
  CD = 0.01
  CHORD = 0.1

  area = 0.5*math.pi*radius**2
  dr = radius / N
  da = dr*CHORD
  r = [ ( dr / 2.0 + radius * float(x) / float(N) ) for x in range(0,N) ]
  v = [ x*OMEGA for x in r ]
  q = [ x*x*0.5*DENSITY for x in v ]
  dl = [ x*CL*da for x in q ]
  dd = [ x*CD*da for x in q ]
  dp = [ x*y for (x,y) in zip(dd,v) ]
  thrust = sum(dl)
  power = sum(dp)

  return (power, thrust)

if __name__ == "__main__":
  # if len(sys.argv) != 2:
    # print "Correct input arguments: <rotor radius (m)> <rotor thrust (N)>"
    # sys.exit()
  # radius = float(sys.argv[1])
  # thrust = float(sys.argv[2])

  radius = 0.3

  (power, thrust) = perf_bet(radius)

  print "Thrust: "+str(thrust)+" N"
  print "Power: "+str(power)+" W"
  print "Thrust efficiency: "+str( thrust / power * 1000.0 )+" N/kW"

  import mt
  print "Power ratio (BET/MT): "+str(power / mt.power_mt(radius, thrust))