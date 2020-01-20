#zadanie 1 Paweł Gałka

import numpy as np
import itertools

A = np.array([[1, 2/3, 2, 5/2, 5/3, 5], 
              [3/2, 1, 3, 10/3, 3, 9], 
              [1/2, 1/3, 1, 4/3, 7/8, 5/2], 
              [2/5, 3/10, 3/4, 1, 5/6, 12/5], 
              [3/5, 1/3, 8/7, 6/5, 1, 3], 
              [1/5, 1/9, 2/5, 5/12, 1/3, 1]])

B = np.array([[1, 2/5, 3, 7/3, 1/2, 1, 2], 
              [5/2, 1, 4/7, 1, 1, 3, 2/3], 
              [1/3, 7/4, 1, 1/2, 2, 1/2, 1], 
              [3/7, 1, 2, 1, 4, 2, 6], 
              [2, 1, 1/2, 1/4, 1, 1/2, 3/4], 
              [1, 1/3, 2, 1/2, 2, 1, 5/8], 
              [1/2, 3/2, 1, 1/6, 4/3, 8/5, 1]])

C = np.array([[1, 2/3, 2/15, 1, 8, 12/5, 1, 1/2], 
              [3/2, 1, 1, 2, 1, 2/3, 1/6, 1], 
              [15/2, 1, 1, 5/2, 7/8, 2, 1, 1/5],
              [1, 1/2, 2/5, 1, 4/3, 1, 2/7, 1],
              [1/8, 1, 8/7, 3/4, 1, 1/5, 2/7, 1],
              [5/12, 3/2, 1/2, 1, 5, 1, 3, 2],
              [1, 6, 1, 7/2, 7/2, 1/3, 1, 3/11],
              [2, 1, 5, 1, 1, 1/2, 11/3, 1]])

D = np.array([[0, 1, 1, -1, -1, 1, -1],
              [-1, 0, 0, 1, 1, -1, 0],
              [-1, 0, 0, 0, 1, 1, -1],
              [1, -1, 0, 0, 1, 0, 1],
              [1, 0, -1, -1, 0, 1, -1],
              [-1, 1, -1, 1, -1, 0, 0],
              [1, 0, 1, -1, 1, 0, 0]])

E = np.array([[0, 1, 0, 0, -1],
              [-1, 0, 0, 0, 1],
              [0, 0, 0, 1, 0],
              [0, 0, -1, 0, 0],
              [1, -1, 0, 0, 0]])

F = np.array([[0, -1, 1, -1, 1, -1, 1, -1, 1],
              [1, 0, 1, 1, 1, -1, -1, -1, -1],
              [-1, -1, 0, -1, 1, -1, 1, 1, 1],
              [1, -1, 1, 0, -1, 1, -1, 1, -1],
              [-1, -1, -1, 1, 0, -1, 1, 1, 1],
              [1, 1, 1, -1, 1, 0, -1, -1, -1],
              [-1, 1, -1, 1, -1, 1, 0, 1, -1],
              [1, 1, -1, -1, -1, 1, -1, 0, 1],
              [-1, 1, -1, 1, -1, 1, 1, -1, 0]])

def retrieve_name(obj):
    return [name for name in globals() if globals()[name] is obj]

def transform(item):
    return np.sign(item-1)

def to_general_tournament_matrix(matrix):
    return np.array([transform(i) for i in matrix])

def check_count_general_tournament_matrix(matrix):
    return np.all(np.array([(matrix[i,j] == -matrix[j,i]) for i in range(matrix.shape[0]) for j in range(matrix.shape[1])])) #if any inconsistency return false

def allows_ties(matrix):
    return np.any(np.array([(matrix[i,j] == 0 and i!=j) for i in range(matrix.shape[0]) for j in range(matrix.shape[1])]))

def count_0_directed(matrix,i,j,k):
    a = matrix[i,j]
    b = matrix[j,k]
    c = matrix[k,i]
    return a==0 and b==0 and c==0

