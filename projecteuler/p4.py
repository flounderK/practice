# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 17:20:35 2018

@author: Clif
"""

largest_palindrome_product = 0
def is_palindrome(number):
    if number == int(str(number)[::-1]):
        return True
    return False

for i in range(100,1000):
    for k in range(100,1000):
        prod = i*k
        if is_palindrome(prod) and prod > largest_palindrome_product:
            largest_palindrome_product = prod
print(largest_palindrome_product)