#zadanie_2 Paweł Gałka
import numpy

def get_weight(matrix):
    w1, v1 = numpy.linalg.eig(matrix)
    current = w1[0]
    vector = v1[:,0]
    vector_normalized = vector/vector.sum()

    for i in range(1,len(w1)):
        if numpy.isreal(w1[i]) and current<w1[i]:
            current = w1[i]
            vector =  v1[:,i]
            vector_normalized = vector/vector.sum()
    return numpy.real(current),numpy.real(vector_normalized)

matrixPrize = numpy.matrix([[1,1/5,3,5], [5,1,7,9], [1/3,1/7,1,3],[1/5,1/9,1/3,1]])
matrixFood = numpy.matrix([[1,1,7,4],[1,1,7,4],[1/7,1/7,1,1/3],[1/4,1/4,3,1]])
matrixDistance = numpy.matrix([[1,6,1/5,1/9],[1/6,1,1/7,1/9],[5,7,1,1/3],[9,9,3,1]])
matrixParklot = numpy.matrix([[1,1/9,1,1/9],[9,1,9,1],[1,1/9,1,1/9],[9,1,9,1]])


matrixC = numpy.matrix([[1,5,3,4],
                        [1/5,1,4,1],
                        [1/3,1/4,1,2],
                        [1/4,1,1/2,1]])



w1,v1 = get_weight(matrixPrize)
w2,v2 = get_weight(matrixFood)
w3,v3 = get_weight(matrixDistance)
w4,v4 = get_weight(matrixParklot)
wC,vC = get_weight(matrixC)

R = numpy.concatenate([v1,v2,v3,v4]).reshape(4,4).transpose()*vC

print('vector Prize',v1)
print('vector Food',v2)
print('vector Distance',v3)
print('vector Parklot',v4)
print('vector Final',vC)
print('rank',R)
