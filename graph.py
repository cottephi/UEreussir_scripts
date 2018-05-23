def graph(sx = "", sy = "", fx = 0, fy = 0, r = 0, stheta = "", ftheta = 0, method = "", origin = "O", end = "M", xpoint = "x", ypoint = "y"):
  if method == "":
    return
  value_to_use_x = ""
  value_to_use_y = ""
  value_to_use_r = ""
  fx2 = 0
  fy2 = 0
  fr2 = 0
  fx2 = int(fx*fx*100)/100
  fy2 = int(fy*fy*100)/100
  fr2 = int(r*r*100)/100
  output = "\\begin{tikzpicture}[scale=3, axis/.style={->,blue,thick}, vector/.style={-stealth,red,very thick}, vector guide/.style={dashed,red,thick}]\n    "
  output = output + "\\coordinate[label=below  left:O] (" + origin + ") at (0cm,0cm);\n    "
  output = output + "\\coordinate[label=below  left:] (x) at (1cm,0cm);\n    "
  output = output + "\\draw[axis] (0,0) -- (1,0) node[anchor=north east]{$x$};\n    "
  output = output + "\\draw[axis] (0,0) -- (0,1) node[anchor=north west]{$y$};\n    "
  sign = ""
  #if fx*fy < 0:
    #sign = "-"
    
#######################################################################
  if method == "xy":
    output = output + "\\draw[-Stealth] (" + origin + ") to [] ++ (" + str(ftheta) + ":" + sign + str(r) + ") coordinate[label=above right:" + end + "] (" + end + ");\n    "
    if sx != "0" and sy != "0":
      output = output + "\\draw[densely dotted] (" + origin + ") to [\"$" + xpoint + "=" +sx+ "$\"] ++ (0:" +str(fx)+ ") coordinate (Mx);\n    "
      output = output + "\\draw[densely dotted] (Mx) to [\"$" + ypoint + "=" +sy+ "$\"] ++ (90:" +str(fy)+ ");\n    "
    else:
      output = output + "\\draw[densely dotted] (" + origin + ") to [] ++ (0:" +str(fx)+ ") coordinate (Mx);\n    "
      output = output + "\\draw[densely dotted] (Mx) to [] ++ (90:" +str(fy)+ ");\n    "
      output = output + "\\draw (1,1) node[right]{$" + xpoint + "=" +sx+ "$, $" + ypoint + "=" +sy+ "$ };\n    "
    if fx < r:
      if ftheta > 0:
        output = output + "\\pic [\"$\\theta$\", draw=red,->, angle radius = 12mm, angle eccentricity=1.3] {angle = x--" + origin + "--" + end + "};\n"
      else:
        output = output + "\\pic [\"$\\theta$\", draw=red,<-, angle radius = 12mm, angle eccentricity=1.3] {angle = " + end + "--" + origin + "--x};\n"
        
#######################################################################
  elif method == "xtheta":
    output = output + "\\draw[-Stealth] (" + origin + ") to [] ++ (" +str(ftheta)+ ":" +str(r)+ ") coordinate[label=above right:" + end + "] (" + end + ");\n    "
    if sx != "0" and sy != "0":
      output = output + "\\draw[densely dotted] (" + origin + ") to [\"$" + xpoint + "=" +sx+ "$\"] ++ (0:" +str(fx)+ ") coordinate (Mx);\n    "
      output = output + "\\draw[densely dotted] (Mx) to [\"$y$\"] ++ (90:" +str(fy)+ ");\n    "
      if ftheta > 0:
        output = output + "\\pic [\"$\\theta=" +stheta+ "$\", draw=red,->, angle radius = 12mm, angle eccentricity=1.3] {angle = x--" + origin + "--" + end + "};\n"
      else:
        output = output + "\\pic [\"$\\theta=" +stheta+ "$\", draw=red,<-, angle radius = 12mm, angle eccentricity=1.3] {angle = " + end + "--" + origin + "--x};\n"
    else:
      output = output + "\\draw[densely dotted] (" + origin + ") to [] ++ (0:" +str(fx)+ ") coordinate (Mx);\n    "
      output = output + "\\draw[densely dotted] (Mx) to [] ++ (90:" +str(fy)+ ");\n    "
      if fx < r:
        output = output + "\\draw (1,1) node[right]{$" + xpoint + "=" +sx+ "$};\n    "
        if ftheta > 0:
          output = output + "\\pic [\"$\\theta=" +stheta+ "$\", draw=red,->, angle radius = 12mm, angle eccentricity=1.3] {angle = x--" + origin + "--" + end + "};\n"
        else:
          output = output + "\\pic [\"$\\theta=" +stheta+ "$\", draw=red,<-, angle radius = 12mm, angle eccentricity=1.3] {angle = " + end + "--" + origin + "--x};\n"
      else:
        output = output + "\\draw (1,1) node[right]{$" + xpoint + "=" +sx+ "$, $\\theta=0$};\n    "
        
