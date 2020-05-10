# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 21:44:25 2018

@author: Ansary
"""
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))
    
def Towers(n, fr, to, spare):
    if n == 1:
        global moves
        moves += 1
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
  
moves = 0      
Towers(6,0,1,2)
print(moves)