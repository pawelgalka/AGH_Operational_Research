#zadanie 2 Paweł Gałka

#ta metoda implementuje metodę węgierską
#https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.optimize.linear_sum_assignment.html
from scipy.optimize import linear_sum_assignment
from numpy import array

cost = array([[0.8,0.8,0.8,0.6,0.6,0.6],
              [2.0,2.0,2.0,1.5,1.5,1.5],
              [0.7,0.7,0.7,0.6,0.6,0.6],
              [0.4,0.4,0.4,0.2,0.2,0.2],
              [0.2,0.2,0.2,0.4,0.4,0.4],
              [0.3,0.3,0.3,0.5,0.5,0.5]])

rows, cols = linear_sum_assignment(cost)

brand_to_index_dict = {0:"P1",1:"P1",2:"P1",3:"P2",4:"P2",5:"P2"}

for i in range (0,len(cols)):
    print("Zadanie",i+1,"powinien wykonać",brand_to_index_dict[cols[i]])
    
print("Czas zadań będzie wynosił",cost[rows,cols].sum())

