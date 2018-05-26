import random
import sys
import numpy as np
import fractions
from print_question import *


N = random.SystemRandom(0).randint(1,4)
M = random.SystemRandom(0).randint(1,4)
a = [ random.SystemRandom(0).randint(1,9) for i in range(0,N) ]
b = [ random.SystemRandom(0).randint(-10,10) for i in range(0,N) ]
c = [ random.SystemRandom(0).randint(1,9) for i in range(0,M) ]
d = [ random.SystemRandom(0).randint(-10,10) for i in range(0,M) ]

formula = "\\frac{"
for i in range(0,N):
  formula = formula + str(a[i])+"\\cdot 10^{"+str(b[i])+"}\\times "
formula = formula[:-7]+"}{"
for i in range(0,M):
  formula = formula + str(c[i])+"\\cdot 10^{"+str(d[i])+"}\\times "
formula = formula[:-7]+"}"

prefacteur = fractions.Fraction(np.array(a).prod(), np.array(c).prod())
exposant = np.array(b).sum() - np.array(d).sum()
exposant_wrong = np.array(d).sum() - np.array(b).sum()
answer = ""
distractor3 = ""
distractor2 = ""
distractor1 = ""
if prefacteur.denominator != 1:
  answer = "$\\frac{"+str(prefacteur.numerator)+"}{"+str(prefacteur.denominator)+"}\\cdot 10^{"+str(exposant)+"}$"
  distractor3 = "$\\frac{"+str(prefacteur.numerator)+"}{"+str(prefacteur.denominator)+"}\\cdot 10^{"+str(exposant_wrong)+"}$"
else:
  answer = "$"+str(prefacteur.numerator)+"\\cdot 10^{"+str(exposant)+"}$"
  distractor3 = "$"+str(prefacteur.numerator)+"\\cdot 10^{"+str(exposant_wrong)+"}$"
if prefacteur.numerator != 1:
  distractor1 = "$\\frac{"+str(prefacteur.denominator)+"}{"+str(prefacteur.numerator)+"}\\cdot 10^{"+str(exposant)+"}$"
  distractor2 = "$\\frac{"+str(prefacteur.denominator)+"}{"+str(prefacteur.numerator)+"}\\cdot 10^{"+str(exposant_wrong)+"}$"
else:
  distractor1 = "$"+str(prefacteur.denominator)+"\\cdot 10^{"+str(exposant)+"}$"
  distractor2 = "$"+str(prefacteur.denominator)+"\\cdot 10^{"+str(exposant_wrong)+"}$"

question = "Que vaut $"+formula+"$?"
answers = [answer, distractor1, distractor2, distractor3]

print_question("1211","Calcul",2,[9],question,answers)
