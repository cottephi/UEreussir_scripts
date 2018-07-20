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


question = "Que vaut $"+formula+"$?"
answers = [answer, distractor1, distractor2, distractor3]

print_question("1211","Calcul",2,[9],question,answers)
