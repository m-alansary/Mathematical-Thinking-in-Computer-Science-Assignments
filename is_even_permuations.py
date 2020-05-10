# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 15:32:41 2018

@author: Ansary
"""

def is_even_permutation(p):
    sign = 0
    s = 0
    n = len(p)
    while s < n:
        u = s
        while u < n:
            if p[u] < p[s]:
                tmp = p[s]
                p[s] = p[u]
                p[u] = tmp
                sign = 1 - sign
            u = u +1
        s = s + 1
    if sign == 0:
        return True
    return False

print(is_even_permutation([0,3,2,4,5,6,7,1,9,8] ))