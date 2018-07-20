import random
from print_question import *

p = 1000 # number of significant numbers




# function to format to LaTeX

def Sci(significand,power):
    if significand == int(significand):
        significand = int(significand)
    if power == 0:
        return significand
    else:
        return "{0} \\times 10^{1}".format(significand,int(power))

def formula(NumberOfNumerator, NumberOfDenominator, NumeratorSignificands, DenominatorSignificands, NumeratorPowers, DenominatorPowers):
    result = "\\frac{"
    for i in range(NumberOfNumerator):
        result += Sci(NumeratorSignificands[i],NumeratorPowers[i]) + " \\times " 
    result = result[:-8] + "}{"    
    for i in range(NumberOfDenominator):
        result += Sci(DenominatorSignificands[i],DenominatorPowers[i]) + " \\times " 
    result = result[:-8] + "}" 
    return result



def prod(T):
    R = 1
    for e in T:
        R *= e
    return R

def div(T):
    return T[0]/T[1]

def sub(T):
    return T[0]-T[1]


def toSci(Significand, Power):  # exemple :  50*10^2 -> 5*10^3
    if Significand == 0:
        return [0, 0]
    else:
        while abs(Significand) >= 10:
            Significand /= 10
            Power += 1
        while abs(Significand) < 1:
            Significand *= 10
            Power -= 1
        return [Significand, Power]





def calc(NumeratorSignificands, DenominatorSignificands, NumeratorPowers, DenominatorPowers,f1,f2,f3,f4):
    return toSci(f2([f1(NumeratorSignificands),f1(DenominatorSignificands)]),f4([f3(NumeratorPowers),f3(DenominatorPowers)]))






def distractors(NumeratorSignificands, DenominatorSignificands, NumeratorPowers, DenominatorPowers):
    D = []
    # Distractor 1 :
    # + - + -
    (significand,power) = calc(NumeratorSignificands, DenominatorSignificands, NumeratorPowers, DenominatorPowers,sum,sub,sum,sub)
    D.append(Sci(significand,power))
    # Distractor 2 :
    # + - * /
    (significand,power) = calc(NumeratorSignificands, DenominatorSignificands, NumeratorPowers, DenominatorPowers,sum,sub,prod,div)
    D.append(Sci(significand,power))
    # Distractor 2 :
    # * / * /
    (significand,power) = calc(NumeratorSignificands, DenominatorSignificands, NumeratorPowers, DenominatorPowers,prod,div,prod,div)
    D.append(Sci(significand,power))
    return D

def answer(NumeratorSignificands, DenominatorSignificands, NumeratorPowers, DenominatorPowers):
    # Answer :
    # * / + -
    (significand,power) = calc(NumeratorSignificands, DenominatorSignificands, NumeratorPowers, DenominatorPowers,prod,div,sum,sub)
    return Sci(significand,power)







N = random.SystemRandom(0).randint(1,4)
M = random.SystemRandom(0).randint(1,4)
a = [ random.SystemRandom(0).randint(1,9) for i in range(0,N) ] # Numerator   Significand Table
b = [ random.SystemRandom(0).randint(1,9) for i in range(0,M) ] # Denominator Significand Table
c = [ random.SystemRandom(0).randint(1,9) for i in range(0,N) ] # Numerator   Power       Table
d = [ random.SystemRandom(0).randint(1,9) for i in range(0,M) ] # Denominator Power       Table



tmp = div([prod(a),prod(b)]) * p
while int(tmp) != tmp:
    a = [ random.SystemRandom(0).randint(1,9) for i in range(0,N) ]
    b = [ random.SystemRandom(0).randint(1,9) for i in range(0,M) ]
    tmp = div([prod(a),prod(b)]) * p


tmp = div([prod(c),prod(d)])
while int(tmp) != tmp:
    c = [ random.SystemRandom(0).randint(1,9) for i in range(0,N) ]
    d = [ random.SystemRandom(0).randint(1,9) for i in range(0,M) ]
    tmp = div([prod(c),prod(d)])




 # randomizing negatives numbers
 # (random.SystemRandom(0).randint(0,1)*2-1) = +1 or -1 at 50%
for i in range(N):
    a[i] *= (random.SystemRandom(0).randint(0,1)*2-1)
    c[i] *= (random.SystemRandom(0).randint(0,1)*2-1)

for i in range(M):
    b[i] *= (random.SystemRandom(0).randint(0,1)*2-1)
    d[i] *= (random.SystemRandom(0).randint(0,1)*2-1)






question = "Que vaut $"+formula(N,M,a,b,c,d)+"$?"





T = distractors(a,b,c,d)
T.append(answer(a,b,c,d))

print(question + "\n")

for e in T:
    print(e)




"""


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
"""
