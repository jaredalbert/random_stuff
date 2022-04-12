# -*- coding: utf-8 -*-
"""
Created on Sun May 26 18:24:28 2019

@author: jaredalbert
"""
import pytest
from twosum import Solution

def test_answer():
    assert Solution([3, 3, 4, 5, 6, 7], 9).twoSum() == [0,4]
    assert Solution([3, 3], 6).twoSum() == [0,1]