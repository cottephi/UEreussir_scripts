import random
from print_question import *

p = 1000 # number of significant numbers




# function to format to LaTeX

def Sci(significand,power):
    significand = arrond(significand,p)
    if significand == int(significand):
        significand = int(significand)
    if power == 0:
        return significand
    else:
        return str(significand) + " \\times 10^{"+ str(int(power)) + "}"

def formula(NumberOfNumerator, NumberOfDenominator, NumeratorSignificands, DenominatorSignificands, NumeratorPowers, DenominatorPowers):
    result = "\\frac{"
    for i in range(NumberOfNumerator):
        result += Sci(NumeratorSignificands[i],NumeratorPowers[i]) + " \\times "
    result = result[:-8] + "}{"
    for i in range(NumberOfDenominator):
        result += Sci(DenominatorSignificands[i],DenominatorPowers[i]) + " \\times "
    result = result[:-8] + "}"
    return result




def arrond(n,m):
    """
    return n with m significant numbers
    """
    n = float(n)
    s = abs(int(n*m)*10-int(n*m*10))
    if s < 5:
        r = int(n*m)/m
    else:
        r = int((n*m)+(n/abs(n)))/m
    return r

def randPosNeg():
    """
    return -1 or +1 with 50%
    """
    return random.SystemRandom(0).randint(0,1)*2-1

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



##########################################################################################################################################################
###############################################################Program start##############################################################################
##########################################################################################################################################################


#init
N = random.SystemRandom(0).randint(1,4)
M = random.SystemRandom(0).randint(1,4)
a = [ random.SystemRandom(0).randint(1,9) for i in range(0,N) ] # Numerator   Significand Table
b = [ random.SystemRandom(0).randint(1,9) for i in range(0,M) ] # Denominator Significand Table
c = [ random.SystemRandom(0).randint(1,9) for i in range(0,N) ] # Numerator   Power       Table
d = [ random.SystemRandom(0).randint(1,9) for i in range(0,M) ] # Denominator Power       Table



# max p significant numbers ####################################################
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

################################################################################



# randomizing negatives numbers ################################################
for i in range(N):
    a[i] *= randPosNeg()
    c[i] *= randPosNeg()

for i in range(M):
    b[i] *= randPosNeg()
    d[i] *= randPosNeg()

# debuging the 2 awnser error (from the comit : b78af243e5e1bc39caed92f77f87f916fbfd4ab8)
while calc(a,b,c,d,sum,sub,sum,sub)[0]==0:
    for i in range(N):
        a[i] *= randPosNeg()
        c[i] *= randPosNeg()

    for i in range(M):
        b[i] *= randPosNeg()
        d[i] *= randPosNeg()
################################################################################




Question = "Que vaut $"+formula(N,M,a,b,c,d)+"$?"
Distractors = distractors(a,b,c,d)
Awnser = answer(a,b,c,d)


AllAwnsers = Distractors.append(Awnser)
AllAwnsers.reverse();

print_question("1211","Calcul",2,[9],Question,AllAwnsers)
















#
