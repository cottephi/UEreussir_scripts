###########################################################################
################################authors####################################
#####  Philippe Cotte cottephi@gmail.com

python scripts to generate QCM questions. The output is in LateX format, ready to compile on overleaf  or sharelatex. To compile locally, please check you have the appropriate packages (check LateX_requierements.tex and look for the \usepackage commands)

To generate a question, run:
  python3 vectors.py
or
  python3 scalar_product.py
or
  python3 powers_of_ten.py
or
  python3 derivatives.py

To generate 100 questions, run:
  100.sh exercise
exercise being vectors, derivatives, powers_of_ten, or scalar_products
  
The output will be placed in the txt file which name corresponds to the exercice type.

vectors.py will generate a question where two elements of the vector are given among x, y, r and theta, and the other two are to be found. It can display (randomly) the question with a graph or not (in that case the value of r is limited to 3).

scalar_products.py will generate 2 vectors and give either both their x and y or both their r and theta. Again, they will randomly be diplayed in a graph. The goal is, of course, to compute the scalar product

r is a random integer between 2 and 50 and the angle theta is a fraction of pi corresponding to the particular values on the trigo circle. It can go above 2pi but can not be negative (I might implement this feature in the futur)

powers_of_ten.py will generate a fraction, whose numerator contains a product of N terms and the denominator a product of M terms, both N and M chosen randomly between 1 and 4. Each term is of the form a*10^b, where a and b are integers, a is chosen randomly between 1 and 9 and b is chosen randomly between -10 and 10. The goal is to simplify the fraction.

derivatives will choose randomly a "theme" (functions like cos, sin, exp, ln, or plynomials, or combinations of those... details are commented in derivatives.py), take random values for the different termes (all are rationnals), and random symbol for the variable. It uses sympy to solve the derivations and to generate distractor. Those will depend on the functions used.
