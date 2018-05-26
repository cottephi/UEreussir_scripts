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

def get_domaine(funcs, div = False, factor = 1):
  domaine = "\\mathbb{R}"
  for i in range(0,len(funcs)):
    if funcs[i] == 'ln':
      domaine = "\\mathbb{R}^{+*}"
    if div and i == len(funcs)-1:
      if funcs[i] == 'ln':
        exclude = Fraction(factor.denominator,factor.numerator)
        domaine = domaine + "/\\{" + str(latex(Rational(exclude))) + "\\}"
      if funcs[i] == 'cos':
        exclude = Fraction(factor.denominator,2*factor.numerator)
        domaine = domaine + "/\\{\pm " + str(latex(pi*Rational(exclude))) + "\\}"
      if funcs[i] == 'sin':
        exclude = Fraction(factor.denominator,factor.numerator)
        domaine = domaine + "/\\{0," + str(latex(pi*Rational(exclude))) + "\\}"
  return domaine
  
def get_distractors(a,b,x,func):
  if func == 'exp':
    return [a*exp(b*x),a*b*exp(x),a*b*ln(x)]
  if func == 'cos':
    return [a*b*sin(b*x),-a*b*cos(b*x),-a*b*sin(x)]
  if func == 'sin':
    return [-a*b*cos(b*x),-a*b*sin(b*x),a*b*cos(x)]
  if func == 'ln':
    return [a*b/x,a*b*exp(b*x),a/(b*x)]
  if func == 'poly':
    return [a*b*x**(b+1),a*x**(b-1),a*b*x**b]
    
      
    
#themes:
  #functions:
    #1: af(bx)+c -> 3 termes to generate, 1 func
    #2: Sum(aifi(bix)+ci) -> i*3 termes to generate, i func
    #3: Prod(aifi(bix)+ci) -> i*3 termes to generate, i func
    #4: a1f1(b1x)/a2f2(b2x) -> 4 termes to generate, 2 func
    #5: a1f1(b1f2(b2x)) -> 3 termes to generate, 2 func
  #poly:
    #6: Sum(aix^gi) -> i*2 termes to generate
    #7: (a1x^g1+a2x^g2)/a3x^g3 -> 6 termes to generate
  #polyfunc:
    #8: Sum(aifi(bix)^gi) -> i*3 termes to generate, i func
    #9: af(Sum(bix^gi)) -> 1+i*2 termes to generate, 1 func
    #10: ax^g f(bx) -> 3 termes to generate, 1 func
theme = random.SystemRandom(0).randint(1,10)
theme = 10
Ntermes = 1
if theme == 3:
  Ntermes = 2
elif theme == 2 or theme == 6 or theme == 8 or theme == 9:
  Ntermes = random.SystemRandom(0).randint(2,3)
Nvalues = {1:3, 2:Ntermes*3, 3:Ntermes*3, 4:4, 5:3, 6:Ntermes*2, 7:6, 8:Ntermes*3, 9:1+Ntermes*2, 10:3}
Nfuncs = {1:1, 2:Ntermes, 3:Ntermes, 4:2, 5:2, 6:0, 7:0, 8:Ntermes, 9:1, 10:1}
possible_funcs = ['exp','cos','sin','ln']
variables = ["x","y","z","t","n","m","r","\\theta","\\phi","\\nu","\\mu","\\epsilon","\\varepsilon","\\varphi","\\alpha","\\beta","\\gamma","\\eta"]

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

div = False
if theme == 4 or theme == 7:
  div = True
domaine = get_domaine(funcs, div, values[-1])

if theme == 1 or theme == 2:
  distractor1 = 0
  distractor2 = 0
  distractor3 = 0
  function = 0
  for i in range(0,len(funcs)):
    variable = values[1+3*i]*x
    fun = values[3*i]*get_function(funcs[i],variable)+values[2+3*i]
    function = function + fun
    distr1, distr2, distr3 = get_distractors(values[3*i],values[1+3*i],x,funcs[i])
    distractor1 = distractor1 + distr1
    distractor2 = distractor2 + distr2
    distractor3 = distractor3 + distr3
  answer = diff(function,x)
  
if theme == 3:
  function = values[0]*get_function(funcs[0],values[1]*x)*values[2]*get_function(funcs[1],values[3]*x)
  answer = diff(function,x)
  distractor1, distractor2, distractor3 = get_distractors(values[0],values[1],x,funcs[0])
  distractor1 = distractor1*values[2]*get_function(funcs[1],values[3]*x)
  distractor2 = distractor2*values[2]*get_function(funcs[1],values[3]*x)
  distractor3 = distractor3*values[2]*get_function(funcs[1],values[3]*x)
  distr1, distr2, distr3 = get_distractors(values[2],values[3],x,funcs[1])
  distractor1 = distractor1+distr1*values[0]*get_function(funcs[0],values[1]*x)
  distractor2 = distractor2+distr2*values[0]*get_function(funcs[0],values[1]*x)
  distractor3 = distractor3+distr3*values[0]*get_function(funcs[0],values[1]*x)
  
