# -*- coding: utf-8 -*-
"""

@author: Michal

Problem

For a random variable X taking integer values between 1 and n, the expected 
value of X is E(X)=∑nk=1k×Pr(X=k). The expected value offers us a way of 
taking the long-term average of a random variable over a large number of trials.

As a motivating example, let X be the number on a six-sided die.
Over a large number of rolls, we should expect to obtain an average of 3.5
on the die (even though it's not possible to roll a 3.5).
The formula for expected value confirms that E(X)=∑6k=1k×Pr(X=k)=3.5.

More generally, a random variable for which every one of a number of equally
spaced outcomes has the same probability is called a uniform random variable
(in the die example, this "equal spacing" is equal to 1). We can generalize 
our die example to find that if X is a uniform random variable with minimum 
possible value a and maximum possible value b, then E(X)=a+b2. You may also 
wish to verify that for the dice example, if Y is the random variable 
associated with the outcome of a second die roll, then E(X+Y)=7.

Given: Six positive integers, each of which does not exceed 20,000. 
The integers correspond to the number of couples in a population possessing
each genotype pairing for a given factor. In order, the six given integers 
represent the number of couples having the following genotypes:

    AA-AA
    AA-Aa
    AA-aa
    Aa-Aa
    Aa-aa
    aa-aa

Return: The expected number of offspring displaying the dominant phenotype in 
the next generation, under the assumption that every couple has exactly two offspring.
"""


genotypes = ['AA-AA', 'AA-Aa', 'AA-aa', 'Aa-Aa', 'Aa-aa','aa-aa']
genotypes_dominant_prob = {'AA-AA' : 1, 'AA-Aa' : 1, 'AA-aa' : 1, 'Aa-Aa' : 0.75, 'Aa-aa' : 0.5,'aa-aa' : 0}
    
f = open("rosalind_iev.txt", 'r')
data = f.read().strip()
nums = [int(num) for num in data.split()]
ex_dominant_phenotype = 0
for i in range(len(genotypes)):
    ex_dominant_phenotype += genotypes_dominant_prob[genotypes[i]] * nums[i] * 2    



fo = open("out.txt", 'w')
fo.write(str(ex_dominant_phenotype))

fo.close()    
     