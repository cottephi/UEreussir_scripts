import random
import sys
import numpy as np
from fractions import Fraction
from sympy import *

def poly(difficulty, forceterms = 0):
  terms = forceterms
  signchoice = [-1,1]
  if terms == 0:
    terms = random.SystemRandom(0).randint(1,difficulty)
  coeff = []
  expo = []
  if difficulty == 1:
    coeff = [ Fraction(random.SystemRandom(0).randint(1,9), 1) for i in range(0,terms) ]
    expo = [ Fraction(random.SystemRandom(0).randint(1,3), 1) for i in range(0,terms) ]
  if difficulty == 2:
    coeff = [ Fraction(random.choice(signchoice)*random.SystemRandom(0).randint(1,9), 1) for i in range(0,terms) ]
    expo = [ Fraction(random.choice(signchoice)*random.SystemRandom(0).randint(1,3), 1) for i in range(0,terms) ]
  if difficulty == 3:
    coeff = [ Fraction(random.choice(signchoice)*random.SystemRandom(0).randint(1,9),random.choice(signchoice)*random.SystemRandom(0).randint(1,9)) for i in range(0,terms) ]
    expo = [ Fraction(random.choice(signchoice)*random.SystemRandom(0).randint(1,3), random.choice(signchoice)*random.SystemRandom(0).randint(1,3)) for i in range(0,terms) ]
  if difficulty > 3:
    coeff = [ Fraction(random.choice(signchoice)*random.SystemRandom(0).randint(1,15), random.choice(signchoice)*random.SystemRandom(0).randint(1,15)) for i in range(0,terms) ]
    expo = [ Fraction(random.choice(signchoice)*random.SystemRandom(0).randint(1,15), random.choice(signchoice)*random.SystemRandom(0).randint(1,15)) for i in range(0,terms) ]
    return [terms, coeff, expo]

functions = ["cos","sin","exp","ln","tan","poly","poly","poly"]
compositions = ["","+","-","*","-1","/","pow","comp"]


difficulty = 1
if len(sys.argv) == 2:
  difficulty = int(sys.argv[1])
  
mycomp = ""
if difficulty == 2:
  mycomp = compositions[random.SystemRandom(0).randint(0,1)]
if difficulty == 3:
  mycomp = compositions[random.SystemRandom(0).randint(0,3)]
if difficulty == 4:
  mycomp = compositions[random.SystemRandom(0).randint(0,5)]
if difficulty == 5:
  mycomp = compositions[random.SystemRandom(0).randint(0,6)]
if difficulty == 6:
  mycomp = compositions[random.SystemRandom(0).randint(0,7)]
if difficulty == 7:
  mycomp = compositions[random.SystemRandom(0).randint(1,7)]
if difficulty == 8:
  mycomp = compositions[random.SystemRandom(0).randint(2,7)]
if difficulty == 9:
  mycomp = compositions[random.SystemRandom(0).randint(3,7)]
if difficulty == 10:
  mycomp = compositions[random.SystemRandom(0).randint(4,7)]
if difficulty == 11:
  mycomp = compositions[random.SystemRandom(0).randint(5,7)]
if difficulty == 12:
  mycomp = compositions[random.SystemRandom(0).randint(6,7)]
if difficulty > 12:
  mycomp = compositions[7]
  
funcs = ["",""]
funcs[0] = functions[random.SystemRandom(0).randint(0,7)]
if mycomp == "+" or mycomp == "-" or mycomp == "*" or mycomp == "/":
  funcs[1] = functions[random.SystemRandom(0).randint(0,7)]
elif mycomp == "pow":
  funcs[1] = poly(difficulty,1)
elif mycomp == "comp":
  while funcs[1] == "" or funcs[0] == funcs[1]:
    funcs[1] = functions[random.SystemRandom(0).randint(0,7)]

if funcs[0] == "poly":
  funcs[0] = poly(difficulty)
if funcs[1] == "poly":
  funcs[1] = poly(difficulty)
  
print(funcs,mycomp)

  
exit()  
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

prefacteur = Fraction(np.array(a).prod(), np.array(c).prod())
exposant = np.array(b).sum() - np.array(d).sum()
exposant_wrong = np.array(d).sum() - np.array(b).sum()
true = "\\frac{"+str(prefacteur.numerator)+"}{"+str(prefacteur.denominator)+"}\\cdot 10^{"+str(exposant)+"}"
distractor1 = "\\frac{"+str(prefacteur.denominator)+"}{"+str(prefacteur.numerator)+"}\\cdot 10^{"+str(exposant)+"}"
distractor2 = "\\frac{"+str(prefacteur.denominator)+"}{"+str(prefacteur.numerator)+"}\\cdot 10^{"+str(exposant_wrong)+"}"
distractor3 = "\\frac{"+str(prefacteur.numerator)+"}{"+str(prefacteur.denominator)+"}\\cdot 10^{"+str(exposant_wrong)+"}"

answers = [true, distractor1, distractor2, distractor3]
tags = ["true", "false", "false", "false"]
index = [0, 1, 2, 3]
random.shuffle(index)

question = "\\begin{question}{1211}{Calcul}{}{/}\n    Que vaut $"+formula+"$?\n\\end{question}\n\n\\begin{reponses}\n    \\item["+tags[index[0]]+"] $"+answers[index[0]]+"$\n    \\item["+tags[index[1]]+"] $"+answers[index[1]]+"$\n    \\item["+tags[index[2]]+"] $"+answers[index[2]]+"$\n    \\item["+tags[index[3]]+"] $"+answers[index[3]]+"$\n\\end{reponses}\n"

print(question)
