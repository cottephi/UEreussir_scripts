python scripts to generate QCM questions. The output is in LateX format, and only needs to be copied/pasted. Will requier the appropriate question and answer commands.

To generate a question, run:
  python3 vectors.py
or
  python3 scalar_product.py
or
  python3 powers_of_ten.py difficulty
where difficulty should be an integer. It will determine the number of terms in the formula to compute.

To generate 100 questions, run:
  100_vectors.sh
or 
  100_scalar_products.sh
or
  100_powers_of_ten.sh difficulty
Only works on UNIX systems (like linux). If you do not have a linux system... install one :)
  
The output will be placed in the txt file which name corresponds to the exercice type.

vectors.py will generate a question where two elements of the vector are given among x, y, r and theta, and the other two are to be found. It can display (randomly) the question with a graph or not (in that case the value of r is limited to 3).

scalar_products.py will generate 2 vectors and give either both their x and y or both their r and theta. Again, they will randomly be diplayed in a graph. The goal is, of course, to compute the scalar product

r is a random integer between 2 and 50 and the angle theta is a fraction of pi corresponding to the particular values on the trigo circle. It can go above 2pi but can not be negative (I might implement this feature in the futur)

powers_of_ten.py will generate a fraction, whose numerator contains a product of N terms and the denominator a product of M terms, both N and M chosen randomly between 1 and difficulty. Each term is of the form a*10^b, where a and b are integers, a is chosen randomly between 1 and 9 and b is chosen randomly between -10 and 10. The goal is to simplify the fraction.
