import random
import sys
import numpy as np
import fractions
import math
import pandas
from graph import *
from print_question import *

dict_stheta_vs_sxy = {"0":["1","0"], "1/6":["\\sqrt{3}/2", "\\frac{1}{2}"], "1/4":["\\sqrt{2}/2", "\\sqrt{2}/2"], "1/3":["\\frac{1}{2}", "\\sqrt{3}/2"], "1/2":["0","1"], "2/3":["-\\frac{1}{2}","\\sqrt{3}/2"], "3/4":["-\\sqrt{2}/2", "\\sqrt{2}/2"], "5/6":["-\\sqrt{3}/2", "\\frac{1}{2}"], "1":["-1","0"], "-1/6":["\\sqrt{3}/2", "-\\frac{1}{2}"], "-1/4":["\\sqrt{2}/2", "-\\sqrt{2}/2"], "-1/3":["\\frac{1}{2}", "-\\sqrt{3}/2"], "-1/2":["0","-1"], "-2/3":["-\\frac{1}{2}","-\\sqrt{3}/2"], "-3/4":["-\\sqrt{2}/2", "-\\sqrt{2}/2"], "-5/6":["-\\sqrt{3}/2", "-\\frac{1}{2}"], "-1":["-1","0"]}
dict_stheta_vs_fxy = {"0":[1,0], "1/6":[math.sqrt(3)/2., 0.5], "1/4":[math.sqrt(2)/2., math.sqrt(2)/2.], "1/3":[0.5, math.sqrt(3)/2.], "1/2":[0,1], "2/3":[-0.5,math.sqrt(3)/2.], "3/4":[-math.sqrt(2)/2., math.sqrt(2)/2.], "5/6":[-math.sqrt(3)/2., 0.5], "1":[-1,0], "-1/6":[math.sqrt(3)/2., -0.5], "-1/4":[math.sqrt(2)/2., -math.sqrt(2)/2.], "-1/3":[0.5, -math.sqrt(3)/2.], "-1/2":[0,-1], "-2/3":[-0.5,-math.sqrt(3)/2.], "-3/4":[-math.sqrt(2)/2., -math.sqrt(2)/2.], "-5/6":[-math.sqrt(3)/2., -0.5], "-1":[-1,0]}


df_stheta_vs_xy = pandas.DataFrame({
'theta':['0', '1/6', '1/4', '1/3', '1/2', '2/3', '3/4', '5/6', '1', '-1/6', '-1/4', '-1/3', '-1/2', '-2/3', '-3/4', '-5/6', '-1'],
'str':[  ["1","0"], ["\\sqrt{3}/2", "\\frac{1}{2}"], ["\\sqrt{2}/2", "\\sqrt{2}/2"], ["\\frac{1}{2}", "\\sqrt{3}/2"], ["0","1"], ["-\\frac{1}{2}","\\sqrt{3}/2"], ["-\\sqrt{2}/2", "\\sqrt{2}/2"], ["-\\sqrt{3}/2", "\\frac{1}{2}"], ["-1","0"], ["\\sqrt{3}/2", "-\\frac{1}{2}"], ["\\sqrt{2}/2", "-\\sqrt{2}/2"], ["\\frac{1}{2}", "-\\sqrt{3}/2"], ["0","-1"], ["-\\frac{1}{2}","-\\sqrt{3}/2"], ["-\\sqrt{2}/2", "-\\sqrt{2}/2"], ["-\\sqrt{3}/2", "-\\frac{1}{2}"], ["-1","0"]  ],
'float':[  [1,0], [math.sqrt(3)/2., 0.5], [math.sqrt(2)/2., math.sqrt(2)/2.], [0.5, math.sqrt(3)/2.], [0,1], [-0.5,math.sqrt(3)/2.], [-math.sqrt(2)/2., math.sqrt(2)/2.], [-math.sqrt(3)/2., 0.5], [-1,0], [math.sqrt(3)/2., -0.5], [math.sqrt(2)/2., -math.sqrt(2)/2.], [0.5, -math.sqrt(3)/2.], [0,-1], [-0.5,-math.sqrt(3)/2.], [-math.sqrt(2)/2., -math.sqrt(2)/2.], [-math.sqrt(3)/2., -0.5], [-1,0]  ]
})
df_stheta_vs_xy = df_stheta_vs_xy.set_index('theta')


