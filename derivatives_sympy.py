import random
import sys
import numpy as np
from fractions import *
from sympy import *
from print_question import *

def get_function(func, var):
  if func == 'exp':
    return exp(var)
  if func == 'cos':
    return cos(var)
  if func == 'sin':
    return sin(var)
  if func == 'ln':
    return ln(var)

def get_domaine(func):
  if func == 'ln':
    return "\\mathbb{R}^{+*}"
  else:
    return "\\mathbb{R}"
    
def get_distractors(a,b,x,func):
  if func == 'exp':
    return [latex(a*exp(b*x)),latex(a*b*exp(x)),latex(a*b*ln(x))]
  if func == 'cos':
    return [latex(a*b*sin(b*x)),latex(-a*b*cos(b*x)),latex(-a*b*sin(x))]
  if func == 'sin':
    return [latex(-a*b*cos(b*x)),latex(-a*b*sin(b*x)),latex(a*b*cos(x))]
  if func == 'ln':
    return [latex(a*b/x),latex(a*b*exp(b*x)),latex(a/(b*x))]
    
#themes:
  #functions:
    #1: af(bx)+c -> 3 termes to generate, 1 func
    #2: Sum(aifi(bix)+ci) -> i*3 termes to generate, i func
    #3: Prod(aifi(bix)+ci) -> i*3 termes to generate, i func
    #4: a1f1(b1x)/a2f2(b2x) -> 4 termes to generate, 2 func
    #5: a1f1(b1f2(b2x)) -> 3 termes to generate, 2 func
  #poly:
    #6: Sum(aix^gi) -> i*2 termes to generate
    #7: (a1x^g1+a2x^g2)/a3x^g3 -> 4 termes to generate
  #polyfunc:
    #8: Sum(aifi(bix)^gi) -> i*3 termes to generate, i func
    #9: af(Sum(bix^gi)) -> 1+i*2 termes to generate, 1 func
    #10: ax^g f(bx) -> 3 termes to generate, 1 func
theme = random.SystemRandom(0).randint(1,10)
theme = 1
Ntermes = 1
if theme == 3:
  Ntermes = 2
elif theme == 2 or theme == 6 or theme == 8 or theme == 9:
  Ntermes = random.SystemRandom(0).randint(2,3)
Nvalues = {1:3, 2:Ntermes*3, 3:Ntermes*3, 4:4, 5:3, 6:Ntermes*2, 7:4, 8:Ntermes*3, 9:1+Ntermes*2, 10:3}
Nfuncs = {1:1, 2:Ntermes, 3:Ntermes, 4:3, 5:2, 6:0, 7:0, 8:Ntermes, 9:1, 10:1}
possible_funcs = ['exp','cos','sin','ln']
variables = ["x","y","z","t","n","m","r","\\theta","\\phi","\\nu","\\mu","\\epsilon","\\varepsilon","\\varphi","\\alpha","\\beta","\\gamma","\\eta","chien","chat","banane"]

x = symbols(variables[random.SystemRandom(0).randint(0,len(variables)-1)])
values = []
funcs = []

for i in range(0,Nvalues[theme]):
  frac = 1
  while frac == 1:
    frac = Fraction(random.SystemRandom(0).randint(1,10), random.SystemRandom(0).randint(1,10))
  num = frac.numerator
  denum = frac.denominator
  sign = random.SystemRandom(0).choice([-1,1])
  values.append(sign*frac)

for i in range(0,Nfuncs[theme]):
  funcs.append(possible_funcs[random.SystemRandom(0).randint(0,len(possible_funcs)-1)])

if theme == 1:
  variable = values[1]*x
  domaine = get_domaine(funcs[0])
  function = values[0]*get_function(funcs[0],variable)+values[2]
  answer = latex(diff(function,x))
  distractor1, distractor2, distractor3 = get_distractors(values[0],values[1],x,funcs[0])
  
  question = "Quelle est la dérivée par rapport à $" + latex(x) + "$ de la fonction $f$ définie sur $" + domaine + "$ par $f(" + latex(x) + ")=" + latex(function) + "$?"
  answers = [answer, distractor1, distractor2, distractor3]
  print_question("1211","Calcul",2,[],question,answers)
  
