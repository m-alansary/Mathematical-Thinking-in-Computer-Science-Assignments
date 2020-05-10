# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 21:14:02 2018

@author: Ansary
"""

def change(amount):
    if amount == 28:
        return [7, 7, 7, 7]
        
    elif amount == 24:
        return [5, 5, 7, 7]
    
    elif amount == 22:
        return [5, 5, 5, 7]
    
    elif amount == 21:
        return [7, 7, 7]
    
    elif amount == 20:
        return [5, 5, 5, 5]
    
    elif amount == 19:
        return [5, 7, 7]
        
    coins = change(amount - 5)
    coins.append(5)
    return coins

coins = change(57)
print(coins)