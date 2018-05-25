import random
import sys
import numpy as np
import fractions
import sympy
from print_question import *

derivatives_and_primitives = {'e^{x}':['e^{x}','e^{x}'],'\\cos(x)':['-\\sin(x)','\\sin(x)'],'\\sin(x)':['\\cos(x)','-\\cos(x)'],'\\ln(x)':['\\frac{1}{x}','x\\ln(x)-x']}

def start_factor(old_sentence, sign, value):
  sentence = old_sentence
  if sign == "-":
    sentence = sentence + sign
  if type(value) is str:
    if value != "1":
      sentence = sentence + value
  else:
    if value != 1:
      if value.denominator == 1:
        sentence = sentence + str(value.numerator)
      else:
        sentence = sentence + "\\frac{" + str(value.numerator) + "}{" + str(value.denominator) + "}"
  return sentence
  
def start_value(old_sentence, sign, value):
  sentence = old_sentence
  if sign == "-":
    sentence = sentence + sign
  if type(value) is str:
    sentence = sentence + value
  else:
    if value == 1:
      sentence = sentence + "1"
    else:
      if value.denominator == 1:
        sentence = sentence + str(value.numerator)
      else:
        sentence = sentence + "\\frac{" + str(value.numerator) + "}{" + str(value.denominator) + "}"
  return sentence

def add_factor(old_sentence, sign, value):
  sentence = old_sentence
  if sign == "-":
    sentence = sentence + sign
  else:
    sentence = sentence + "+"
  if type(value) is str:
    if value != "1":
      sentence = sentence + value
  else:
    if value != 1:
      if value.denominator == 1:
        sentence = sentence + str(value.numerator)
      else:
        sentence = sentence + "\\frac{" + str(value.numerator) + "}{" + str(value.denominator) + "}"
  return sentence
  
def add_value(old_sentence, sign, value):
  sentence = old_sentence
  if sign == "-":
    sentence = sentence + sign
  else:
    sentence = sentence + "+"
  if type(value) is str:
    sentence = sentence + value
  else:
    if value == 1:
      sentence = sentence + "1"
    else:
      if value.denominator == 1:
        sentence = sentence + str(value.numerator)
      else:
        sentence = sentence + "\\frac{" + str(value.numerator) + "}{" + str(value.denominator) + "}"
  return sentence
  
def multiply_factor(old_sentence, sign, value):
  sentence = old_sentence
  parenthese = ""
  if sign == "-":
    sentence = sentence + "\\times (" + sign
    parenthese = ")"
  else:
    sentence = sentence + "\\times "
  if type(value) is str:
    if value != "1":
      sentence = sentence + value
  else:
    if value != 1:
      if value.denominator == 1:
        sentence = sentence + str(value.numerator)
      else:
        sentence = sentence + "\\frac{" + str(value.numerator) + "}{" + str(value.denominator) + "}"
  return [sentence,parenthese]

def form_derivative(previous_string,variable,funcs,sign1,sign2,values1,values2,ans_or_dist, start_or_add):
  output = ""
  sign = ""
  if funcs != '\\ln(x)':
    new_variable = start_factor("", sign2, values2)
    new_variable = new_variable + variable
    if sign1 != sign2:
      sign = "-"
    if ans_or_dist != 1:
      if start_or_add == 0:
        output = start_factor(previous_string, sign, values1*values2)
      else:
        output = add_factor(previous_string, sign, values1*values2)
    else:
      if start_or_add == 0:
        output = start_factor(previous_string, sign, values1)
      else:
        output = add_factor(previous_string, sign, values1)
    if ans_or_dist !=3
      output = output + derivatives_and_primitives[funcs][0].replace('x', new_variable)
    else:
      output = output + derivatives_and_primitives[funcs][0].replace('x', variable)
  else:
    if start_or_add != 0 and sign1 != "-":
      sign1 = "+"
    if ans_or_dist == 0:
      output = previous_string + sign1 + "\\frac{" + str(value1.numerator) + "}{" + str(value1.denominator) + variable + "}"
    if ans_or_dist == 1:
      if sign1 != sign2:
        sign = "-"
      value = value1*value2
      output = previous_string + sign + "\\frac{" + str(value.numerator) + "}{" + str(value.denominator) + variable + "}"
    if ans_or_dist == 2:
      new_variable = start_factor("", sign2, values2)
      new_variable = new_variable + variable
    
  return output
