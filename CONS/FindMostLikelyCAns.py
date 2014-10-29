# -*- coding: utf-8 -*-
"""

@author: MGasiorowski

Problem

A matrix is a rectangular table of values divided into rows and columns. 
An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate
the value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n.
Their profile matrix is a 4×n matrix P in which P1,j represents the number
of times that 'A' occurs in the jth position of one of the strings, P2,j
represents the number of times that C occurs in the jth position, and so on (see below).

A consensus string c is a string of length n formed from our collection 
by taking the most common symbol at each position; the jth symbol of c therefore
corresponds to the symbol having the maximum value in the j-th column 
of the profile matrix. Of course, there may be more than one most common symbol, 
leading to multiple possible consensus strings.

            	A T C C A G C T
            	G G G C A A C T
            	A T G G A T C T
DNA Strings 	A A G C A A C C
            	T T G G A A C T
            	A T G C C A T T
            	A T G G C A C T
            	A   5 1 0 0 5 5 0 0
Profile	      C   0 0 1 4 2 0 6 1
            	G   1 1 6 3 0 1 0 0
            	T   1 5 0 0 0 1 1 6
Consensus	      A T G C A A C T

Given: A collection of at most 10 DNA strings of
equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. 
(If several possible consensus strings exist, then you may return any one of them.)

"""

from itertools import repeat

basePairs = "ACGT"

def read_fasta(filename):
    f = open(filename, 'r')
    dna_strings = f.read().strip().split(">")[1:]
    dna_ret = [ map(lambda x: x.replace("\n", ""), dna_s.split("\n", 1)) for dna_s in dna_strings]
    return dna_ret
    
def get_max_bpair(profile_matrix, ind):
    max_c = -1
    max_bpair = ""
    for bpair in basePairs:
        if profile_matrix[bpair][ind] > max_c:
            max_c = profile_matrix[bpair][ind]
            max_bpair = bpair
    return max_bpair    
    
    
dna_strings = read_fasta("rosalind_cons.txt")     
#print dna_strings
dna_len = len(dna_strings[0][1])
dataset_num = len(dna_strings)

profile = {"A" : [0] * dna_len, "C" : [0] * dna_len,"G" : [0] * dna_len, "T" : [0] * dna_len}

for i in range(dna_len):
    for bPair in basePairs:
        profile[bPair][i] = sum([1 for d_num in range(dataset_num) if dna_strings[d_num][1][i] == bPair ])


consensus = "".join([get_max_bpair(profile, i) for i in range(dna_len)])

fo = open("out.txt", 'w')
fo.write("".join(consensus))
for bPair in basePairs:    
    fo.write('\n%s: %s' % (bPair, " ".join(map(lambda x: str(int(x)) , profile[bPair])) ))

fo.close()
