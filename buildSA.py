# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 10:05:43 2021

@author: Kahn Potter
"""

from suffix import suffix

class buildSA:
    def __init__(self, text, n):
        self.text = text
        self.n = n
        
    def cmp(self, a):
        return a.suff
        
    def build(self):
        n = self.n
        text = self.text
        
        suffixes = []
        
        for i in range(n):
            s = suffix(i, text[i:])
            suffixes.append(s)
            
        suffixes = sorted(suffixes, key = self.cmp)
        #print(suffixes)
        
        suffixArr = []
        
        for i in range(n):
            suffixArr.append(suffixes[i].index)
            
        return suffixArr
        
    