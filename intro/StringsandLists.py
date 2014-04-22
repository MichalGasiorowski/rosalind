# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 21:17:16 2014

@author: Michal
"""


def readfile(filename):
    return open(filename, 'rt').read().split()

def sliceIt(toSlice, i1, i2, j1, j2):
    return toSlice[i1:i2+1] + " " + toSlice[j1:j2+1]
    
