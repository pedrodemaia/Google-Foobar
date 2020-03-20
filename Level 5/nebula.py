# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 09:54:09 2020

@author: pedro
"""


# Case 1
g = [[True, False, True], 
     [False, True, False], 
     [True, False, True]]
output = 4

# Case 2
g = [[True, False, True, False, False, True, True, True], 
     [True, False, True, False, False, False, True, False], 
     [True, True, True, False, False, False, True, False], 
     [True, False, True, False, False, False, True, False], 
     [True, False, True, False, False, True, True, True]]
output = 254

# Case 3
g = [[True, True, False, True, False, True, False, True, True, False], 
     [True, True, False, False, False, False, True, True, True, False], 
     [True, True, False, False, False, False, False, False, False, True], 
     [False, True, False, False, False, False, True, True, False, False]]
output = 11567

from collections import defaultdict

# get next step for row r1 considering the lower row r2
def getResult(r1, r2, nCols):
    c11 = r1 >> 1 # upper row [:-1] 
    c12 = r1 & ~(1 << nCols) # upper row [1:]
    c21 = r2 >> 1  # lower row [:-1]
    c22 = r2 & ~(1 << nCols) # lower row [1:]
    
    return (c11 & ~c12 & ~c21 & ~c22) | (~c11 & c12 & ~c21 & ~c22) | \
        (~c11 & ~c12 & c21 & ~c22) | (~c11 & ~c12 & ~c21 & c22)

def solution(g):
    rows, cols = len(g), len(g[0])
    # transpose g to improve performance operating on lowest dimension
    if cols > rows:
        g = list(zip(*g))
        rows, cols = cols, rows
    
    # binary representation of each row
    rowSum = [sum(1 << i for i, c in enumerate(row) if c) for row in g]
    
    # get all combinations that generate the existing rows
    uniqueRows = set(rowSum)
    maxNumber = (1 << cols + 1)
    possibilities = defaultdict(set)
    for r1 in range(maxNumber):
        for r2 in range(maxNumber):
            # get generated row from each pair of rows
            result = getResult(r1, r2, cols)
            # check if generated row belongs to final rows
            if result in uniqueRows:
                # any next row r2 transforms current row r1 into result
                possibilities[(result, r1)].add(r2)
                
    # check combined possible combinations for every pair of rows
    previous = {i : 1 for i in range(maxNumber)}
    for row in rowSum:
        nextRow = defaultdict(int)
        for c in previous:
            for p in possibilities[(row,c)]:
                nextRow[p] += previous[c]
        previous = nextRow
        
    return sum(previous.values())