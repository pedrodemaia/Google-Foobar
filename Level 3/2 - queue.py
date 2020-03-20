# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:33:59 2020

@author: pedro
"""

def solution(start, length):
    # Your code here
    
    # return xor from 1 to n
    def getXOR(n):
        return [n, 1, n+1, 0][n%4]
    
    result = 0
    for i in range(length):
        # get first and last workers of current line
        initial = start + i*length
        final = start + (i+1)*length - i - 1
        
        # xor for numbers [lower,upper] equals xor([1,lower-1],[1,upper])
        result ^= getXOR(initial-1) ^ getXOR(final)
        
    return result
        
        
    