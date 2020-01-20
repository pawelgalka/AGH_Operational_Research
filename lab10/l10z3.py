#zadanie 3 Paweł Gałka

from scipy.optimize import linprog
import numpy as np
import math

#x1,x2, maksymalizacja
c = np.array([-23, -17])

A = np.array([[4, 3],
     [1, 1]])

b = np.array([190, 55])

max_fun = 0
max_params = []

def solve_task(bounds_param):
    global max_fun
    global max_params
    optimalization = linprog(c, A, b, bounds = bounds_param)
    fun_res = abs(optimalization.fun)
    res = optimalization.x
    x1 = round(res[0],2)
    x2 = round(res[1],2)
    
    if ('infeasible' in optimalization.message):
        return
    
    if (max_fun < fun_res and (x1.is_integer() and x2.is_integer())):
        max_fun = fun_res
        max_params = [x1, x2]
        return
    
    if (x1.is_integer()):
        upper = math.ceil(x2)
        lower = math.floor(x2)
        solve_task((bounds_param[0],(0,lower)))
        solve_task((bounds_param[0],(upper,None)))
    else:
        upper = math.ceil(x1)
        lower = math.floor(x1)
        solve_task(((0,lower),bounds_param[1]))
        solve_task(((upper,None),bounds_param[1]))
        
        
solve_task(((0, None), (0,None)))
print('Zysk', 23*max_params[0] + 17*max_params[1])
print('Łańcuszki', max_params[0])
print('Pierscionki', max_params[1])