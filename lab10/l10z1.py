#zadanie 1 Paweł Gałka
from scipy.optimize import linprog
import numpy as np

#y1, y2, y0, maksymalizacja
c = np.array([-3, -4, 0])

A = np.array([[1, 2, -500],
     [1, 1, -350],
     [-2, -1, 600],
     [1, 2, 0],
     [-1, -2, 0]])

b = np.array([0, 0, 0, 1, -1])

res = linprog(c, A, b).x

print('A =', res[0]/res[2])

print('B =', res[1]/res[2])
