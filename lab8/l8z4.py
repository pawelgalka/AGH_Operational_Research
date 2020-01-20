#zadanie 4 Paweł Gałka

import numpy
from scipy.optimize import linprog

#f(x) = 0*x1 + 3*x2 + 1*x3 + 1*x4 + 4*x5 + 2*x6 + 0*x7 + 3*x8 + 4*x9 -> min
#2*x1 + 1*x2 + 1*x3 + 0*x4 + 0*x5 + 0*x6 + 0*x7 + 2*x8 + 1*x9= 12000
#1*x1 + 2*x2 + 1*x3 + 3*x4 + 2*x5 + 1*x6 + 0*x7 + 0*x8 + 0*x9= 24000
#0*x1 + 0*x2 + 2*x3 + 1*x4 + 2*x5 + 4*x6 + 6*x7 + 1*x8 + 3*x9= 27000

A = numpy.array([[2, 1, 1, 0, 0, 0, 0, 2, 1],
[-2, -1, -1, 0, 0, 0, 0, 0, 0],
[1, 2, 1, 3, 2, 1, 0, 1, 3],
[-1, -2, -1, -3, -2, -1, 0, -2, -1],
[0, 0, 2, 1, 2, 4, 6, 0, 0],
[ 0, 0, -2, -1, -2, -4, -6, -1, 3]])

b = [12000, -12000, 24000, -24000, 27000, -27000]

c = numpy.array([ 0, -3, -1, -1, -4, -2, 0, -3, -4])

A_dual = numpy.transpose(A)

b_dual = numpy.transpose(c)

c_dual = numpy.transpose(b)

result = linprog(c_dual,-A_dual,-b_dual)
x = list(result.x)

#sprawdz ograniczenia problemu dualnego

res_x = {}
for i in range(len(A_dual)):
    RHS = round(b_dual[i],3)
    LHS = round(sum([A_dual[i][j] * x[j] for j in range(len(x))]),3)
    if (LHS > RHS): #zerowanie tej zmiennej
        res_x[i] = 0
        
A_indexes = list(filter(lambda x : x not in res_x.keys(), numpy.arange(0,len(A[0]))))
A_primal = []
for i in range(len(A)):
    A_primal.append([A[i][j] for j in A_indexes])

primal_solution = numpy.linalg.lstsq(A_primal, b,rcond=1)[0]

print('f_min',abs(result.fun),'m')

print('[11cm, 8cm, 5cm]')
for i in range(len(primal_solution)):
    print(A[::2,A_indexes[i]], round(primal_solution[i],2),'m')