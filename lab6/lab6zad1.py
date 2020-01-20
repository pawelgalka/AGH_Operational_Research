#Paweł Gałka
import numpy as np

matrix  = np.matrix([[20,-150,-250], [150,-80,-100], [250,100,40]])

strategyAresult = matrix.min(1).max(0)[0][0]

strategyA = np.where(matrix == strategyAresult)[0] + 1

strategyBresult = matrix.max(0).min(1)[0][0]

strategyB = np.where(matrix == strategyBresult)[1] + 1

print('Strategy A', strategyA)
print('Strategy B', strategyB)