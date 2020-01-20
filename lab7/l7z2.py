#Zadanie 1 Paweł Gałka
from scipy.optimize import linprog
import numpy as np
np.set_printoptions(precision=3)

#f(x) = 8*x_1 + 4*x_2 -> max
# A*x <= b

goal_function_coeff = [8,4]
constraints_matrix = [[-5,-15],[-20,-5],[15,2]]
constraints_values = [-50, -40, 60]

result = linprog(goal_function_coeff, A_ub=constraints_matrix, b_ub=constraints_values)

print("Result parameters", result.x)