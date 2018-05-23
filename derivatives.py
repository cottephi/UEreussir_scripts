import random
import sys
import numpy as np
import fractions
from print_question import *

derivatives_and_primitives = {'e^{x}':['e^{x}','e^{x}'],'\\cos(x)':['-\\sin(x)','\\sin(x)'],'\\sin(x)':['\\cos(x)','-\\cos(x)'],'\\ln(x)':['\\frac{1}{x}','x\\ln(x)-x']}

def theme1(values,funcs,variable):
  function = values[0][0]
  new_variable = values[1][0]
  if values[1][1] != "1":
    new_variable = new_variable + values[1][1]
  new_variable = new_variable + variable
  if values[0][1] != "1":
    function = function + values[0][1]
  function = function + funcs[0].replace('x',new_variable)
  if values[2][0] == "-":
    function = function + "-"
  else:
    function = function + "+"
  function = function + values[2][1]
  domaine = "\\mathbb{R}"
  if funcs[0] == 'ln(x)':
    domaine = "\\mathbb{R}^{+*}"
  question = "Quelle est la dérivée par rapport à $" + variable + "$ de la fonction $f$ définie sur $" + domaine + "$ par $f(" + variable + ")=" + function + "$?"
  print(question)


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
if theme == 2 or theme == 3 or theme == 6 or theme == 8 or theme == 9:
  Ntermes = random.SystemRandom(0).randint(2,3)
Nvalues = {1:3, 2:Ntermes*3, 3:Ntermes*3, 4:4, 5:3, 6:Ntermes*2, 7:4, 8:Ntermes*3, 9:1+Ntermes*2, 10:3}
Nfuncs = {1:1, 2:Ntermes, 3:Ntermes, 4:3, 5:2, 6:0, 7:0, 8:Ntermes, 9:1, 10:1}
possible_funcs = ['e^{x}','\\cos(x)','\\sin(x)','\\ln(x)']
variables = ["x","y","z","t","n","m","r","\\theta","\\phi","\\nu","\\mu","\\epsilon","\\varepsilon","\\varphi","\\alpha","\\beta","\\gamma","\\eta","chien","chat","banane"]

variable = variables[random.SystemRandom(0).randint(0,len(variables)-1)]
values = []
funcs = []
for i in range(0,Nvalues[theme]):
  num = random.SystemRandom(0).randint(1,10)
  denum = random.SystemRandom(0).randint(1,10)
  sign = random.SystemRandom(0).randint(0,1)
  num = 2
  denum = 1
  if sign == 1:
    sign = "-"
  else:
    sign = ""
  if denum == 1 and num != 1:
    values.append([sign,str(num)])
  elif denum == num:
    values.append([sign,"1"])
  else:
    value = fractions.Fraction(num,denum)
    values.append([sign,"\\frac{"+str(value.numerator)+"}{"+str(value.denominator)+"}"])
for i in range(0,Nfuncs[theme]):
  funcs.append(possible_funcs[random.SystemRandom(0).randint(0,len(possible_funcs)-1)])
theme1(values,funcs,variable)

