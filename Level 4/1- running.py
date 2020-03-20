# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 08:24:41 2020

@author: pedro
"""

# test case 1
times = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], 
         [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
times_limit = 1
sol = [1, 2]

# test case 2
times = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], 
         [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]
times_limit = 3
sol = [0, 1]

def solution(times, times_limit):
    # Your code here
    import itertools

    def getTimeToComplete(times,bunnies):
        route = [0] + bunnies + [len(times)-1]
        time = 0
        for i in range(1,len(route)):
            time += times[route[i-1]][route[i]]
        return time
    
    n = len(times)
    num_bunnies = n - 2
    
    # get minimum time to reach each position from each origin
    # if it is possible to leave i and reach j passing in k faster than the 
    # direct route, the time from i to j is adjusted 
    for i in range(n):
        for j in range(n):
            for k in range(n):
                times[i][j] = min(times[i][j], times[i][k] + times[k][j])
    
    # check if can get infinity time by leaving some place and returning to it
    for i in range(n):
        if times[i][i] < 0:
            return list(range(num_bunnies))
        
    # create all possible permutations for all quantities of bunnies
    for num in range(num_bunnies, 0, -1):
        for permutation in itertools.permutations(range(1,num_bunnies+1), num):
            bunnies = list(permutation)
            if getTimeToComplete(times,bunnies) <= times_limit:
                return sorted([bunny-1 for bunny in bunnies])
    return []
    