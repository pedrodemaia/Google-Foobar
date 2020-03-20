# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 08:13:00 2020

@author: pedro
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 08:06:33 2020

@author: pedro
"""

# test case 1
dimensions = [3,2]
your_position = [1,1]
guard_position = [2,1]
distance = 4

# test case 2
dimensions = [300,275]
your_position = [150,150]
guard_position = [185,100]
distance = 500

import math
import itertools

# return squared distance between points
def getDistance(origin, dest):
    return math.sqrt((dest[0] - origin[0])**2 + (dest[1] - origin[1])**2)

def getAngle(origin, target, tol = 10):
    angle = math.atan2(target[1]-origin[1], target[0]-origin[0])
    return round(angle, tol)

def getDirections(dimensions, origin, target, distance):
    # get extended positions
    minVal = -distance//dimensions[0] - 1
    maxVal = distance//dimensions[0] + 1
    xExtensions = list(set([2*i*dimensions[0] + side*target[0] for i in 
                           range(minVal, maxVal+1) for side in [-1,1]]))
    
    minVal = -distance//dimensions[1] - 1
    maxVal = distance//dimensions[1] + 1
    yExtensions = list(set([2*i*dimensions[1] + side*target[1] for i in 
                           range(minVal, maxVal+1) for side in [-1,1]]))
    
    # build extended points
    extended = [(x,y) for x in xExtensions for y in yExtensions]
    extended = [v for v in extended if getDistance(v,origin) <= distance
                and v !=tuple(origin)]
    
    # get angle of extended directions
    angles = [[getAngle(origin,v),getDistance(origin,v)] for v in extended]
    angles.sort()
    uniqueAngles = [list(p)[0] for i, p in 
                    itertools.groupby(angles,lambda p:p[0])]
    
    return uniqueAngles

def isAngleValid(a, d, collisions):
    if a in collisions:
        if collisions[a] < d:
            return False
    return True
    
def solution(dimensions, your_position, guard_position, distance):    
    my_angles = getDirections(dimensions, your_position, your_position, distance)
    
    guard_angles = getDirections(dimensions, your_position, guard_position, distance)
    
    collisionAngles = dict(my_angles)
    
    cont = 0
    for a,d in guard_angles:
        if isAngleValid(a, d, collisionAngles):
            cont += 1
    return cont