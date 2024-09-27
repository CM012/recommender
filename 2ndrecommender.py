import numpy as np
from scipy import linalg

A = np.array([[5, 3, 4], 
              [2, 2, 6], 
              [2, 1, 3]])
y = np.array([50, 40, 110])
Y = y.T

x = np.linalg.solve(A, Y)
print(x)
