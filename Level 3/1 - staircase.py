# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:53:28 2020

@author: pedro

https://jtp.io/2016/07/26/dynamic-programming-python.html

https://math.stackexchange.com/questions/2055775/finding-all-possible-designs-for-a-staircase
"""

def solution(n):
    # Your code here
# =============================================================================
#     stair = [[-1 for i in range(n+2)] for j in range(n+2)]
#     
#     def addLevel(stair, height, left):
#         if stair[height][left] != -1:
#             return stair, stair[height][left] # already computed
#         if left == 0:
#             return stair, 1 # valid combination
#         if left < height:
#             return stair, 0 # new height not possible with left blocks
#         
#         # calculate new level using or not the current height
#         stair, s1 = addLevel(stair, height+1, left - height)
#         stair, s2 = addLevel(stair, height+1, left)
#         stair[height][left] = s1 + s2
#         
#         return stair, s1 + s2
#     
#     stair, comb = addLevel(stair, 1, n)
#     return comb - 1
# =============================================================================
        

    s = [[0 for i in range(n + 1)] for j in range(n + 1)]
    s[0][0] = 1

    for height in range(1, n + 1):
        for left in range(0, n + 1):
            s[height][left] = s[height - 1][left]
            if left >= height:
                s[height][left] += s[height - 1][left - height]
    
    return s
    return s[n][n] - 1
