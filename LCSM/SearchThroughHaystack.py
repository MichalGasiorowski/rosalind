# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 23:29:07 2014

@author: Michal

Problem

A common substring of a collection of strings is a substring of every member 
of the collection. We say that a common substring is a longest common substring
if there does not exist a longer common substring. 
For example, "CG" is a common substring of "ACGTACGT" and "AACCGGTATA", 
but it is not as long as possible; in this case, "GTA" is a longest common 
substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a 
simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. 
(If multiple solutions exist, you may return any single solution.)

"""


from functools import wraps

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)            
        return cache[args]
    return wrap

def lcp(i, j, s):
    ret = 0
    n = len(s)
    for k in range(n):
        if i+k >= n or j+k >=n:
            break
        if s[i+k] != s[j+k]:
            break
        ret += 1
    return ret
#print lcp(1, 3, "banana$")

def suffix_lcp(s):    
    
    n = len(s)    
    ss = [i for i in range(n)]
    suffix = sorted(ss, key = lambda x: s[x:])
    lcp_arr = [lcp(suffix[i - 1], suffix[i], s) for i in range(1, n)]
    return suffix, lcp_arr  

class SuffixTree(object):
    
    class Node(object):
        def __init__(self, label):
            self.label = label
            self.child = {}
    def __init__(self, s, term):
        s += term
        








    
print suffix_lcp("banana$")