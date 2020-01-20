#Zadanie 3 Paweł Gałka
from scipy.optimize import linprog
import numpy as np


# 1 -> 1. reka 1, 2. reka 2
# 2 -> 1. reka 1, 2. reka 3
# 3 -> 1. reka 2, 2. reka 3
# 4 -> 1. reka 2, 2. reka 4

game_matrix = np.array([
    [0, 2, -3, 0],
    [-2, 0, 0, 3],
    [3, 0, 0, -4],
    [0, -3, 4, 0],
])

shift_value = abs(np.min(game_matrix))

#player A
#f(x) min (1/v)
#constraints -> iloczyn każdy z każdym kolumny >=1 -> do postaci <= -1
game_matrixA = -(game_matrix + shift_value).T 

constraints_values_A = [-1,-1,-1,-1]

goal_function_coeff = [1,1,1,1]

#wylicza x_i
gameA_result = linprog(goal_function_coeff, A_ub=game_matrixA, b_ub=constraints_values_A, options={"disp": True})

v_A = 1/sum(gameA_result.x)

#zamiana na p_i
probabilities_A = gameA_result.x*v_A
gameA_value = v_A - shift_value

print("Player A")
print("Probabilities A",probabilities_A)
print("Game value A %.2f"%gameA_value)

#player B
#f(x) max (1/v) -> min -f(x)
#constraints -> iloczyn każdy z każdym kolumny <=1
game_matrixB = (game_matrix + shift_value)

constraints_values_B = [1,1,1,1]

goal_function_coeff = [-1,-1,-1,-1]

#wylicza x_i
gameB_result = linprog(goal_function_coeff, A_ub=game_matrixB, b_ub=constraints_values_B,options={"disp":True})

v_B = 1/sum(gameB_result.x)

#zamiana na p_i
probabilities_B = gameB_result.x*v_B
gameB_value = v_B - shift_value

print("Player B")
print("Probabilities B",probabilities_B)
print("Game value B %.2f"%gameB_value)

