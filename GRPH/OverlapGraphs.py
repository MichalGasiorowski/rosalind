# -*- coding: utf-8 -*-
"""

@author: Michal

Problem

A graph whose nodes have all been labeled can be represented by an adjacency 
list, in which each row of the list contains the two node labels corresponding to a unique edge.

A directed graph (or digraph) is a graph containing directed edges, each
of which has an orientation. That is, a directed edge is represented by an
arrow instead of a line segment; the starting and ending nodes of an edge form 
its tail and head, respectively. The directed edge with tail v and head w is
represented by (v,w) (but not by (w,v)). A directed loop is a directed edge of the form (v,v).

For a collection of strings and a positive integer k, the overlap graph for
the strings is a directed graph Ok in which each string is represented by
a node, and string s is connected to string t with a directed edge when there
is a length k suffix of s that matches a length k prefix of t, 
as long as s≠t; we demand s≠t to prevent directed loops in the overlap
graph (although directed cycles may be present).

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.

"""

basePairs = "ACGT"

def read_fasta(filename):
    f = open(filename, 'r')
    dna_strings = f.read().strip().split(">")[1:]
    dna_ret = [ map(lambda x: x.replace("\n", ""), dna_s.split("\n", 1)) for dna_s in dna_strings]
    return dna_ret

def calc_suffixes_prefixes(dna_strings, k):
    return [[item[0], item[1], item[1][-k:], item[1][:k]]   for item in dna_strings]
        

fo = open("out.txt", 'w')
dna_strings = read_fasta("rosalind_grph.txt")
dna_strings = calc_suffixes_prefixes(dna_strings, 3)

vertices = set()
edges = []

for i in range(len(dna_strings)):
    v1 = dna_strings[i]
    v1_name, v1_dna, v1_suff, v1_pre = v1
    for v2 in dna_strings[i+1:]:
        v2_name, v2_dna, v2_suff, v2_pre = v2
        if v1_suff == v2_pre: # v1 -> v2
            vertices.add(v1_name)
            vertices.add(v2_name)
            edges.append((v1_name, v2_name))          
        if v2_suff == v1_pre: # v2 -> v1
            vertices.add(v1_name)
            vertices.add(v2_name)
            edges.append((v2_name, v1_name))

fo.write("\n".join([" ".join(edge) for edge in edges]  )  )

#for edge in edges:
    #fo.write(" ".join(edge) + "\n")           



fo.close()


    
