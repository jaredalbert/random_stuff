# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 07:23:36 2020

@author: Windows10
"""

'''Enter an integer or float and the nth digit place that you want to retrieve 
for example the 1's place would be n=1, the 10's place would be n = 2, the 100's n=3 etc'''
def get_digit(number, n):
    return number // 10**(n-1) % 10

print(get_digit(123456,2)) #works with integers

5


print(get_digit(123456.78,2)) #works with floats
5.0


print(get_digit(-123456.78,2)) #FAILS with negative numbers
4.0


