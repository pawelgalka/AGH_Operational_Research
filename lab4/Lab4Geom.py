#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:32:46 2019

@author: galkpawe
"""
#Zadanie 1 Paweł Gałka
import numpy
import math  

#indeks Koczkodaja    
def koczkodaj(matrix):
    x_size, y_size = matrix.shape
        
    def index(triple):
        (i,j,k) = triple
        return matrix.item(i,k)*matrix.item(k,j)/matrix.item(i,j)
    
    triples = [(i,j,k) for i in range(x_size) for j in range(x_size) for k in range(x_size)]
    indexes = [min(abs(1-index(i)),1-1/index(i)) for i in triples]
    return max(indexes)

#warunek rozwiązania arytmetycznego
def check_if_solution_exists(matrix,index,n,k):
    value = index < 1 - (1+math.sqrt(4*(n-1)*(n-k-2)))/(2*(n-1))
    if (value):
        print('Matrix has a proper solution')
    else:
        print('Matrix has an unreliable solution')
    return value


def check_if_rearrangement_needed(matrix,known_dict):
    unknown_indexes =  numpy.array(list(filter(lambda a: a+1 not in list(known_dict.keys()), numpy.arange(matrix.shape[0]))))
    return (len(unknown_indexes)-1)*len(unknown_indexes)/2 != numpy.sum(unknown_indexes)

def rearranged_matrix(matrix,known_dict):
    rows_to_move = numpy.array([matrix[row] for row in range(len(matrix)) if row+1 in list(known_dict.keys())]) #indexing from 0
    matrix_with_rows_removed = numpy.delete(matrix, [x-1 for x in list(known_dict.keys())],0)
    matrix = numpy.concatenate((matrix_with_rows_removed, rows_to_move), axis=0)
    cols_to_move = numpy.transpose(numpy.array([matrix[:,col] for col in range(len(matrix)) if col+1 in list(known_dict.keys())])) #indexing from 0
    matrix_with_cols_removed = numpy.delete(matrix, [x-1 for x in list(known_dict.keys())],1)
    matrix = numpy.concatenate((matrix_with_cols_removed, cols_to_move), axis=1)
    return matrix

def calculate_b(matrix,known_values,i):
    return numpy.log10(numpy.prod(matrix[i]) * numpy.prod(known_values))

def geometric_rank(matrix,known_dict):
    known_values = numpy.array(list(known_dict.values()))
    k = known_values.shape[0]
    n = matrix.shape[0]
    
    if (check_if_rearrangement_needed(matrix,known_dict)):
        matrix = rearranged_matrix(matrix,known_dict)
        
    b_dash = [calculate_b(matrix,known_values,i) for i in range (0,n-k)]
    
    A_dash = (n)*numpy.identity(n-k) - numpy.ones((n-k,n-k))
    
    W_dash = numpy.linalg.solve(A_dash, b_dash)
    W = numpy.array([10**x for x in W_dash])

    for k in known_dict.keys():
       W = numpy.insert(W,k-1,known_dict[k])
    print('Geometric rank', W)
    
A = numpy.array([[1, 2/3, 2,  5/2, 5/3, 5], 
                       [3/2, 1, 3, 10/3, 3, 9], 
                       [1/2, 1/3, 1, 4/3, 7/8, 5/2], 
                       [2/5, 3/10, 3/4, 1, 5/6, 12/5], 
                       [3/5, 1/3, 8/7, 6/5, 1, 3], 
                       [1/5, 1/9, 2/5, 5/12, 1/3, 1]])       
known_A = {5:3, 6:1}

B = numpy.array([[1, 2/5, 3,  7/3, 1/2, 1], 
                       [5/2, 1, 4/7, 5/8, 1/3, 3], 
                       [1/3, 7/4, 1, 1/2, 2, 1/2], 
                       [3/7, 8/5, 2, 1, 4, 2], 
                       [2, 3, 1/2, 1/4, 1, 1/2], 
                       [1, 1/3, 2, 1/2, 2, 1]])       
known_B = {4:2, 5:1/2, 6:1}

C = numpy.array([[1, 17/4, 17/20, 8/5, 23/6, 8/3], 
                       [4/17, 1, 1/5, 2/5, 9/10, 2/3], 
                       [20/17, 5, 1, 21/10, 51/10, 10/3], 
                       [5/8, 5/2, 10/21, 1, 5/2, 11/6], 
                       [6/23, 10/9, 10/51, 2/5, 1, 19/30], 
                       [3/8, 3/2, 3/10, 6/11, 30/19, 1]]) 
known_C = {2:2, 4:5}

print('Matrix A')
geometric_rank(A,known_A)
print('Matrix B')
geometric_rank(B,known_B)
print('Matrix C')
geometric_rank(C,known_C)
