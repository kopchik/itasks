#!/usr/bin/env python3

def calc(Rup, Rdown, Rdac, Vdac, Vref=1.21):
  Idown = Vref / Rdown
  Vdown = Idown * Rdown
  Idac  = (Vdac - Vref) / Rdac
  Iup   = Idown - Idac
  Vup   = Iup * Rup
  Vout  = Vup + Vref
  return Vout

"""
def reverse(Rup, Vmin, Vmax, Vdacmax, Vref=1.21):
  Idown = Iup + Idac
  Vdown = Vref
  V = Vref + Vup
  V = Vref + Vdac
  Idac = (Vdac - Vref) / Rdac

  Vmax = Vref + Vupmax
  Vmin = Vref + Vupmin
  Idacmax = ( - Vref) / Rdac
  Idacmin = (Vdacmax - Vref / Rdac


  Vupmax = Vdacmax - Vref
  Vupmin = -Vref  # is this correct?
  Iupmax + Idacmax = Vref / Rdown
  Iupmin + Idacmin = Vref / Rdown

  # =>
  Iupmax + Idacmax = Iupmin + Idacmin
  =>
  Iupmax - Upmin = - Vref / Rdac - (Vdacmax - Vref) / Rdac = -Vdacmax / Rdac
  Iupmax = (Vmax - Vref) / Rup
  Iupmin = (Vmin - Vref) / Rup
  =>
  (Vmax - Vref) / Rup - (Vmin - Vref) / Rup = -Vdacmax / Rdac
  => (Vmax - Vref - Vmin + Vref) / Rup  = -Vdacmax  / Rdac
  => (Vmax - Vmin) / Rup =  - Vdacmax / Rdac
  

  Rdac = Vdacmax * Rup / (Vmax - Vmin)
  Rdown = ((- Vref)  / Rdac + (Vmax - Vref) / Rup) / Vref
"""

from useful.mstring import prints
def reverse(Rup, Vmin, Vmax, Vdacmax, Vref=1.21):
  Rdac = Vdacmax * Rup / (Vmax - Vmin)
  Rdown = Vref / ((- Vref)  / Rdac + (Vmax - Vref) / Rup)


  Idacmax = ( - Vref) / Rdac*1000
  Idacmin = (Vdacmax - Vref) / Rdac * 1000
  prints("Idacmin = {Idacmin:0.2f}, Idacmax={Idacmax:0.2f}")
  return Rup, Rdown, Rdac


if __name__ == '__main__':
  Rup   = 5000
  Vdacmax = 3.3
  Vmin = 0.1
  Vmax = 20
  Rup, Rdown, Rdac = reverse(Rup, Vmin=Vmin, Vmax=Vmax, Vdacmax=Vdacmax)

  print(Rup, Rdown, Rdac)
  print(calc(Rup, Rdown, Rdac, Vdacmax))
  print(calc(Rup, Rdown, Rdac, 0.0))
  
