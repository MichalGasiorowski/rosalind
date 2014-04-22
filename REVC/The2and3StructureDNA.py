# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 12:04:26 2014

@author: MGasiorowski
Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing 
the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""

import string

transInTab = "ACGT"
transOutTab = "TGCA"

transTable = string.maketrans(transInTab, transOutTab)

fo = open("out.txt", 'w')

with open("rosalind_revc.txt", 'r') as data:
    s = data.read().strip()
    reverse_compl = s[::-1].translate(transTable)
    fo.write(reverse_compl)

fo.close()
#f = open("in.txt", 'r')
#data = str(f.read().strip())

