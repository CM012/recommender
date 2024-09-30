import numpy as np 
from scipy.optimize import minimize
import argparse

parser = argparse.ArgumentParser(description='The differences in intakes')
parser.add_argument('-c', '-carbon', type=float, default=100, help='Difference in the targeted carb intake') #Carbon
parser.add_argument('-p', '-protein', type=float, default=20, help='Difference in the targeted protein intake') #Protein
parser.add_argument('-f', '-fat', type=float, default=20, help='Difference in the targeted fat intake') #Fat
parser.add_argument('--NS', action='store_true', help='Difference in the targeted fat intake') #Without Sweetpotato
parser.add_argument('--NR', action='store_true', help='Difference in the targeted fat intake') #Without Wedlentils
parser.add_argument('--NA', action='store_true', help='Difference in the targeted fat intake') #Without Avocado
args = parser.parse_args()

# Nutrition Weights Matrix
# [         sweetpotato redlentils  avocado ]
# [ carbon                                  ]
# [ protein                                 ]
# [ fat                                     ]
W = np.array([[0 if args.NS else 20, 0 if args.NR else 20.1, 0 if args.NA else 9], 
              [0 if args.NS else 1.45, 0 if args.NR else 9.02, 0 if args.NA else 2], 
              [0 if args.NS else 0, 0 if args.NR else 0.38, 0 if args.NA else 15]])
print(W)

# Nutrition Target Matrix
# [ carbon  protein  fat ]
y = np.array([args.c, args.p, args.f])
n = len(y)
print(y)

# Nutrition Weights Matrix
# [ sweetpotato redlentils  avocado ]
fun = lambda x: np.linalg.norm(np.dot(W, x) - y)
sol = minimize(fun, np.zeros(n), method='L-BFGS-B', bounds=[(0.,None) for x in range(n)])
x = sol['x']
# res = np.linalg.solve(W, y, assume_a='pos', overwrite_a=True, overwrite_b=True, check_finite=False) 
print(x)
print(W @ x)