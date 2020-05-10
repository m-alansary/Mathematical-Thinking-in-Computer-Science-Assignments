# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 13:21:48 2018

@author: Ansary
"""

def whichType(perm, i):
    TL = perm[i - 6]
    TR = perm[i - 4]
    L = perm[i - 1]
    T = perm[i - 5]

    if L != 2  and T != 2 and TL != 1:
        return 1
    elif (L != 1 and T != 1 and TR != 2):
        return 2
    else:
        return 0
    
def isComplete(perm, n):
    result = 0
    for i in perm:
        if i == 1 or i == 2:
            result += 1
    if (result >= n):
        return True
    
        
    
def extend(perm, n):
    if isComplete(perm, n):
        print(perm)
        exit()
    else:
        for 
        


