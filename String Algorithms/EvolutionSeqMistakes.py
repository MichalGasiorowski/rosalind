# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 13:34:13 2014

@author: MGasiorowski

Problem
Given two strings s and t of equal length, the Hamming distance between
s and t, denoted dH(s,t), is the number of corresponding symbols
that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

"""

def hamming_distance(s, t):
    if len(s) != len(t):
        return 9999
    return sum( (1 for cs, ct in zip(s,t) if cs != ct ) )

fo = open("out.txt", 'w')

with open("rosalind_hamm.txt", 'r') as f:
    data = f.readlines()
    s1 = data[0].strip()
    s2 = data[1].strip()
    fo.write(str(hamming_distance(s1, s2)))

fo.close()