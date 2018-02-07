# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 16:31:31 2018

@author: Clif
"""

count = 0
for i in range(1,1000):        
    if (not i % 3) or (not i % 5):
        count += i
print(count)