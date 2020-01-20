#zadanie 1 Paweł Gałka

import numpy
from scipy.optimize import linprog
numpy.set_printoptions

A = numpy.array([[1,3,2,3,1],
     [4,6,5,7,1]])

A_dual = numpy.transpose(A)

b = numpy.array([6,15])

c = numpy.array([2,5,3,4,1])

b_dual = numpy.transpose(c)

c_dual = numpy.transpose(b)

#constraints Ay >= b => do postaci -Ay <= -b

result = linprog(c_dual,-A_dual,-b_dual)
print(result.x)
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

primal_solution = numpy.linalg.solve(A_primal, b)

print('x1',primal_solution[0])
print('x2',primal_solution[1])
print('x3',0)
print('x4',0)
print('x5',0)

    
    