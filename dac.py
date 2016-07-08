#!/usr/bin/env python3
from useful.mstring import prints

def calc(Rup, Rdown, Rdac, Vdac, Vref=1.21):
  Idown = Vref / Rdown
  Vdown = Idown * Rdown
  Idac  = (Vdac - Vref) / Rdac
  Iup   = Idown - Idac
  Vup   = Iup * Rup
  Vout  = Vup + Vref
  return Vout


def reverse(R2, Vmin, Vmax, Vdacmin, Vdacmax, Vref=1.21):
  """
    Id = (Vref - Vd) / Rd
    I2*R2 = V - Vref
    Vref = I1*R1 =>
      I1 = Vref / R1
    I2 + Id = I1 => 
      (V - Vref) / R2 + (Vref - Vd) / Rd = Vref / R1
      ----------------------------------------------
  """
  """
  (Vmin - Vref) / R2 + (Vref - Vdacmax) / Rd = Vref / R1     => R1 = (Vmin - Vref) / R2 + (Vref - Vdacmax) / Rd * Vref
  (Vmax - Vref) / R2 + (Vref - Vdacmin) / Rd = Vref / R1

  =>
  (Vmin - Vref) / R2 + (Vref - Vdacmax) / Rd = (Vmax - Vref) / R2 + (Vref - Vdacmin) / Rd
  
  (Vmin - Vref)*Rd + (Vref - Vdacmax)*R2 = (Vmax - Vref)*Rd +  (Vref - Vdacmin)*R2
  => 
  (Vmin - Vref)*Rd - (Vmax - Vref)*Rd = (Vref - Vdacmin)*R2 - (Vref - Vdacmax)*R2
  => (Vmin - Vref - Vmax + Vref)*Rd = (Vref - Vdacmin - Vref + Vdacmax) * R2
  (Vmin - Vmax) Rd = (Vdacmax-Vdacmin)* R2 =>
  Rd = (Vdacmax-Vdacmin)* R2 / (Vmin - Vmax)  #!
  -----------------------------------------------

  (V - Vref) / R2 + (Vref - Vd) / Rd = Vref / R1 =>
  R1 / Vref = (R2 * Rd) / ((V - Vref)*Rd + (Vref - Vd) * R2) =>
  R1 / Vref = R2 * Rd / ((V - Vref)*Rd + (Vref - Vd) * R2) =>
  R1  = R2 * Rd * Vref / ((V - Vref)*Rd + (Vref - Vd) * R2)
  """
  Rd  =  (Vdacmax-Vdacmin)* R2 / (Vmax-Vmin)
  R1  =  Vref / (Vmax/R2 - Vref*(R2 + Rd)/(R2*Rd) + Vdacmin/Rd)


  Idacmin = (Vdacmax - Vref) / Rd * 1000
  Idacmax = (Vdacmin - Vref) / Rd * 1000
  prints("Idacmin = {Idacmin:0.2f}mA, Idacmax={Idacmax:0.2f}mA")

  return R2, R1, Rd



if __name__ == '__main__':
  Rup   = 10000
  Vdacmin = 0.05
  Vdacmax = 3.3
  Vmin = 0.00
  Vmax = 15
  Rup, Rdown, Rdac = reverse(Rup, Vmin=Vmin, Vmax=Vmax, Vdacmin=Vdacmin, Vdacmax=Vdacmax)
  prints("Calculated resistors:\n Rup={Rup}, Rdown = {Rdown}, Rdac = {Rdac}")

  VminCalc = calc(Rup, Rdown, Rdac, Vdacmax)
  VmaxCalc = calc(Rup, Rdown, Rdac, Vdacmin)
  prints("Vmin={Vmin:.2f} (checked {VminCalc:.2f})\nVmax={Vmax:.2f} (checked: {VmaxCalc:.2f})")
  ratio = (Rup + Rdown) / Rdown;
  prints("ratio: {ratio:.2f}")
  #print(calc(5100, 530, 300, 3))