if theme == 4:
  function = values[0]*get_function(funcs[0],values[1]*x)/(values[2]*get_function(funcs[1],values[3]*x))
  answer = diff(function,x)
  distractor1, distractor2, distractor3 = get_distractors(values[0],values[1],x,funcs[0])
  distractor1 = distractor1*values[2]*get_function(funcs[1],values[3]*x)
  distractor2 = distractor2*values[2]*get_function(funcs[1],values[3]*x)
  distractor3 = distractor3*values[2]*get_function(funcs[1],values[3]*x)
  distr1, distr2, distr3 = get_distractors(values[2],values[3],x,funcs[1])
  distractor1 = distractor1-distr1*values[0]*get_function(funcs[0],values[1]*x)
  distractor2 = distractor2-distr2*values[0]*get_function(funcs[0],values[1]*x)
  distractor3 = distractor3-distr3*values[0]*get_function(funcs[0],values[1]*x)
  distractor1 = distractor1/(values[2]**2 * get_function(funcs[1],values[3]*x)**2 )
  distractor2 = distractor2/(values[2]**2 * get_function(funcs[1],values[3]*x)**2 )
  distractor3 = distractor3/(values[2]**2 * get_function(funcs[1],values[3]*x)**2 )
  
if theme == 5:
  function = values[0]*get_function(funcs[0],values[1]*get_function(funcs[1],values[2]*x))
  answer = diff(function,x)
  distractor1 = answer / diff(get_function(funcs[1],values[2]*x),x)
  distractor2 = distractor1 * get_function(funcs[1],values[2]*x) / values[2]
  distractor3 = values[0]*values[2]*diff(get_function(funcs[1],values[2]*x),x)*get_function(funcs[0],values[1]*get_function(funcs[1],values[2]*x))
    
if theme == 6:
  distractor1 = 0
  distractor2 = 0
  distractor3 = 0
  function = 0
  for i in range(0,int(len(values)/2)):
    fun = values[2*i]*x**(values[1+2*i])
    function = function + fun
    distr1, distr2, distr3 = get_distractors(values[2*i],values[1+2*i],x,'poly')
    distractor1 = distractor1 + distr1
    distractor2 = distractor2 + distr2
    distractor3 = distractor3 + distr3
  answer = diff(function,x)

if theme == 7:
  function = (values[0]*x**values[1] + values[2]*x**values[3])/(values[4]*x**values[5])
  answer = diff(function,x)
  distractor1 = (values[0]/values[4])*x**(values[1]-values[5]-1) * (values[1]+values[5]) + (values[2]/values[4])*x**(values[3]-values[5]-1) * (values[3]+values[5])
  distractor2 = (values[0]/values[4])*x**(values[1]-values[5]-1) * (values[1]-values[5]) - (values[2]/values[4])*x**(values[3]-values[5]-1) * (values[3]-values[5])
  distractor3 = values[0]*x**(values[1]-1) * (values[1]-values[5]) + values[2]*x**(values[3]-1) * (values[3]-values[5])
  
if theme == 8:
  distractor1 = 0
  distractor2 = 0
  distractor3 = 0
  function = 0
  for i in range(0,len(funcs)):
    fun = values[3*i]*get_function(funcs[i],values[1+3*i]*x)**(values[2+3*i])
    function = function + fun
    distr1, distr2, distr3 = get_distractors(values[3*i],values[2+3*i],diff(get_function(funcs[i],values[1+3*i]*x)),'poly')
    distractor1 = distractor1 + distr1
    distractor2 = distractor2 + distr2
    distractor3 = distractor3 + distr3
  answer = diff(function,x)

if theme == 9:
  distractor = 0
  function = 0
  print(len(values))
  for i in range(1,int((len(values)+1)/2)):
    fun = values[i]*x**values[i+1]
    function = function + fun
    distr = values[i]*values[i+1]*x**(values[i+1]-1)
    distractor = distractor + distr
  answer = diff(values[0]*get_function(funcs[0],function))
  distractor1 = answer / distractor
  distractor2 = distractor1*function
  distractor3 = values[0]*diff(get_function(funcs[0],x)).replace(x,distractor)

if theme == 10:
  function = values[0]*x**values[1] * get_function(funcs[0],values[2]*x)
  answer = diff(function,x)
  distractor1 = values[0]*values[1]*x**(values[1]-1) * get_function(funcs[0],values[2]*x) - values[0]*x**values[1] * diff(get_function(funcs[0],values[2]*x),x)
  distractor2 = values[0]*values[1]*x**(values[1]-1) * diff(get_function(funcs[0],values[2]*x),x)
  distractor3 = values[0]*values[1]*x**(values[1]-1) * get_function(funcs[0],values[2]*x) + values[0]*x**(values[1]) * diff(get_function(funcs[0],values[2]*x),x)/values[2]

if answer == 0:
  exit()
  
question = "Quelle est la dérivée par rapport à $" + latex(x) + "$ de la fonction $f$ définie sur $" + domaine + "$ par $f(" + latex(x) + ")=" + latex(function) + "$?"
answers = [latex(answer), latex(distractor1), latex(distractor2), latex(distractor3)]
print_question("1211","dérivée",2,[],question,answers)
  
  
