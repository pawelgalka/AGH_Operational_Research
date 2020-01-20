#Zadanie 4 Paweł Gałka
from scipy.optimize import linprog
import numpy as np
np.set_printoptions(precision=3)

matrix = np.array([
        [-2,8,2],
        [3,-1,0]
        ])

shift_value = abs(np.min(matrix))

#playerA
#min f(x), Ax <= b
goal_function_coeff = [1,1]

matrixA = matrix + shift_value

#constraints >=1 -> <= -1
constraints_values_A = [-1,-1,-1]
constraintsA = -matrixA.T

gameA_result = linprog(goal_function_coeff, A_ub=constraintsA, b_ub=constraints_values_A)
v_A = 1/sum(gameA_result.x)

#zamiana na p_i
probabilities_A = gameA_result.x*v_A
gameA_value = v_A - shift_value

print("Player A")
print("Probabilities A",probabilities_A)
print("Game value A %.2f"%gameA_value)


#playerB
#max f(x) -> min -f(x)
goal_function_coeff = [-1,-1,-1]

matrixB = matrix + abs(np.min(matrix))

#constraints <= 1
constraints_values_B = [1,1]
constraintsB = matrixA.T.T

gameB_result = linprog(goal_function_coeff, A_ub=constraintsB, b_ub=constraints_values_B)
v_B = 1/sum(gameB_result.x)

#zamiana na p_i
probabilities_B = gameB_result.x*v_B
gameB_value = v_B - shift_value

print("Player B")
print("Probabilities B",probabilities_B)
print("Game value B %.2f"%gameB_value)
