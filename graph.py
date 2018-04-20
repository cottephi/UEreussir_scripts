def graph(x,y,r,stheta,ftheta):
  value_to_use_x = ""
  value_to_use_y = ""
  value_to_use_r = ""
  if stheta == "\\pi" or stheta == "-\\pi":
    return
    value_to_use_r = "yes"
    value_to_use_x = "-1"
    value_to_use_y = "0"
  if stheta == "\\2pi" or stheta == "0":
    return
    value_to_use_r = "yes"
    value_to_use_x = "1"
    value_to_use_y = "0"
  if stheta == "\\pi/2" or stheta == "-\\3pi/2":
    return
    value_to_use_r = "yes"
    value_to_use_x = "0"
    value_to_use_y = "1"
  if stheta == "-\\pi/2" or stheta == "\\3pi/2":
    return
    value_to_use_r = "yes"
    value_to_use_x = "0"
    value_to_use_y = "-1"
  output = "\\begin{tikzpicture}[scale=3, axis/.style={->,blue,thick}, vector/.style={-stealth,red,very thick}, vector guide/.style={dashed,red,thick}]\n    "
  output = output + "\\coordinate[label=below  left:O] (O) at (0cm,0cm);\n    "
  output = output + "\\coordinate[label=below  left:] (x) at (1cm,0cm);\n    "
  output = output + "\\draw[axis] (0,0) -- (1,0) node[anchor=north east]{$x$};\n    "
  output = output + "\\draw[axis] (0,0) -- (0,1) node[anchor=north west]{$y$};\n    "
  if x !=0 and y !=0:
    output = output + "\\draw[-Stealth] (O) to [\"$\overrightarrow{OM}$\",sloped] ++ ({atan("+str(y)+"/"+str(x)+"}:{sqrt("+str(x**2)+"+"+str(y**2)+")}) coordinate[label=above right:M] (M);\n    "
    output = output + "\\draw[densely dotted] (O) to [\""+str(x)+"\" \'] ++ (0:"+str(x)+") coordinate (Mx);\n    "
    output = output + "\\draw[densely dotted] (Mx) to [\""+str(y)+"\" \'] ++ (90:"+str(y)+");\n    "
    output = output + "\\pic [\"$\\theta$\", draw, angle radius = 12mm, angle eccentricity=1.3] {angle = x--O--M};\n"
  elif x !=0 and stheta !="":
    if value_to_use_r == "yes":
      value_to_use_r = str(x)
    else:
      value_so_use_r = str(x)+"/cos("+str(ftheta)+")"
    if value_to_use_y == "":
       value_to_use_y = str(x)+"*tan("+str(ftheta)+")"
    else:
      value_to_use_y = value_to_use_y+"*"+value_to_use_r
    output = output + "\\draw[-Stealth] (O) to [\"$\overrightarrow{OM}$\",sloped] ++ ("+str(ftheta)+":{"+value_so_use_r+")}) coordinate[label=above right:M] (M);\n    "
    output = output + "\\draw[densely dotted] (O) to [\""+str(x)+"\" \'] ++ (0:"+str(x)+") coordinate (Mx);\n    "
    output = output + "\\draw[densely dotted] (Mx) to [\"$M_y$\" \'] ++ (90:{"+value_to_use_y+"});\n    "
    if ftheta > 0:
      output = output + "\\pic [\"$"+stheta+"$\", draw, angle radius = 12mm, angle eccentricity=1.3] {angle = x--O--M};\n"
    else:
      output = output + "\\pic [\"$"+stheta+"$\", draw, angle radius = 12mm, angle eccentricity=1.3] {angle = M--O--x};\n"
  elif y !=0 and stheta !="":
    if value_to_use_r == "yes":
      value_to_use_r = str(y)
    else:
      value_so_use_r = str(y)+"/sin("+str(ftheta)+")"
    if value_to_use_x == "":
       value_to_use_x = str(y)+"/tan("+str(ftheta)+")"
    else:
      value_to_use_x = value_to_use_x+"*"+value_to_use_r
    output = output + "\\draw[-Stealth] (O) to [\"$\overrightarrow{OM}$\",sloped] ++ ("+str(ftheta)+":{"+value_so_use_r+")}) coordinate[label=above right:M] (M);\n    "
    output = output + "\\draw[densely dotted] (O) to [\"$M_x$\" \'] ++ (0:{"+value_to_use_x+"}) coordinate (Mx);\n    "
    output = output + "\\draw[densely dotted] (Mx) to [\""+str(y)+"\" \'] ++ (90:"+str(y)+");\n    "
    if ftheta > 0:
      output = output + "\\pic [\"$"+stheta+"$\", draw, angle radius = 12mm, angle eccentricity=1.3] {angle = x--O--M};\n"
    else:
      output = output + "\\pic [\"$"+stheta+"$\", draw, angle radius = 12mm, angle eccentricity=1.3] {angle = M--O--x};\n"
  elif r !=0 and stheta !="":
    if value_to_use_x == "":
       value_to_use_x = str(r)+"*cos("+str(ftheta)+")"
    if value_to_use_y == "":
       value_to_use_y = str(r)+"*sin("+str(ftheta)+")"
    output = output + "\\draw[-Stealth] (O) to [\""+str(r)+"\",sloped] ++ ("+str(ftheta)+":"+str(r)+") coordinate[label=above right:M] (M);\n    "
    output = output + "\\draw[densely dotted] (O) to [\"$M_x$\" \'] ++ (0:{"+value_to_use_x+"}) coordinate (Mx);\n    "
    output = output + "\\draw[densely dotted] (Mx) to [\"$M_y$\" \'] ++ (90:{"+value_to_use_y+"});\n    "
    if ftheta > 0:
      output = output + "\\pic [\"$"+stheta+"$\", draw, angle radius = 12mm, angle eccentricity=1.3] {angle = x--O--M};\n"
    else:
      output = output + "\\pic [\"$"+stheta+"$\", draw, angle radius = 12mm, angle eccentricity=1.3] {angle = M--O--x};\n"
  elif r !=0 and x !=0:
    output = output + "\\draw[-Stealth] (O) to [\""+str(r)+"\",sloped] ++ ({acos("+str(x)+")/"+str(r)+"}:"+str(r)+") coordinate[label=above right:M] (M);\n    "
    output = output + "\\draw[densely dotted] (O) to [\""+str(x)+"\" \'] ++ (0:"+str(x)+") coordinate (Mx);\n    "
    output = output + "\\draw[densely dotted] (Mx) to [\"$M_y$\" \'] ++ (90:{sqrt("+str(r**2)+"-"+str(x**2)+")});\n    "
    output = output + "\\pic [\"$\\theta$\", draw, angle radius = 12mm, angle eccentricity=1.3] {angle = x--O--M};\n"
  elif r !=0 and y !=0:
    output = output + "\\draw[-Stealth] (O) to [\""+str(r)+"\",sloped] ++ ({asin("+str(y)+")/"+str(r)+"}:"+str(r)+") coordinate[label=above right:M] (M);\n    "
    output = output + "\\draw[densely dotted] (O) to [\"$M_x$\" \'] ++ (0:{sqrt("+str(r**2)+"-"+str(y**2)+")}) coordinate (Mx);\n    "
    output = output + "\\draw[densely dotted] (Mx) to [\""+str(y)+"\" \'] ++ (90:"+str(y)+");\n    "
    output = output + "\\pic [\"$\\theta$\", draw, angle radius = 12mm, angle eccentricity=1.3] {angle = x--O--M};\n"

  output = output + "\\end{tikzpicture}"
  print(output)
