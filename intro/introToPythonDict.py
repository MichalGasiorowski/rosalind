# -*- coding: utf-8 -*-
"""

@author: Michal
"""

def createDict(s):
    words = {}
    for word in s.split(' '):
        t_word = word.strip()
        if t_word in words:
            words[t_word] += 1
        else:
            words[t_word] = 1
    return words

f = open("rosalind_ini6.txt", 'r')

words = createDict(f.read())

fo = open("out.txt", 'w')
fo.write('\n'.join([word + " " + str(words[word]) for word in words]))

fo.close()
    
    