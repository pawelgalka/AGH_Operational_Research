#zadanie 2 Paweł Gałka
from scipy.optimize import linprog
import numpy as np

dolar = 3.83

# x1 - lakierki
# x2 - sportowe

#y1, y2, y0, maksymalizacja
c = np.array([-150, -130, 0])

A = np.array([[2, 1, -9000],
              [1, 1, -5500],
              [1, 2.5, -10000],
              [-1, 0, 100],
              [0, -1, 100],
              [140/dolar, 250/dolar, 0],
              [-140/dolar, -250/dolar, 0]])

b = np.array([0, 0, 0, 0, 0, 1, -1])

res = linprog(c, A, b).x

print('Lakierki',round(res[0]/res[2]))
print('Sportowe',round(res[1]/res[2]))