# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 23:10:58 2014

@author: Michal
"""



def readfile(filename):
    return open(filename, 'r').readlines()
    
    
def writeEvenLines(infile, outfile):
    outF = open(outfile, 'w')
    outF.write(''.join(readfile(infile)[1::2]))    
    outF.close()    
    