def theme_1_or_2(values_str, values_frac, funcs, variable):
  function = ""
  domaine = "\\mathbb{R}"
  for i in range(0,len(funcs)):
    if i == 0:
      function = start_factor(function, values_str[3*i][0], values_str[3*i][1])
    else:
      function = add_factor(function, values_str[3*i][0], values_str[3*i][1])
    new_variable = start_factor("", values_str[1+3*i][0], values_str[1+3*i][1])
    new_variable = new_variable + variable
    function = function + funcs[i].replace('x', new_variable)
    function = add_value(function, values_str[2+3*i][0], values_str[2+3*i][1])
    if funcs[i] == '\\ln(x)':
      domaine = "\\mathbb{R}^{+*}"
      
  question = "Quelle est la dérivée par rapport à $" + variable + "$ de la fonction $f$ définie sur $" + domaine + "$ par $f(" + variable + ")=" + function + "$?"
  
  answer = ""
  distractor1 = ""
  distractor2 = ""
  distractor3 = ""
  
  for i in range(0,len(funcs)):
    answer = form_derivative(answer,variable,funcs[0],values_str[3*i][0],values_str[1+3*i][0],values_frac[3*i],values_frac[1+3*i],0,i)
    distractor1 = form_derivative(distractor1,variable,funcs[0],values_str[3*i][0],values_str[1+3*i][0],values_frac[3*i],values_frac[1+3*i],1,i)
    distractor2 = form_derivative(distractor2,variable,funcs[0],values_str[3*i][0],values_str[1+3*i][0],values_frac[3*i],values_frac[1+3*i],2,i)
    distractor3 = form_derivative(distractor3,variable,funcs[0],values_str[3*i][0],values_str[1+3*i][0],values_frac[3*i],values_frac[1+3*i],3,i)
    
  answers = [answer, distractor1, distractor2, distractor3]
  print_question("1211","dérivées",2,[],question,answers)

