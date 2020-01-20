#zadanie_1 Paweł Gałka

import numpy 
from scipy.stats.mstats import gmean

matrix1 = numpy.matrix([[1, 1/7, 1/5], [7, 1, 3], [5, 1/3, 1]])
matrix2 = numpy.matrix([[1, 5, 9], [1/5, 1, 4], [1/9, 1/4, 1]])
matrix3 = numpy.matrix([[1, 4, 1/5], [1/4, 1, 1/9], [5, 9, 1]])
matrix4 = numpy.matrix([[1, 9, 4],[1/9, 1, 1/4], [1/4, 4, 1]])
matrix5 = numpy.matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
matrix6 = numpy.matrix([[1, 6, 4], [1/6, 1, 1/3], [1/4, 3, 1]])
matrix7 = numpy.matrix([[1,9,6], [1/9,1,1/3], [1/6,3,1]])
matrix8 = numpy.matrix([[1,1/2,1/2],[2,1,1],[2,1,1]])


matrixC = numpy.matrix([[1,4,7,5,8,6,6,2],
                        [1/4,1,5,3,7,6,6,1/3],
                        [1/7,1/5,1,1/3,5,3,3,1/5],
                        [1/5,1/3,3,1,6,3,4,1/2],
                        [1/8,1/7,1/5,1/6,1,1/3,1/4,1/7],
                        [1/6,1/6,1/3,1/3,3,1,1/2,1/5],
                        [1/6,1/6,1/3,1/4,4,2,1,1/5],
                        [1/2,3,5,2,7,5,5,1]])



def get_matrix_rank(matrix):
    rank=[]
    (size_x,size_y) = matrix.shape
    for i in range(size_y):
        rank.append(gmean(matrix[i],axis=1).item(0))
    return numpy.transpose(numpy.matrix(rank))/numpy.matrix(rank).sum()
        
v1 = get_matrix_rank(matrix1)
v2 = get_matrix_rank(matrix2)
v3 = get_matrix_rank(matrix3)
v4 = get_matrix_rank(matrix4)
v5 = get_matrix_rank(matrix5)
v6 = get_matrix_rank(matrix6)
v7 = get_matrix_rank(matrix7)
v8 = get_matrix_rank(matrix8)
vC = get_matrix_rank(matrixC)

R = numpy.concatenate([v1,v2,v3,v4,v5,v6,v7,v8]).reshape(8,3).transpose()*vC

old_R = numpy.matrix([[0.34634713],[0.36914035],[0.28451251]])

print('vector 1',v1)
print('vector 2',v2)
print('vector 3',v3)
print('vector 4',v4)
print('vector 5',v5)
print('vector 6',v6)
print('vector 7',v7)
print('vector 8',v8)
print('vector Final',vC)
print('rank',R)
print('old rank',old_R)
print('error MSE',(numpy.square(R-old_R)).mean())
