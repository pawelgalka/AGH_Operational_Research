#zadanie 2 Paweł Gałka

import numpy
from scipy.optimize import linprog

#problem kanoniczny
#f(x) = 10*A + 14*B + 8*C + 11*D -> max
#0.5*A + 0.4*B + 0.4*C + 0.2*D <= 2000
#0.4*A + 0.2*B + 0*C + 0.5*D <= 2800
#A,B,C,D>=0

A = numpy.array([
        [0.5, 0.4, 0.4, 0.2],
        [0.4, 0.2, 0, 0.5]])

b = numpy.array([2000,2800])

c = numpy.array([10,14,8,11])

#problem dualny

A_dual = numpy.transpose(A)

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

print('x1',0)
print('x2',primal_solution[0])
print('x3',0)
print('x4',primal_solution[1])