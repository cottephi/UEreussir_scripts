import random
import sys
import numpy as np
import fractions
import math
from graph import *


def get_xy(r):
  sx = ""
  sy = ""
  fx = 0
  fy = 0
  signs = ["1","-1"]
  sxy_possibles = ["\\sqrt{3}/2","\\frac{1}{2}","\\sqrt{2}/2"]
  fxy_possibles = [math.sqrt(3)/2.,0.5,math.sqrt(2)/2.]
  i = random.SystemRandom(0).randint(0,2)
  sign = signs[random.SystemRandom(0).randint(0,1)]
  sx = sign[:-1]+str(r)+sxy_possibles[i]
  fx = str(sign)*r*fxy_possibles[i]
  sign = signs[random.SystemRandom(0).randint(0,1)]
  sy = sign[:-1]+str(r)+xy_possibles[abs(i-2)]
  fy = str(sign)*r*fxy_possibles[abs(i-2)]
  return [sx, sy, fx, fy]
  
def get_theta_r():  r = 0
  stheta = ""
  ftheta = 0
  rmax = 50
  theta_denoms = ["2","3","4","6"]
  if method == "graph":
    rmax = 3
  r = random.SystemRandom(0).randint(1,rmax)
  theta_denom = theta_denoms[random.SystemRandom(0).randint(0,3)]
  theta_num = random.SystemRandom(0).randint(1,12)
  while float(theta_num/int(theta_denom)) %1 == 0:
    theta_denom = theta_denoms[random.SystemRandom(0).randint(0,3)]
    theta_num = random.SystemRandom(0).randint(1,12)
    
  stheta = str(theta_num)+"\\pi/"+theta_denom
  ftheta = float(theta_num*math.pi/int(theta_denom))
    
  return [r,stheta,ftheta]

difficulty = 1
if len(sys.argv) == 2:
  difficulty = int(sys.argv[1])
  

methods = ["coord","graph"]
method = methods[random.SystemRandom(0).randint(0,2)]
initials = ["xy","xr","yr","xtheta","ytheta","rtheta"]
initial = initials[random.SystemRandom(0).randint(0,5)]

  
  


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
