# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 19:33:57 2022

@author: Windows10
"""

class Rectangle:
    def __init__(self, heigth, length):
        self._heigth = heigth
        self._length = length
        
    @property
    def area(self):
        return (self._heigth * self._length)
    
    def resize(self, new_heigth, new_length):
        self._heigth = new_heigth
        self._length = new_length



class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)
    
    '''@property 
    def area(self):
        return (self.side * self.side)'''
    
s = Square(3)
assert s.area==9
print('ran ok')

r =  Rectangle(2,3)
assert r.area==6
print('ran ok')
        
r.resize(4,5)  
assert r.area == 20
print('ran ok')

s.resize(3,5)

print(s.area)


      