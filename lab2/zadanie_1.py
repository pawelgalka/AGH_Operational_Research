#zadanie_1 Paweł Gałka
import numpy

def get_weight(matrix):
    w, v = numpy.linalg.eig(matrix)
    current = w[0]
    vector = v[:,0]
    vector_normalized = vector/vector.sum()

    for i in range(1,len(w)):
        if numpy.isreal(w[i]) and current<w[i]:
            current = w[i]
            vector = numpy.real(v[:,i])
            vector_normalized = vector/vector.sum()
    return numpy.real(current),numpy.real(vector_normalized)


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


w1,v1 = get_weight(matrix1)
w2,v2 = get_weight(matrix2)
w3,v3 = get_weight(matrix3)
w4,v4 = get_weight(matrix4)
w5,v5 = get_weight(matrix5)
w6,v6 = get_weight(matrix6)
w7,v7 = get_weight(matrix7)
w8,v8 = get_weight(matrix8)
wC,vC = get_weight(matrixC)

R = numpy.concatenate([v1,v2,v3,v4,v5,v6,v7,v8]).reshape(8,3).transpose()*vC
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
