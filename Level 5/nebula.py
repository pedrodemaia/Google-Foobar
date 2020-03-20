# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 08:33:00 2020

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

def copySolution(p):
    return [list(p[i]) for i in range(len(p))]

def solution(g):
    # Your code here
    def backPropagate(g, p, r, c):
        nextR, nextC = (r, c-1) if c > 0 else (r-1, len(g[r])-1)
            
        if r == len(g)-1:
            # last row
            s = p[r][c+1] + p[r+1][c+1]
            if g[r][c]:
                if s == 0:
                    p1 = copySolution(p)
                    p1[r][c], p1[r+1][c] = 1, 0
                    p2 = copySolution(p)
                    p2[r][c], p2[r+1][c] = 0, 1
                    return backPropagate(g, p1, nextR, nextC) + \
                        backPropagate(g, p2, nextR, nextC)
                elif s == 1:
                    p1 = copySolution(p)
                    p1[r][c], p1[r+1][c] = 0, 0
                    return backPropagate(g, p1, nextR, nextC)
                else:
                    return 0
            else:
                if s == 0:
                    p1 = copySolution(p)
                    p1[r][c], p1[r+1][c] = 0, 0
                    p2 = copySolution(p)
                    p2[r][c], p2[r+1][c] = 1, 1
                    return backPropagate(g, p1, nextR, nextC) + \
                        backPropagate(g, p2, nextR, nextC)
                elif s == 1:
                    p1 = copySolution(p)
                    p1[r][c], p1[r+1][c] = 0, 1
                    p2 = copySolution(p)
                    p2[r][c], p2[r+1][c] = 1, 0
                    p3 = copySolution(p)
                    p3[r][c], p3[r+1][c] = 1, 1
                    return backPropagate(g, p1, nextR, nextC) + \
                        backPropagate(g, p2, nextR, nextC) + \
                        backPropagate(g, p3, nextR, nextC)
                else:
                    p1 = copySolution(p)
                    p1[r][c], p1[r+1][c] = 0, 0
                    p2 = copySolution(p)
                    p2[r][c], p2[r+1][c] = 0, 1
                    p3 = copySolution(p)
                    p3[r][c], p3[r+1][c] = 1, 0
                    p4 = copySolution(p)
                    p4[r][c], p4[r+1][c] = 1, 1
                    return backPropagate(g, p1, nextR, nextC) + \
                        backPropagate(g, p2, nextR, nextC) + \
                        backPropagate(g, p3, nextR, nextC) + \
                        backPropagate(g, p4, nextR, nextC)
                        
        elif c == len(g[r])-1:
            # las col
            s = p[r+1][c] + p[r+1][c+1]
            if g[r][c]:
                if s == 0:
                    p1 = copySolution(p)
                    p1[r][c], p1[r][c+1] = 0, 1
                    p2 = copySolution(p)
                    p2[r][c], p2[r][c+1] = 1, 0
                    return backPropagate(g, p1, nextR, nextC) + \
                        backPropagate(g, p2, nextR, nextC)
                elif s == 1:
                    p1 = copySolution(p)
                    p1[r][c], p1[r][c+1] = 0, 0
                    return backPropagate(g, p1, nextR, nextC)
                else:
                    return 0
            else:
                if s == 0:
                    p1 = copySolution(p)
                    p1[r][c], p1[r][c+1] = 0, 0
                    p2 = copySolution(p)
                    p2[r][c], p2[r][c+1] = 1, 1
                    return backPropagate(g, p1, nextR, nextC) + \
                        backPropagate(g, p2, nextR, nextC)
                elif s == 1:
                    p1 = copySolution(p)
                    p1[r][c], p1[r][c+1] = 0, 1
                    p2 = copySolution(p)
                    p2[r][c], p2[r][c+1] = 1, 0
                    p3 = copySolution(p)
                    p3[r][c], p3[r][c+1] = 1, 1
                    return backPropagate(g, p1, nextR, nextC) + \
                        backPropagate(g, p2, nextR, nextC) + \
                        backPropagate(g, p3, nextR, nextC)
                else:
                    p1 = copySolution(p)
                    p1[r][c], p1[r][c+1] = 0, 0
                    p2 = copySolution(p)
                    p2[r][c], p2[r][c+1] = 0, 1
                    p3 = copySolution(p)
                    p3[r][c], p3[r][c+1] = 1, 0
                    p4 = copySolution(p)
                    p4[r][c], p4[r][c+1] = 1, 1
                    return backPropagate(g, p1, nextR, nextC) + \
                        backPropagate(g, p2, nextR, nextC) + \
                        backPropagate(g, p3, nextR, nextC) + \
                        backPropagate(g, p4, nextR, nextC)
        
        elif r == 0 and c == 0:
            # 1st cell
            s = p[0][1] + p[1][0] + p[1][1]
            if g[0][0]:
                if s <= 1:
                    return 1
                else:
                    return 0
            else:
                if s <= 1:
                    return 1
                else:
                    return 2
            
        else:
            # common case
            s = p[r][c+1] + p[r+1][c] + p[r+1][c+1]
            if g[r][c]:
                if s == 0:
                    p1 = copySolution(p)
                    p1[r][c] = 1
                    return backPropagate(g, p1, nextR, nextC)
                elif s == 1:
                    p1 = copySolution(p)
                    p1[r][c] = 0
                    return backPropagate(g, p1, nextR, nextC)
                else:
                    return 0
            else:
                if s == 0:
                    p1 = copySolution(p)
                    p1[r][c] = 0
                    return backPropagate(g, p1, nextR, nextC)
                elif s == 1:
                    p1 = copySolution(p)
                    p1[r][c] = 1
                    return backPropagate(g, p1, nextR, nextC)
                else:
                    p1 = copySolution(p)
                    p1[r][c] = 0
                    p2 = copySolution(p)
                    p2[r][c] = 1
                    return backPropagate(g, p1, nextR, nextC) + \
                        backPropagate(g, p2, nextR, nextC)
    
    m, n = len(g), len(g[0])

    p = [[-1 for i in range(n+1)] for j in range(m+1)]
    
    # if last position
    if g[-1][-1]:
        # create initial possibilities
        p1 = copySolution(p)
        p1[-2][-2], p1[-2][-1], p1[-1][-2], p1[-1][-1] = 0, 0, 0, 1
        p2 = copySolution(p)
        p2[-2][-2], p2[-2][-1], p2[-1][-2], p2[-1][-1] = 0, 0, 1, 0
        p3 = copySolution(p)
        p3[-2][-2], p3[-2][-1], p3[-1][-2], p3[-1][-1] = 0, 1, 0, 0
        p4 = copySolution(p)
        p4[-2][-2], p4[-2][-1], p4[-1][-2], p4[-1][-1] = 1, 0, 0, 0
        
        # execute back propagation to find feasible combinations
        return backPropagate(g, p1, m-1, n-2) + backPropagate(g, p2, m-1, n-2)\
            + backPropagate(g, p3, m-1, n-2) + backPropagate(g, p4, m-1, n-2)
    else:
        # create initial possibilities
        p1 = copySolution(p)
        p1[-2][-2], p1[-2][-1], p1[-1][-2], p1[-1][-1] = 0, 0, 0, 0
        p2 = copySolution(p)
        p2[-2][-2], p2[-2][-1], p2[-1][-2], p2[-1][-1] = 0, 0, 1, 1
        p3 = copySolution(p)
        p3[-2][-2], p3[-2][-1], p3[-1][-2], p3[-1][-1] = 0, 1, 0, 1
        p4 = copySolution(p)
        p4[-2][-2], p4[-2][-1], p4[-1][-2], p4[-1][-1] = 0, 1, 1, 0
        p5 = copySolution(p)
        p5[-2][-2], p5[-2][-1], p5[-1][-2], p5[-1][-1] = 0, 1, 1, 1
        p6 = copySolution(p)
        p6[-2][-2], p6[-2][-1], p6[-1][-2], p6[-1][-1] = 1, 0, 0, 1
        p7 = copySolution(p)
        p7[-2][-2], p7[-2][-1], p7[-1][-2], p7[-1][-1] = 1, 0, 1, 0
        p8 = copySolution(p)
        p8[-2][-2], p8[-2][-1], p8[-1][-2], p8[-1][-1] = 1, 0, 1, 1
        p9 = copySolution(p)
        p9[-2][-2], p9[-2][-1], p9[-1][-2], p9[-1][-1] = 1, 1, 0, 0
        p10 = copySolution(p)
        p10[-2][-2], p10[-2][-1], p10[-1][-2], p10[-1][-1] = 1, 1, 0, 1
        p11 = copySolution(p)
        p11[-2][-2], p11[-2][-1], p11[-1][-2], p11[-1][-1] = 1, 1, 1, 0
        p12 = copySolution(p)
        p12[-2][-2], p12[-2][-1], p12[-1][-2], p12[-1][-1] = 1, 1, 1, 1
        
        # execute back propagation to find feasible combinations
        return backPropagate(g, p1, m-1, n-2) + backPropagate(g, p2, m-1, n-2) + \
            backPropagate(g, p3, m-1, n-2) + backPropagate(g, p4, m-1, n-2) + \
            backPropagate(g, p5, m-1, n-2) + backPropagate(g, p6, m-1, n-2) + \
            backPropagate(g, p7, m-1, n-2) + backPropagate(g, p8, m-1, n-2) + \
            backPropagate(g, p9, m-1, n-2) + backPropagate(g, p10, m-1, n-2) + \
            backPropagate(g, p11, m-1, n-2) + backPropagate(g, p12, m-1, n-2)

solution(g)