#######################################################################
  elif method == "ytheta":
    output = output + "\\draw[-Stealth] (" + origin + ") to [] ++ (" +str(ftheta)+ ":" +str(r)+ ") coordinate[label=above right:" + end + "] (" + end + ");\n    "
    if sx != "0" and sy != "0":
      output = output + "\\draw[densely dotted] (" + origin + ") to [\"$x$\"] ++ (0:" +str(fx)+ ") coordinate (Mx);\n    "
      output = output + "\\draw[densely dotted] (Mx) to [\"y=$" +sy+ "$\"] ++ (90:" +str(fy)+ ");\n    "
      if ftheta > 0:
        output = output + "\\pic [\"$\\theta=" +stheta+ "$\", draw=red,->, angle radius = 12mm, angle eccentricity=1.3] {angle = x--" + origin + "--" + end + "};\n"
      else:
        output = output + "\\pic [\"$\\theta=" +stheta+ "$\", draw=red,<-, angle radius = 12mm, angle eccentricity=1.3] {angle = " + end + "--" + origin + "--x};\n"
    else:
      output = output + "\\draw[densely dotted] (" + origin + ") to [] ++ (0:" +str(fx)+ ") coordinate (Mx);\n    "
      output = output + "\\draw[densely dotted] (Mx) to [] ++ (90:" +str(fy)+ ");\n    "
      if fx < r:
        output = output + "\\draw (1,1) node[right]{$" + ypoint + "=" +sy+ "$};\n    "
        if ftheta > 0:
          output = output + "\\pic [\"$\\theta=" +stheta+ "$\", draw=red,->, angle radius = 12mm, angle eccentricity=1.3] {angle = x--" + origin + "--" + end + "};\n"
        else:
          output = output + "\\pic [\"$\\theta=" +stheta+ "$\", draw=red,<-, angle radius = 12mm, angle eccentricity=1.3] {angle = " + end + "--" + origin + "--x};\n"
      else:
        output = output + "\\draw (1,1) node[right]{$" + ypoint + "=" +sy+ "$, $\\theta=0$};\n    "
        
#######################################################################
  elif method == "rtheta":
    if sx != "0" and sy != "0":
      output = output + "\\draw[-Stealth] (" + origin + ") to [\"$OM=" +str(r)+ "$\",sloped] ++ (" +str(ftheta)+ ":" +str(r)+ ") coordinate[label=above right:" + end + "] (" + end + ");\n    "
      output = output + "\\draw[densely dotted] (" + origin + ") to [\"$x$\"] ++ (0:" +str(fx)+ ") coordinate (Mx);\n    "
      output = output + "\\draw[densely dotted] (Mx) to [\"$y$\"] ++ (90:" +str(fy)+ ");\n    "
      if ftheta > 0:
        output = output + "\\pic [\"$\\theta=" +stheta+ "$\", draw=red,->, angle radius = 12mm, angle eccentricity=1.3] {angle = x--" + origin + "--" + end + "};\n"
      else:
        output = output + "\\pic [\"$\\theta=" +stheta+ "$\", draw=red,<-, angle radius = 12mm, angle eccentricity=1.3] {angle = " + end + "--" + origin + "--x};\n"
    else:
      output = output + "\\draw[-Stealth] (" + origin + ") to [] ++ (" +str(ftheta)+ ":" +str(r)+ ") coordinate[label=above right:" + end + "] (" + end + ");\n    "
      output = output + "\\draw[densely dotted] (" + origin + ") to [] ++ (0:" +str(fx)+ ") coordinate (Mx);\n    "
      output = output + "\\draw[densely dotted] (Mx) to [] ++ (90:" +str(fy)+ ");\n    "
      if fx < r:
        output = output + "\\draw (1,1) node[right]{$OM=" +str(r)+ "$};\n    "
        if ftheta > 0:
          output = output + "\\pic [\"$\\theta=" +stheta+ "$\", draw=red,->, angle radius = 12mm, angle eccentricity=1.3] {angle = x--" + origin + "--" + end + "};\n"
        else:
          output = output + "\\pic [\"$\\theta=" +stheta+ "$\", draw=red,<-, angle radius = 12mm, angle eccentricity=1.3] {angle = " + end + "--" + origin + "--x};\n"
      else:
        output = output + "\\draw (1,1) node[right]{$OM=" +str(r)+ "$, $\\theta=0$};\n    "
        
