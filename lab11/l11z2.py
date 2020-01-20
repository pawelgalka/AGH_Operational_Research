#zadanie 2 Paweł Gałka

from cvxopt import matrix, solvers
import numpy

# model Markowitza przyjmuje do maksymalizacji formę kwadratową f = x^T*A*x
# biblioteka cvxopt minimalizuje formę kwadratową f = (1/2)x^T*P*x + q^T*x
# => P = -2*A, q=[0...0] ale funkcja kwadratowa g(x) ma max tam gdzie -g(x) ma min więc nie ma różnicy jaką macierz P wstawimy (2A czy -2A)
P = -2*matrix(numpy.array([[11.4312, 1.1701, 0.1232, 1.6619, 2.0254], 
            [1.1701,7.7723,0.4983,1.1374,1.7056],
            [0.1232,0.4983,5.1598,-1.3094,-0.6307],
            [1.6619,1.1374,-1.3094,20.2858,2.2824],
            [2.0254,1.7056,-0.6307,2.2824,4.3189]]), tc='d')
q = matrix(numpy.array([0,0,0,0,0]), tc='d')

# ograniczenia Gx <= h
G = matrix(numpy.array([[ -0.94, -1.20, 0.02, -0.81, -0.45], #suma akcji
            [ -1, 0, 0, 0, 0], #x1
            [ 0, -1, 0, 0, 0], #x2
            [ 0, 0, -1, 0, 0], #x3
            [ 0, 0, 0, -1, 0], #x4
            [ 0, 0, 0, 0, -1]])) #x5
h = matrix([-1.0,0,0,0,0,0])

# suma akcji sumuje się do 100% (1) -> Ax=b
A = matrix(1.0, (1,5))
b = matrix(1.0)

sol=solvers.qp(P,q, G, h,A,b)

sol_x = list(sol['x'])

[print('x'+str(ind),'=',x) for ind, x in enumerate(sol_x)]