def get_all(method):
  
  sx = ["","","",""]
  sy = ["","","",""]
  fx = [0,0,0,0]
  fy = [0,0,0,0]
  r = [0,0,0,0]
  stheta = ["","","",""]
  key_stheta = ["","","",""]
  ftheta = [0,0,0,0]
  ftheta_nopi = [0,0,0,0]
  rmax = 50
  theta_denoms = ["1","2","3","4","6"]
  mult = [1,1,2,3]
  if method == "graph":
    rmax = 3
  r[0] = random.SystemRandom(0).randint(2,rmax)
  theta_denom_i = random.SystemRandom(0).randint(0,4)
  theta_denom = theta_denoms[theta_denom_i]
  theta_num = random.SystemRandom(0).randint(0,12)
  
  ftheta_nopi[0] = fractions.Fraction(theta_num,int(theta_denom))
  if ftheta_nopi[0]%2 == 0:
   ftheta_nopi[0] = 0
   ftheta[0] = 0
  else:
    ftheta[0] = int(100*float(180*theta_num)/float(theta_denom))/100
  
  if ftheta_nopi[0].numerator == 0:
    stheta[0] = "0"
  elif ftheta_nopi[0].denominator == 1:
    if ftheta_nopi[0].numerator == 1:
      stheta[0] = "\\pi"
    else:
      stheta[0] = str(ftheta_nopi[0].numerator)+"\\pi"
  elif ftheta_nopi[0].numerator == 1:
      stheta[0] = "\\pi/"+str(ftheta_nopi[0].denominator)
  else:
    stheta[0] = str(ftheta_nopi[0].numerator)+"\\pi/"+str(ftheta_nopi[0].denominator)
  
  while ftheta_nopi[0] >= 2:
    ftheta_nopi[0] = ftheta_nopi[0] - 2
  if ftheta_nopi[0] > 1:
    ftheta_nopi[0]  = fractions.Fraction(ftheta_nopi[0].numerator-2*ftheta_nopi[0].denominator,ftheta_nopi[0].denominator)
  if ftheta_nopi[0].numerator == 0:
    key_stheta[0] = "0"
  elif ftheta_nopi[0].denominator == 1:
    key_stheta[0] = str(ftheta_nopi[0].numerator)
  else:
    key_stheta[0] = str(ftheta_nopi[0].numerator)+"/"+str(ftheta_nopi[0].denominator)

  sx[0],sy[0] = df_stheta_vs_xy.loc[str(key_stheta[0]),'str']
  fx[0],fy[0] = df_stheta_vs_xy.loc[str(key_stheta[0]),'float']
  index_theta = df_stheta_vs_xy.index.get_loc(str(key_stheta[0]))
  
  for j in range(1,4):
    r[j] = int(r[0]*mult[random.SystemRandom(0).randint(0,3)])
    jtheta = str(df_stheta_vs_xy.index.tolist()[(index_theta+j)%17])
    if len(jtheta.split("/")) > 1:
      jnum,jdenom = jtheta.split("/")
      if jnum == '1' or jnum == '-1':
        stheta[j] = "\\pi/"+jdenom
        ftheta[j] = int(100*180/float(jdenom))/100
      else:
        stheta[j] = jnum + "\\pi/"+jdenom
        ftheta[j] = int(100*180*float(jnum)/float(jdenom))/100
    else:
      if jtheta == '1' or jtheta == '-1':
        stheta[j] = "\\pi"
        ftheta[j] = int(100*180)/100
      elif jtheta == '0':
        stheta[j] = "0"
        ftheta[j] = 0
      else:
        stheta[j] = jtheta + "\\pi"
        ftheta[j] = int(100*180*float(jtheta))/100
    sx[j],sy[j] = df_stheta_vs_xy.iloc[(index_theta+j)%17]['str']
    fx[j],fy[j] = df_stheta_vs_xy.iloc[(index_theta+j)%17]['float']
  
  for j in range(0,4):
    if sx[j] == "\\frac{1}{2}":
      sx[j] = str(fractions.Fraction(r[j],2))
    elif sx[j] == "-\\frac{1}{2}":
      sx[j] = str(fractions.Fraction(-r[j],2))
    elif sx[j] == "0":
      sx[j] = "0"
    elif sx[j] == "1":
      sx[j] = str(r[j])
    elif sx[j] == "-1":
      sx[j] = "-"+str(r[j])
    else:
      jnum,jdenom = sx[j].split("/")
      sign = ""
      if "-" in sx[j]:
        sign = "-"
        jnum = jnum[1:]
      sx[j] = fractions.Fraction(r[j],int(jdenom))
      if sx[j].denominator != 1 and sx[j].numerator != 1:
        sx[j] = sign+str(sx[j].numerator)+str(jnum)+"/"+str(sx[j].denominator)
      elif sx[j].denominator == 1 and sx[j].numerator != 1:
        sx[j] = sign+str(sx[j].numerator)+str(jnum)
      elif sx[j].denominator != 1 and sx[j].numerator == 1:
        sx[j] = sign+str(jnum)+"/"+str(sx[j].denominator)
      elif sx[j].denominator == 1 and sx[j].numerator == 1:
        sx[j] = sign+str(jnum)
        
    if sy[j] == "\\frac{1}{2}":
      sy[j] = str(fractions.Fraction(r[j],2))
    elif sy[j] == "-\\frac{1}{2}":
      sy[j] = str(fractions.Fraction(-r[j],2))
    elif sy[j] == "0":
      sy[j] = "0"
    elif sy[j] == "1":
      sy[j] = str(r[j])
    elif sy[j] == "-1":
      sy[j] = "-"+str(r[j])
    else:
      jnum,jdenom = sy[j].split("/")
      sign = ""
      if "-" in sy[j]:
        sign = "-"
        jnum = jnum[1:]
      sy[j] = fractions.Fraction(r[j],int(jdenom))
      if sy[j].denominator != 1 and sy[j].numerator != 1:
        sy[j] = sign+str(sy[j].numerator)+str(jnum)+"/"+str(sy[j].denominator)
      elif sy[j].denominator == 1 and sy[j].numerator != 1:
        sy[j] = sign+str(sy[j].numerator)+str(jnum)
      elif sy[j].denominator != 1 and sy[j].numerator == 1:
        sy[j] = sign+str(jnum)+"/"+str(sy[j].denominator)
      elif sy[j].denominator == 1 and sy[j].numerator == 1:
        sy[j] = sign+str(jnum)

    fx[j] = r[j]*fx[j]
    fy[j] = r[j]*fy[j]
    fx[j] = int(fx[j]*100)/100
    fy[j] = int(fy[j]*100)/100
  
  return [r, sx, sy, fx, fy, stheta, ftheta]

