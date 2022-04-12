# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 18:24:33 2022

@author: Windows10
"""

class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    
    @property    
    def area(self):
        return (self._length * self._width)
    
    def resize(self, new_length, new_width):
        self._length = new_length
        self._width = new_width
    
    
r = Rectangle(2,3)
assert r.area == 6
print('ok')

r.resize(4,6)
assert r.area == 24
print('24')

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(self.side, self.side)
    
    def resize(self, new_length, new_width):
        self._length = new_length
        self._width = new_length

s = Square(3)
print(f' s.area: {s.area}')

s.resize(4)
print(s.area)
    
