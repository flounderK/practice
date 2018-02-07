# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 16:44:39 2018

@author: Clif
"""


a = 1
b = 2
total = 2

while b < 4000000:
    c = a + b
    a = b
    b = c
    if not c % 2:
        total += c
print(total)