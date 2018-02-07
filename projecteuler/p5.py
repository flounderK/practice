# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 17:33:57 2018

@author: Clif
"""
def divisible_by_1_20(number):
    still_divisible = True
    i = 2
    while (i < 20) and (still_divisible):
        if (number % i):
            still_divisible = False
        i = i + 1
    return still_divisible

number_found = False
i = 1
while not number_found:
    if divisible_by_1_20(i):
        number_found = True
        break
    i = i + 1
print(i)