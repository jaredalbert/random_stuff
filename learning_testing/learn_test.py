# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:20:34 2019

@author: jaredalbert
"""

import pytest
#import spyder_unittest

#
def is_prime(number):
    """Return True if `number` is prime."""
    for element in range(2, number):
        if number % element == 0:
            return False
    return True

#
#
#def test_five_is_prime():
#    assert is_prime(5) == True
#
#def test_four_is_not_prime():
#    assert is_prime(5) == False
## content of test_sample.py
#def inc(x):
#    return x + 1
#
#
#def test_answer():
#    assert inc(3) == 5






    