#######################################################################
  elif method == "xr":
    if sx != "0" and sy != "0":
      output = output + "\\draw[-Stealth] (" + origin + ") to [\"$OM=" +str(r)+ "$\",sloped] ++ (" +str(ftheta)+ ":" +str(r)+ ") coordinate[label=above right:" + end + "] (" + end + ");\n    "
      output = output + "\\draw[densely dotted] (" + origin + ") to [\"$" + xpoint + "=" +sx+ "$\"] ++ (0:" +str(fx)+ ") coordinate (Mx);\n    "
      output = output + "\\draw[densely dotted] (Mx) to [\"$y$\"] ++ (90:" +str(fy)+ ");\n    "
    else:
      output = output + "\\draw[-Stealth] (" + origin + ") to [] ++ (" +str(ftheta)+ ":" +str(r)+ ") coordinate[label=above right:" + end + "] (" + end + ");\n    "
      output = output + "\\draw[densely dotted] (" + origin + ") to [] ++ (0:" +str(fx)+ ") coordinate (Mx);\n    "
      output = output + "\\draw[densely dotted] (Mx) to [] ++ (90:" +str(fy)+ ");\n    "
      output = output + "\\draw (1,1) node[right]{$OM=" +str(r)+ "$, $" + xpoint + "=" +sx+ "$};\n    "
    if fx < r:
      if ftheta > 0:
        output = output + "\\pic [\"$\\theta$\", draw=red,->, angle radius = 12mm, angle eccentricity=1.3] {angle = x--" + origin + "--" + end + "};\n"
      else:
        output = output + "\\pic [\"$\\theta$\", draw=red,<-, angle radius = 12mm, angle eccentricity=1.3] {angle = " + end + "--" + origin + "--x};\n"
      
#######################################################################
  elif method == "yr":
    if sx != "0" and sy != "0":
      output = output + "\\draw[-Stealth] (" + origin + ") to [\"$OM=" +str(r)+ "$\",sloped] ++ (" +str(ftheta)+ ":" +str(r)+ ") coordinate[label=above right:" + end + "] (" + end + ");\n    "
      output = output + "\\draw[densely dotted] (" + origin + ") to [\"$x$\"] ++ (0:" +str(fx)+ ") coordinate (Mx);\n    "
      output = output + "\\draw[densely dotted] (Mx) to [\"$" + ypoint + "=" +sy+ "$\"] ++ (90:" +str(fy)+ ");\n    "
    else:
      output = output + "\\draw[-Stealth] (" + origin + ") to [] ++ (" +str(ftheta)+ ":" +str(r)+ ") coordinate[label=above right:" + end + "] (" + end + ");\n    "
      output = output + "\\draw[densely dotted] (" + origin + ") to [] ++ (0:" +str(fx)+ ") coordinate (Mx);\n    "
      output = output + "\\draw[densely dotted] (Mx) to [] ++ (90:" +str(fy)+ ");\n    "
      output = output + "\\draw (1,1) node[right]{$OM=" +str(r)+ "$, $" + ypoint + "=" +sy+ "$};\n    "
    if fx < r:
      if ftheta > 0:
        output = output + "\\pic [\"$\\theta$\", draw=red,->, angle radius = 12mm, angle eccentricity=1.3] {angle = x--" + origin + "--" + end + "};\n"
      else:
        output = output + "\\pic [\"$\\theta$\", draw=red,<-, angle radius = 12mm, angle eccentricity=1.3] {angle = " + end + "--" + origin + "--x};\n"

  output = output + "\\end{tikzpicture}"
  return output
