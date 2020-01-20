#zadanie 2 Paweł Gałka

#ta metoda implementuje metodę węgierską
#https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.optimize.linear_sum_assignment.html
from scipy.optimize import linear_sum_assignment
from numpy import array,negative

#ostatnia kolumna oznacza że dany bank nie zostanie wybrany
cost = array([[5.6, 3.2, 4.4, 4.7, 0],
		[6, 3.5, 4.6, 4.5, 0],
		[0, 4, 5, 4.8, 0],
		[0, 3.8, 4.7, 4.8, 0],
		[4.8, 4, 4.5, 4.2, 0]])

#negative bo szukamy maximum
rows, cols = linear_sum_assignment(negative(cost))

index_type_dict = {0:"1d",1:"1m",2:"3m",3:"6m",4:"żadna"}
index_brand_dict = {0:"PKO BP",1:"PEKAO SA",2:"Millenium",3:"ING",4:"MBank"}

for i in range (0,len(cols)):
    print("W",index_brand_dict[i],"powinna zostać założona",index_type_dict[cols[i]],"lokata")
    
print("Zbiorcze oprocentowanie wyniesie",cost[rows,cols].sum())