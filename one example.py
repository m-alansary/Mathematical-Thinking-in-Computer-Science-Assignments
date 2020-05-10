# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 15:29:16 2018

@author: Ansary
"""

from math import floor

a = 95800
b = 217519
c = 414560

d = a ** 4 + b ** 4 + c ** 4
d = d ** (1/4)
if floor(d) == d and a != 0 and b != 0 and c != 0:
    print(True)
