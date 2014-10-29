# -*- coding: utf-8 -*-
"""

@author: MGasiorowski

Problem
A string is simply an ordered collection of symbols selected from some alphabet
 and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string 
(whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number 
of times that the symbols 'A', 'C', 'G', and 'T' occur in s


"""


f = open("rosalind_dna.txt", 'r')
data = f.read()

dna_dict = {}

for symbol in data.strip():
    if symbol in dna_dict:
        dna_dict[symbol] += 1
    else:
        dna_dict[symbol] = 1

count_out = " ".join([str(v) for k, v in sorted(dna_dict.iteritems())])

    

fo = open("out.txt", 'w')
fo.write(count_out)

fo.close()

