# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 11:17:19 2014

@author: MGasiorowski

Problem

An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

"""

f = open("rosalind_rna.txt", 'r')
data = str(f.read().strip())

fo = open("out.txt", 'w')

s = data.replace("T", "U")
fo.write(s)

fo.close()
