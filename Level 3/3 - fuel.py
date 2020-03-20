# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 08:39:58 2020

@author: pedro
"""

def solution(m):
    def getFraction(x, error=0.00001):
        integer = int(x)
        x -= integer
        if x < error:
            return integer, 1
        elif 1 - error < x:
            return integer+1, 1
    
        # start with fraction between 0/1 and 1/1
        min_n = 0
        min_d = 1
        max_n = 1
        max_d = 1
        while True:
            n = min_n + max_n
            d = min_d + max_d
            if d * (x + error) < n:
                max_n = n
                max_d = d
            elif n < (x - error) * d:
                min_n = n
                min_d = d
            else:
                return (integer *d + n, d)
    
    def multMatrix(a,b):
        ra = len(a)
        ca = len(a[0])
        cb = len(b[0])
        
        return [[sum(a[i][k]*b[k][j] for k in range(ca)) 
                 for j in range(cb)] for i in range(ra)]
    
    def matrixPower(m,n):
        result = m
        for i in range(n-1):
            result = multMatrix(result,m)
        return result
    
    def getLCM(nums):
        lcm = max(nums)
        while True:
            if all([lcm%n == 0 for n in nums]):
                return lcm
            lcm += 1
            
    n = len(m)
    probMatrix = [[0 for i in range(n)] for j in range(n)]
    
    # transfrom matrix into probability
    terminal = []
    transient = []
    for i in range(n):
        s = sum(m[i])
        if s == 0:
            probMatrix[i][i] = 1
            terminal.append(i)
        else:
            probMatrix[i] = [float(j)/s for j in m[i]]
            transient.append(i)
    
    probs = matrixPower(probMatrix,1000)[0]
    
    nums = []
    dens = []
    for t in terminal:
        n, d = getFraction(probs[t])
        nums.append(n)
        dens.append(d)
        
    lcm = getLCM(dens)
    result = [nums[i]*lcm/dens[i] for i in range(len(nums))]
    result.append(lcm)
    
    return result
    