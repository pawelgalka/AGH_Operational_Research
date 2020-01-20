#zadanie 3 Paweł Gałka

import numpy
from scipy.optimize import linprog

#f(x) = 0.1*x1 + 0.2*x2 + 0.2*x3 + 0.3*x4 + 0.4*x5 + 0*x6 -> min
#4*x1 + 1*x2 + 8*x3 + 5*x4 + 2*x5 + 0*x6 = 12000
#0*x1 + 1*x2 + 0*x3 + 1*x4 + 2*x5 + 3*x6 = 18000

A = numpy.array([
        [4,1,8,5,2,0],
        [-4,-1,-8,-5,-2,0],
        [0,1,0,1,2,3],
        [ 0, -1,  0, -1, -2, -3]])

b = [12000,-12000,18000,-18000]

#bo f(x) -> min => -f(x) -> max
c = [-0.1, -0.2, -0.2, -0.3, -0.4, -0. ]

#dualny problem
A_dual = numpy.transpose(A)

b_dual = numpy.transpose(c)

c_dual = numpy.transpose(b)

#bo ogr. A_dual*y >= b_dual
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

print('[0.5m, 1.4m]')
for i in range(len(primal_solution)):
    print(A[::2,A_indexes[i]], round(primal_solution[i],2),'m')
