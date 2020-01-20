#zadanie_2 Paweł Gałka

import numpy
from scipy.stats.mstats import gmean

A = numpy.matrix([[1, 7, 3], [1/7, 1, 2], [1/3, 1/2, 1]])
B = numpy.matrix([[1, 1/5, 7, 1], [5, 1, 1/2, 2], [1/7, 2, 1, 3], [1, 1/2, 1/3, 1]])
C = numpy.matrix([[1, 2, 5, 1, 7], [1/2, 1, 3, 1/2, 5], [1/5, 1/3, 1, 1/5, 2], [1, 2, 5, 1, 7], [1/7, 1/5, 1/2, 1/7, 1]])

def get_matrix_rank(matrix):
    rank=[]
    (size_x,size_y) = matrix.shape
    for i in range(size_y):
        rank.append(gmean(matrix[i],axis=1).item(0))
    return numpy.transpose(numpy.matrix(rank))/numpy.matrix(rank).sum()

#indeks Satty'ego
def satty(matrix):
    x_size, y_size = matrix.shape

    eigen_val, eigen_vec = numpy.linalg.eig(matrix)
    max_eigen_val = max(eigen_val)
    return numpy.real((max_eigen_val-x_size)/(x_size-1))


#indeks geometryczny
def geometric(matrix):
    x_size, y_size = matrix.shape

    rank = get_matrix_rank(matrix) 
    matrix_e = numpy.matrix(numpy.zeros((x_size,y_size)))
    for i in range(matrix_e.shape[0]):
        for j in range(matrix_e.shape[1]):
            matrix_e.itemset((i,j),(matrix.item(i,j)*rank.item(j)/rank.item(i)))
    
    matrix_log = numpy.square(numpy.log10(matrix_e))
    matrix_sum = 0
    for i in range(x_size):
        for j in range (i+1,y_size):
            matrix_sum += matrix_log.item(i,j)
    return 2/((x_size-1)*(x_size-2))*matrix_sum

 
#indeks Koczkodaja    
def koczkodaj(matrix):
    x_size, y_size = matrix.shape
        
    def index(triple):
        (i,j,k) = triple
        return matrix.item(i,k)*matrix.item(k,j)/matrix.item(i,j)
    
    triples = [(i,j,k) for i in range(x_size) for j in range(x_size) for k in range(x_size)]
    indexes = [min(abs(1-index(i)),1-1/index(i)) for i in triples]
    return max(indexes)



print("Satty:")
print("A:",satty(A))
print("B:",satty(B))
print("C:",satty(C))
print("Geometric:")
print("A:",geometric(A))
print("B:",geometric(B))
print("C:",geometric(C))   
print("Koczkodaj:")
print("A:",koczkodaj(A))
print("B:",koczkodaj(B))
print("C:",koczkodaj(C)) 