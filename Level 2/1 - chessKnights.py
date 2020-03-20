#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:45:41 2020

@author: pedro
"""

def solution(src, dest):
    def getRowCol(x):
        return x//8, x%8
    
    def isValid(r, c):
        return r >= 0 and r <= 7 and c >= 0 and c <= 7
    
    # get initial and final rows and columns
    orow, ocol = getRowCol(src)
    drow, dcol = getRowCol(dest)
    
    # possible moves
    moves = [(2,1), (2,-1), (1,2), (1,-2), (-1,2), (-1,-2), (-2,1), (-2,-1)]
    
    # search list
    line = []
    point = (orow, ocol, 0)
    line.append(point)
    
    #min moves to reach each point
    visited = [[False for r in range(8)] 
                      for c in range(8)]
    visited[orow][ocol] = True
    
    while len(line) > 0:
        # get 1st elem in the line
        point = line.pop(0)
        row = point[0]
        col = point[1]
        dist = point[2]
        
        # achieved destination
        if row == drow and col == dcol:
            return dist
        
        for move in moves:
            rowtemp = row + move[0]
            coltemp = col + move[1]
            
            if isValid(rowtemp,coltemp) and not visited[rowtemp][coltemp]:
                newPoint = (rowtemp, coltemp, dist+1)
                line.append(newPoint)
                visited[rowtemp][coltemp] = True
                


src = 1
dest = 0

solution(src,dest)