def theme_3(values_str, values_frac, funcs, variable):
  domaine = "\\mathbb{R}"
  function = start_factor("", values_str[0][0], values_str[0][1])
  new_variable = start_factor("", values_str[1][0], values_str[1][1])
  new_variable = new_variable + variable
  function = function + funcs[0].replace('x', new_variable)
  if funcs[0] == '\\ln(x)':
    domaine = "\\mathbb{R}^{+*}"
      
  func_factor = multiply_factor(function, values_str[2][0], values_str[2][1])
  function = func_factor[0]
  new_variable = start_factor("", values_str[3][0], values_str[3][1])
  new_variable = new_variable + variable
  function = function + funcs[1].replace('x', new_variable) + func_factor[1]
  
  question = "Quelle est la dérivée par rapport à $" + variable + "$ de la fonction $f$ définie sur $" + domaine + "$ par $f(" + variable + ")=" + function + "$?"
  
  sign = ""
  if values_str[0][0] != values_str[1][0]:
    sign = "-"
  answer = start_factor("", sign, values_frac[0]*values_frac[1])
  distractor1 = start_factor("", values_str[0][0], values_frac[0])
  distractor2 = answer
  distractor3 = answer

  new_variable = start_factor("", values_str[1][0], values_str[1][1])
  new_variable = new_variable + variable
  if funcs[0] == '\\ln(x)' and values_frac[1].denominator != 1:
    new_variable = start_factor("", values_str[1][0], values_frac[1].numerator)
    new_variable = new_variable + variable
    
  answer = answer + derivatives_and_primitives[funcs[0]][0].replace('x', new_variable)
  distractor1 = distractor1 + derivatives_and_primitives[funcs[0]][0].replace('x', new_variable)
  if funcs[0] == '\\ln(x)' and values_frac[1].denominator != 1:
    answer = answer.replace("\\frac{1}", "\\frac{" + str(values_frac[1].denominator) + "}")
    distractor1 = distractor1.replace("\\frac{1}", "\\frac{" + str(values_frac[1].denominator) + "}")
  distractor2 = distractor2 + funcs[0].replace('x', new_variable)
  distractor3 = distractor3 + funcs[0].replace('x', variable)

  ans_factor = multiply_factor(answer, sign, values_frac[2]*values_frac[3])
  answer = ans_factor[0]
  dist1_factor = multiply_factor(distractor1, values_str[2][0], values_frac[3])
  distractor1 = dist1_factor[0]
  dist2_factor = multiply_factor(distractor2, sign, values_frac[2]*values_frac[3])
  distractor2 = dist2_factor[0]
  dist3_factor = multiply_factor(distractor3, sign, values_frac[2]*values_frac[3])
  distractor3 = dist3_factor[0]
  
  new_variable = start_factor("", values_str[2][0], values_str[2][1])
  new_variable = new_variable + variable
  if funcs[1] == '\\ln(x)' and values_frac[2].denominator != 1:
    new_variable = start_factor("", values_str[2][0], values_frac[2].numerator)
    new_variable = new_variable + variable
  
  answer = answer + derivatives_and_primitives[funcs[1]][0].replace('x', new_variable) + ans_factor[1]
  distractor1 = distractor1 + derivatives_and_primitives[funcs[1]][0].replace('x', new_variable) + dist1_factor[1]
  if funcs[1] == '\\ln(x)' and values_frac[2].denominator != 1:
    answer = answer.replace("\\frac{1}", "\\frac{" + str(values_frac[2].denominator) + "}")
    distractor1 = distractor1.replace("\\frac{1}", "\\frac{" + str(values_frac[2].denominator) + "}")
  distractor2 = distractor2 + funcs[1].replace('x', new_variable) + dist2_factor[1]
  distractor3 = distractor3 + funcs[1].replace('x', variable) + dist3_factor[1]

  answers = [answer, distractor1, distractor2, distractor3]
  print_question("1211","dérivées",2,[],question,answers)

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
theme = 3
Ntermes = 1
if theme == 3:
  Ntermes = 2
elif theme == 2 or theme == 6 or theme == 8 or theme == 9:
  Ntermes = random.SystemRandom(0).randint(2,3)
Nvalues = {1:3, 2:Ntermes*3, 3:Ntermes*3, 4:4, 5:3, 6:Ntermes*2, 7:4, 8:Ntermes*3, 9:1+Ntermes*2, 10:3}
Nfuncs = {1:1, 2:Ntermes, 3:Ntermes, 4:3, 5:2, 6:0, 7:0, 8:Ntermes, 9:1, 10:1}
possible_funcs = ['e^{x}','\\cos(x)','\\sin(x)','\\ln(x)']
variables = ["x","y","z","t","n","m","r","\\theta","\\phi","\\nu","\\mu","\\epsilon","\\varepsilon","\\varphi","\\alpha","\\beta","\\gamma","\\eta","chien","chat","banane"]

variable = variables[random.SystemRandom(0).randint(0,len(variables)-1)]
values_str = []
values_frac = []
funcs = []

for i in range(0,Nvalues[theme]):
  frac = fractions.Fraction(random.SystemRandom(0).randint(1,10), random.SystemRandom(0).randint(1,10))
  num = frac.numerator
  denum = frac.denominator
  sign = random.SystemRandom(0).randint(0,1)
  if sign == 1:
    sign = "-"
  else:
    sign = ""
  if denum == 1 and num != 1:
    values_str.append([sign,str(num)])
    values_frac.append(num)
  elif denum == num:
    values_str.append([sign,"1"])
    values_frac.append(1)
  else:
    values_str.append([sign,"\\frac{"+str(num)+"}{"+str(denum)+"}"])
    values_frac.append(frac)
    
for i in range(0,Nfuncs[theme]):
  funcs.append(possible_funcs[random.SystemRandom(0).randint(0,len(possible_funcs)-1)])
  
theme_3(values_str, values_frac, funcs, variable)

