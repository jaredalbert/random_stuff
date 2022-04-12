# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:23:30 2019

@author: jaredalbert
"""
from typing import List 
import pytest 

class Solution:      
    def __init__(self,  nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        
    def twoSum(self):
         for i, num in enumerate(self.nums):
            for j, num2 in enumerate(self.nums[i+1:]):
                if num + num2 == self.target:
                    return [i, j+i+1]           


def main(l, t):
    s = Solution(l, t)
    print(s.twoSum())

#def test_answer():
#    assert Solution([3,3], 1) == [0,1]



if __name__ == '__main__':
    l = [3, 3, 4, 5, 6, 7]
    t = 9
    main(l, t)
   

