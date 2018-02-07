# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 16:54:51 2018

@author: Clif
"""

def find_largest_prime_factor(number):
    def is_prime(number):
        if number==1:
            return False
        for i in range(2,number):
            if (not number % i):
                return False
        return True
    
    largest_prime_factor=0
    for i in range(1, number):
        if is_prime(i) and not number % i:
            print(i)
            largest_prime_factor = i
    return largest_prime_factor    

find_largest_prime_factor(600851475143)
