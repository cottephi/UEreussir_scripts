import random

def print_question(SF, theme, level, dependances, question, answers):
  tags = ["true", "false", "false", "false"]
  index = [0, 1, 2, 3]
  random.shuffle(index)
  output = "\\begin{question}{" + SF + "}{"+theme+"}{"+str(level)+"}"
  if len(dependances) == 0:
    output = output + "{/}\n    "
  else:
    output = output + "{"
    for dep in dependances:
      output = output + str(dep) + ","
    output = output[:-1] + "}\n    "
  output = output + question + "\n\\end{question}\n\n\\begin{reponses}"
  for i in range(0,len(tags)):
    output = output + "\n    \\item[" + tags[index[i]]+"] " + answers[index[i]]
  output = output + "\n\\end{reponses}\n"

  print(output)
  
