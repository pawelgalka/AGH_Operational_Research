#zadanie_3 Paweł Gałka
import numpy

def get_weight(matrix):
    w, v = numpy.linalg.eig(matrix)
    current = w[0]
    vector = v[:,0]
    vector_normalized = vector/vector.sum()

    for i in range(1,len(w)):
        if numpy.isreal(w[i]) and current<w[i]:
            current = w[i]
            vector =  v[:,i]
            vector_normalized = vector/vector.sum()
    return numpy.real(current),numpy.real(vector_normalized)

def normalize2Subcat(v1,v2,vSubcat):
    matrix = v1*vSubcat.item(0)+v2*vSubcat.item(1)
    return matrix/matrix.sum()


matrixPrize = numpy.matrix([[1,1/5,3], [5,1,9], [1/3,1/9,1]])
matrixFuel = numpy.matrix([[1,3,1/3], [1/3,1,1/5],[3,5,1]])
matrixSafety = numpy.matrix([[1,5,1/5], [1/5,1,1/9],[5,9,1]])
matrixTrunk = numpy.matrix([[1,5,3], [1/5,1,1/2], [1/3,2,1]])
matrixPassengers = numpy.matrix([[1,1,3], [1,1,3], [1/3,1/3,1]])

matrixCost = numpy.matrix([[1,1/2],[2,1]])
matrixCapacity = numpy.matrix([[1,3], [1/3,1]])

matrixFinal = numpy.matrix([[1,1/3,2], [3,1,1/2], [1/2,2,1]])



wCost,vCost = get_weight(matrixCost)
wCapacity, vCapacity = get_weight(matrixCapacity)
wPrize,vPrize = get_weight(matrixPrize)
wFuel,vFuel = get_weight(matrixFuel)
wSafety,vSafety = get_weight(matrixSafety)
wTrunk,vTrunk = get_weight(matrixTrunk)
wPassengers,vPassengers = get_weight(matrixPassengers)

rankCost = normalize2Subcat(vPrize,vFuel,vCost)
rankCapacity = normalize2Subcat(vTrunk,vPassengers,vCapacity)


wC,vC = get_weight(matrixFinal)

R = numpy.concatenate([rankCost,vSafety,rankCapacity]).reshape(3,3).transpose()*vC

print('vector Prize',vPrize)
print('vector Fuel',vFuel)
print('vector Cost',rankCost)
print('vector Safety',vSafety)
print('vector Trunk',vTrunk)
print('vector Passengers',vPassengers)
print('vector Capacity',rankCapacity)
print('vector Matrix Final',vC)
print('rank',R)

