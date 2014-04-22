# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 22:56:10 2014

@author: Michal

"""

"""
return sum of all odd integers between a, b inclusive
"""
def sumOfAllOdd(a, b):
    return sum([i for i in range(a, b+1) if i%2==1 ])
    