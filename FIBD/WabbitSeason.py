# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 19:41:27 2014

@author: Michal

Problem
Figure 4. A figure illustrating the propagation of Fibonacci's rabbits 
if they die after three months.

Recall the definition of the Fibonacci numbers from 
“Rabbits and Recurrence Relations”, which followed the recurrence relation 
Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one
month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic 
programming solution in the case that all rabbits die out after a fixed
number of months. See Figure 4 for a depiction of a rabbit tree in
which rabbits live for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the 
n-th month if all rabbits live for m months.

"""
import numpy as np
import operator

def tick(old_pop_structure, m):
    new_pop_structure = [0]*m
    
    #print old_pop_structure[1:]    
    
    new_pop_structure[0]  = reduce(operator.add, old_pop_structure[1:])  
    
    #new_pop_structure[0] = sum(old_pop_structure[1:])
    #print '%s' % new_pop_structure[0]
    #print "##########"
    for i in range(1, m):
        new_pop_structure[i] = old_pop_structure[i - 1]
    return new_pop_structure
        

    
    
f = open("rosalind_fibd.txt", 'r')
data = f.read().strip().split()
print data
n, m = long(data[0]), long(data[1])
print n, m
pop_structure = [1] + [0]*(m - 1)
#print pop_structure

for i in range(n - 1):
    #print i + 1, pop_structure, sum(pop_structure)
    pop_structure = tick(pop_structure, m)

#print(pop_structure)

fo = open("out.txt", 'w')
fo.write('%d' % sum(pop_structure))


fo.close()