difficulty = 1
if len(sys.argv) == 2:
  difficulty = int(sys.argv[1])
  

methods = ["coord","graph"]
method = methods[random.SystemRandom(0).randint(0,1)]
initials = ["xy","xr","yr","xtheta","ytheta","rtheta"]
initial = initials[random.SystemRandom(0).randint(0,5)]

r, sx, sy, fx, fy, stheta, ftheta = get_all(method)

question = ""
true = ""
distractor1 = ""
distractor2 = ""
distractor3 = ""


if initial == "xy":
  if method == "coord":
    question = "Un vecteur a pour coordonnées $(" + sx[0] + "," + sy[0] + ")$. Que valent l'angle $\\theta$ (entre le vecteur et l'axe des $x$) et le rayon $OM$ de ce vecteur?"
  else:
    question = "Parmis les valeurs ci-dessous, lesquelles peuvent être égales à l'angle $\\theta$ (entre le vecteur et l'axe des $x$) et le rayon $OM$ du vecteur $\\vec{OM}$? \\\\ \n" + graph( sx[0], sy[0], fx[0], fy[0], r[0], stheta[0], ftheta[0], initial)
  true = "$OM$ = " + str(r[0]) + " et $\\theta$ = $" + stheta[0] + "$"
  distractor1 = "$OM$ = " + str(r[1]) + " et $\\theta$ = $" + stheta[1] + "$"
  distractor2 = "$OM$ = " + str(r[2]) + " et $\\theta$ = $" + stheta[2] + "$"
  distractor3 = "$OM$ = " + str(r[3]) + " et $\\theta$ = $" + stheta[3] + "$"    
  
#######################################################################
if initial == "xr":
  if method == "coord":
    question = "Un vecteur a pour coordonnées $(" + sx[0] + ",y)$ et pour rayon " + str(r[0]) + ". Que valent l'angle $\\theta$ (entre le vecteur et l'axe des $x$) et la coordonnée $y$ de ce vecteur?"
  else:
    question = "Parmis les valeurs ci-dessous, lesquelles peuvent être égales à l'angle $\\theta$ (entre le vecteur et l'axe des $x$) et la coordonnée $y$ du vecteur $\\vec{OM}$? \\\\ \n" + graph( sx[0], sy[0], fx[0], fy[0], r[0], stheta[0], ftheta[0], initial)
  true = "$y$ = $" + sy[0] + "$ et $\\theta$ = $" + stheta[0] + "$"
  distractor1 = "$y$ = $" + sy[1] + "$ et $\\theta$ = $" + stheta[1] + "$"
  distractor2 = "$y$ = $" + sy[2] + "$ et $\\theta$ = $" + stheta[2] + "$"
  distractor3 = "$y$ = $" + sy[3] + "$ et $\\theta$ = $" + stheta[3] + "$"
    
