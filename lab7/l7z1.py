#Zadanie 1 Paweł Gałka
from scipy.optimize import linprog
import numpy as np
np.set_printoptions(precision=3)

#f(x) = 2*x_1 + x_2 + 3*x_3 -> max więc -f(x) -> min
# A*x <= b

goal_function_coeff = [-2,-1,-3]
constraints_matrix = [[1,1,1],[-1,-1,-1],[-1,-2,-1],[0,2,1]]
constraints_values = [30, -30,-10,20]

result = linprog(goal_function_coeff, A_ub=constraints_matrix, b_ub=constraints_values)

print("Result parameters", result.x)