def count_1_directed(matrix,i,j,k):
    a = matrix[i,j]
    b = matrix[j,k]
    c = matrix[k,i]
    return (not a and not b and c) or (not a and b and not c) or (a and not b and not c)

def count_2_directed(matrix,i,j,k):
    a = matrix[i,j]
    b = matrix[j,k]
    c = matrix[k,i]
    return (a == b and a and b and not c) or (a == c and a and not b and c) or (b == c and not a and b and c)

def count_3_directed(matrix,i,j,k):
    return matrix[i,j] == matrix[j,k] and matrix[j,k] == matrix[k,i] and matrix[i,j] != 0

def count_inconsistent_triads_3_directed(matrix):
    n = matrix.shape[0]
    return len([(i,j,k) for (i,j,k) in itertools.combinations(range(n), 3) if matrix[i,j] == matrix[j,k] and matrix[j,k] == matrix[k,i] and i!=j and j!=k and i!=k ])

def count_inconsistent_triads_general(matrix):
    n = matrix.shape[0]
    return len([(i,j,k) for (i,j,k) in itertools.combinations(range(n), 3) if count_1_directed(matrix,i,j,k) or count_2_directed(matrix,i,j,k) or count_3_directed(matrix,i,j,k) and i!=j and j!=k and i!=k])

def max_possible_inconsistent_triads_classic(matrix):
    n = matrix.shape[0]
    return ((n**3 - n)//24, (n**3 - 4*n)//24)[n//2 == 0]

def max_possible_inconsistent_triads_general(matrix):
    n = matrix.shape[0]
    if (n%4 == 0):
        return (13*n**3 - 24*n**2 - 16*n)/96
    elif (n%4 == 1):
        return (13*n**3 - 24*n**2 - 19*n + 30)/96
    elif (n%4 == 2):
        return (13*n**3 - 24*n**2 - 4*n)/96
    else:
        return (13*n**3 - 24*n**2 - 19*n + 18)/96
    
def classic_Kendall_index(matrix):
    return 1 - count_inconsistent_triads_3_directed(matrix)/max_possible_inconsistent_triads_classic(matrix)

def general_Kendall_index(matrix):
    return 1 - count_inconsistent_triads_general(matrix)/max_possible_inconsistent_triads_general(matrix)

A_general = to_general_tournament_matrix(A)
B_general = to_general_tournament_matrix(B)
C_general = to_general_tournament_matrix(C)

print('--Exercise 1--')
print('Matrix A')
print(A_general)
print('Matrix B')
print(B_general)
print('Matrix C')
print(C_general)

print('--Exercise 2--')
print('Matrix D')
print('General tournament matrix', check_count_general_tournament_matrix(D))
print('Matrix E')
print('General tournament matrix', check_count_general_tournament_matrix(E))
print('Matrix F')
print('General tournament matrix', check_count_general_tournament_matrix(F))

matrices = [A_general, B_general, C_general, D, E, F]
general_tournament_matrices_vals = [matrix for matrix in matrices if check_count_general_tournament_matrix(matrix)]
general_tournament_matrices_names = [retrieve_name(i)[0] for i in general_tournament_matrices_vals]
general_tournament_matrices = dict(zip(general_tournament_matrices_names, general_tournament_matrices_vals))

print('--Exercise 3--')
for (name,matrix) in general_tournament_matrices.items():
    print(name,'allows' if allows_ties(matrix) else 'does not allow','ties')

general_tournament_without_ties = dict(filter(lambda elem: not allows_ties(elem[1]), general_tournament_matrices.items())) 
  
print('--Exercise 4--')
for (name, matrix) in general_tournament_matrices.items():
    print('General Kendall index for',name)
    print(general_Kendall_index(matrix))

print('--Exercise 5--')
for (name, matrix) in general_tournament_without_ties.items():
    print('Classic Kendall index for',name)
    print(classic_Kendall_index(matrix))  
    