#######################################################################
if initial == "yr":
  if method == "coord":
    question = "Un vecteur a pour coordonnées $(x, " + sy[0] + ")$ et pour rayon " + str(r[0]) + ". Que valent l'angle $\\theta$ (entre le vecteur et l'axe des $x$) et la coordonnée $x$ de ce vecteur?"
  else:
    question = "Parmis les valeurs ci-dessous, lesquelles peuvent être égales à l'angle $\\theta$ (entre le vecteur et l'axe des $x$) et la coordonnée $x$ du vecteur $\\vec{OM}$? \\\\ \n" + graph( sx[0], sy[0], fx[0], fy[0], r[0], stheta[0], ftheta[0], initial)
  true = "$x$ = $" + sx[0] + "$ et $\\theta$ = $" + stheta[0] + "$"
  distractor1 = "$x$ = $" + sx[1] + "$ et $\\theta$ = $" + stheta[1] + "$"
  distractor2 = "$x$ = $" + sx[1] + "$ et $\\theta$ = $" + stheta[2] + "$"
  distractor3 = "$x$ = $" + sx[1] + "$ et $\\theta$ = $" + stheta[3] + "$"
    
#######################################################################
if initial == "xtheta":
  if method == "coord":
    question = "Un vecteur a pour coordonnées $(" + sx[0] + ", y)$ et pour angle $\\theta$ (entre le vecteur et l'axe des $x$) $" + stheta[0] + "$. Que valent le rayon $OM$ et la coordonnée $y$ de ce vecteur?"
  else:
    question = "Que valent le rayon $OM$ et la coordonnée $y$ du vecteur $\\vec{OM}$ ci-dessous? \\\\ \n" + graph( sx[0], sy[0], fx[0], fy[0], r[0], stheta[0], ftheta[0], initial)
  true = "$y$ = $" + sy[0] + "$ et $OM$ = " + str(r[0])
  distractor1 = "$y$ = $" + sy[1] + "$ et $OM$ = " + str(r[1])
  distractor2 = "$y$ = $" + sy[2] + "$ et $OM$ = " + str(r[2])
  distractor3 = "$y$ = $" + sy[3] + "$ et $OM$ = " + str(r[3])
    
#######################################################################
if initial == "ytheta":
  if method == "coord":
    question = "Un vecteur a pour coordonnées $(x, " + sy[0] + ")$ et pour angle $\\theta$ (entre le vecteur et l'axe des $x$) $" + stheta[0] + "$. Que valent le rayon $OM$ et la coordonnée $x$ de ce vecteur?"
  else:
    question = "Que valent le rayon $OM$ et la coordonnée $x$ du vecteur $\\vec{OM}$ ci-dessous? \\\\ \n" + graph( sx[0], sy[0], fx[0], fy[0], r[0], stheta[0], ftheta[0], initial)
  true = "$x$ = $" + sx[0] + "$ et $OM$ = " + str(r[0])
  distractor1 = "$x$ = $" + sx[1] + "$ et $OM$ = " + str(r[1])
  distractor2 = "$x$ = $" + sx[2] + "$ et $OM$ = " + str(r[2])
  distractor3 = "$x$ = $" + sx[3] + "$ et $OM$ = " + str(r[3])
    
#######################################################################
if initial == "rtheta":
  if method == "coord":
    question = "Un vecteur a pour rayon " + str(r[0]) + " et pour angle $\\theta$ (entre le vecteur et l'axe des $x$) $" + stheta[0] + "$. Que valent les coordonnées $x$ et $y$ de ce vecteur?"
  else:
    question = "Que valent les coordonnées $x$ et $y$ du vecteur $\\vec{OM}$ ci-dessous? \\\\ \n" + graph( sx[0], sy[0], fx[0], fy[0], r[0], stheta[0], ftheta[0], initial)
  true = "$x$ = $" + sx[0] + "$ et $y$ = $" + sy[0] + "$"
  distractor1 = "$x$ = $" + sx[1] + "$ et $y$ = $" + sy[1] + "$"
  distractor2 = "$x$ = $" + sx[2] + "$ et $y$ = $" + sy[2] + "$"
  distractor3 = "$x$ = $" + sx[3] + "$ et $y$ = $" + sy[3] + "$"
    
answers = [true, distractor1, distractor2, distractor3]
tags = ["true", "false", "false", "false"]
index = [0, 1, 2, 3]
random.shuffle(index)

print_question("/","Vecteurs",0,[1217,31,1213],question,tags,index,answers)

