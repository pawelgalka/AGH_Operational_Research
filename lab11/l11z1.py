#zadanie 1 Paweł Gałka

from cvxopt import matrix, solvers
import numpy
# biblioteka cvxopt minimalizuje formę kwadratową f = (1/2)x^T*P*x + q^T*x
# przekształcając funkcje celu dostaje nastepujace macierze P,q
P = matrix(numpy.array([[20.0, 4.0], [4.0, 2.0]]))
q = matrix([-10.0,-25.0])

#ograniczenia Gx <= h
G = matrix(numpy.array([[1.0,2.0], #x1 + 2x2 <= 10
                       [-1.0,-1.0], #-x1 -x2 <= -9
                       [-1.0,0], #x1 <=0 
                       [0,-1.0]])) #x2 <= 0
h = matrix([10.0,-9.0,0.0,0.0])
 
sol=solvers.qp(P, q, G, h)

sol_x = list(sol['x'])

[print('x'+str(ind),'=',x) for ind, x in enumerate(sol_x)]