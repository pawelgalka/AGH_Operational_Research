#zadanie 1 Paweł Gałka

#ta metoda implementuje metodę węgierską
#https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.optimize.linear_sum_assignment.html
from scipy.optimize import linear_sum_assignment
from numpy import array

cost = array([[5,7,8,7],
              [6,4,7,6],
              [7,5,6,5],
              [4,3,5,9]])

rows, cols = linear_sum_assignment(cost)

brand_to_index_dict = {0:"Ford",1:"Volkswagen",2:"Toyota",3:"Fiat"}

for i in range (0,len(cols)):
    print("Warsztat",i+1,"powinien naprawiać",brand_to_index_dict[cols[i]])
    
print("Czas naprawy będzie wynosił",cost[rows,cols].sum())

