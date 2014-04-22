# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 12:46:10 2014

@author: MGasiorowski

Problem

The GC-content of a DNA string is given by the percentage of symbols in the 
string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%.
Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. 
A commonly used method of string labeling is called FASTA format. 
In this format, the string is introduced by a line that begins with '>', 
followed by some labeling information. Subsequent lines contain the string 
itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the
ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the 
GC-content of that string. Rosalind allows for a default error of 0.001 in 
all decimal answers unless otherwise stated; please see the note on absolute error below.

"""

#from collections import Counter

def gc_content(s):
    s_strip = s.strip().replace("\n", "")
    return (s_strip.count("G") + s_strip.count("C") + 0.0)/len(s_strip)
    
fo = open("out.txt", 'w')

with open("rosalind_gc.txt", 'r') as f:
    dna_strings = f.read().strip().split(">")
    max_gc = 0
    max_gc_name = ""
    
    for dna_s in dna_strings[1:]:
        curr_gc_name, curr_gc_content = dna_s.split("\n", 1)
        curr_gc = gc_content(curr_gc_content)
        if curr_gc > max_gc:
            max_gc = curr_gc
            max_gc_name = curr_gc_name
    fo.write(max_gc_name + "\n" + str(100*max_gc))
        
        
fo.close()
    
    