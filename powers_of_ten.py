import random
import sys
import numpy as np
import fractions


difficulty = 1
if len(sys.argv) == 2:
  difficulty = int(sys.argv[1])
  
N = random.SystemRandom(0).randint(1,difficulty)
M = random.SystemRandom(0).randint(1,difficulty)
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
true = ""
distractor3 = ""
distractor2 = ""
distractor1 = ""
if prefacteur.denominator != 1:
  true = "\\frac{"+str(prefacteur.numerator)+"}{"+str(prefacteur.denominator)+"}\\cdot 10^{"+str(exposant)+"}"
  distractor3 = "\\frac{"+str(prefacteur.numerator)+"}{"+str(prefacteur.denominator)+"}\\cdot 10^{"+str(exposant_wrong)+"}"
else:
  true = str(prefacteur.numerator)+"\\cdot 10^{"+str(exposant)+"}"
  distractor3 = str(prefacteur.numerator)+"\\cdot 10^{"+str(exposant_wrong)+"}"
if prefacteur.numerator != 1:
  distractor1 = "\\frac{"+str(prefacteur.denominator)+"}{"+str(prefacteur.numerator)+"}\\cdot 10^{"+str(exposant)+"}"
  distractor2 = "\\frac{"+str(prefacteur.denominator)+"}{"+str(prefacteur.numerator)+"}\\cdot 10^{"+str(exposant_wrong)+"}"
else:
  distractor1 = str(prefacteur.denominator)+"\\cdot 10^{"+str(exposant)+"}"
  distractor2 = str(prefacteur.denominator)+"\\cdot 10^{"+str(exposant_wrong)+"}"

answers = [true, distractor1, distractor2, distractor3]
tags = ["true", "false", "false", "false"]
index = [0, 1, 2, 3]
random.shuffle(index)

question = "\\begin{question}{1211}{Calcul}{}{/}\n    Que vaut $"+formula+"$?\n\\end{question}\n\n\\begin{reponses}\n    \\item["+tags[index[0]]+"] $"+answers[index[0]]+"$\n    \\item["+tags[index[1]]+"] $"+answers[index[1]]+"$\n    \\item["+tags[index[2]]+"] $"+answers[index[2]]+"$\n    \\item["+tags[index[3]]+"] $"+answers[index[3]]+"$\n\\end{reponses}\n"

print(question)
