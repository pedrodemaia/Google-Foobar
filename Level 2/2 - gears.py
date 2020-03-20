#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:11:27 2020

@author: pedro
"""
#import numpy as np

def solution(pegs):
    def zeros_matrix(n):
        return [[0.0 for i in range(n)] for j in range(n)]
    
    n = len(pegs)
    
    invA = zeros_matrix(n)
    b = [pegs[i+1]-pegs[i] for i in range(n-1)]
    b.append(0)
    
    #create inverse matrix
    divider = 3 if n%2 == 0 else 1
    
    for i in range(n-1):
        for j in range(n-1):
            if i == j:
                val = 2
            elif i > j:
                val = 1 if (i+j+n%2)%2 == 1 else -1
            else:
                val = 2 if (i+j)%2 == 0 else -2
            invA[i][j] = val
      
    # create last row and col
    for i in range(n-1):
        invA[-1][i] = 1 if i%2 == 0 else -1
        invA[i][-1] = 1 if (i+n%2)%2 == 0 else -1
    invA[-1][-1] = -1
        
# =============================================================================
#     A = zeros_matrix(n)
#    
#     # relationship between adjacent gears
#     for i in range(n-1):
#         A[i][i] = 1.0
#         A[i][i+1] = 1.0
#     
#     # relationship between first and last gears
#     A[-1][0] = 1.0
#     A[-1][-1] = -2.0
#     Ainv = np.linalg.inv(A)
# =============================================================================

    
    gears = [sum(invA[i][j]*b[j] for j in range(n)) for i in range(n)]
        
    if any(g < divider for g in gears):
        return -1, -1
    
    if gears[0]%divider == 0:
        return gears[0]/divider, 1
    return gears[0], divider