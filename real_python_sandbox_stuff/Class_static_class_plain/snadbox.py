# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 10:14:23 2022

@author: Windows10
"""

import concurrent.futures
import requests
import threading
import time

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        indicator = 'J' if 'jython' in url else 'R'
        print(indicator, sep='', end = '', flush = True)

def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)
        
if __name__ == '__main__':
    sites = ['https://www.jython.org',
             'http://olympus.realpython.org/dice'] * 80
    
    print('Starting downloads')
    start = time.time()
    download_all_sites(sites)
    duration = time.time() - start
    print(f'\nDownloaded {len(sites)} sites in {duration} seconds')

'''
import requests
import time

def get_session():
    return requests.Session()

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        indicator = 'j' if 'jython' in url else 'r'
        print (indicator, sep = '', end='', flush = True)

def download_all_sites(sites):
    for url in sites:
        download_site(url)
    
    print()
    
if __name__ == '__main__':
    sites = [
        'https://www.jython.org',
        'http://olympus.realpython.org/dice'] * 80
    print ('Starting downloads')
    start = time.time()
    download_all_sites(sites)
    duration = time.time() - start
    print(f'Download {len(sites)} sites in {duration} seconds')
'''    


# import random
# cases_per_thousand = [50, 60, 38, 20, 45, 405, 29, 102, 29, 28, 10, 39]
# cities = ['Vancouver', 'Oslo', 'Houston', 'Warsaw','Graz', 'Holquin']
# unsafe_places = [i>300  for i in cases_per_thousand]

# h = [city.startswith('H') for city in cities]

# g = any(i for i in random.sample([True,False], k=2))
# isnice = True
# isfar = True
# isfamily = False

# condition =  [isnice, isfar, isfamily]



# bowl = ['apple', 'peach', 'banana']
# shelf = 'chocolate cookies'.split(' ')

# bag =[*bowl, *shelf]
# class A:
#     def __init__(self):
#         print ('a')
#         super().__init__()
        
# class B(A):
#     def __init__(self):
#         print ('b')
#         super().__init__()

# class X:
#     def __init__(self):
#         print('X')
#         super().__init__()
        
# class Forward(B,X):
#     def __init__(self):
#         print ('Forward')
#         super().__init__()
        
# class Backward(X, B):
#     def __init__(self):
#         print ('Backward')
#         super().__init__()
# class Triangle:
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
        
#     def area(self):
#         return .5 * self.base * self.height
    
#     def what_am_i(self):
#         return 'I am a triangle'

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
        
#     def area(self):
#         return self.length * self.width
    
#     def perimeter(self):
#         return 2 * self.length + 2 * self.width
    
#     def what_am_i(self):
#         return 'I am a rectangle'

# class Square(Rectangle):
#     def __init__(self, length):
#         super().__init__(length, length)
      
#     def what_am_i(self):
#         return 'I am a square'

# class Cube(Square):
    
#     def surface_area(self):
#         face_area = self.area()
#         return face_area * 6

#     def volume(self):
#         face_area = super().area()
#         return face_area * self.length  

#     def family_tree(self):
#         #super() is a shortcut for super(Cube, self)
#         return self.what_am_i() + 'child of ' + super().what_am_i()
    
#     def what_am_i(self):
#         return 'I am a cube'
    
# class RightPyramid(Triangle, Square):
#     def __init__(self, base, slant_height):
#         self.base = base
#         self.slant_height = slant_height

#     def what_am_i(self):
#         return 'I am a Right Pyramid'


# right_pyramid = RightPyramid(2,4)           
# square = Square(2)
# cube = Cube(3)

# from dataclasses import dataclass
# from typing import List

# @dataclass
# class PlayingCard:
#     __slots__=['rank','suite']
#     rank: str
#     suite: str
#     extra: str
    
#     @property
#     def nonsense(self)->str:
#         return self.rank + self.suite    

# queen_of_spade = PlayingCard('q', 's', 'e')
# queen_of_hearts = PlayingCard('q', 'h', 'f')
# @dataclass
# class Deck:
#     cards: List[PlayingCard] 
    

# deck = Deck([queen_of_spade, queen_of_hearts])

# RANK = '2,3,4,5,6,7,8,9,10,j,q,k,a'.split(',')
# SUITES = '\u2660 \u2665 \u2666 \u2663'.split()

# def make_french_deck():
#     return [PlayingCard(r,s) for r in RANK for s in SUITES]

# from collections import namedtuple

# Person = namedtuple('person', ['height', 'age'])

# ralph = Person(12, 24)

# from dataclasses import dataclass

# class RegularDataCard:
#     def __init__(self, rank:str, suite:str):
#         self.rank = rank
#         self.suite = suite
        
#     def __repr__(self):
#         return f'{self.__class__.__name__} (rank = {self.rank!r}'\
#             f', suite = {self.suite})'

# Reg_queen_of_hearts = RegularDataCard('Q', 'Hearts')   
    
# @dataclass
# class DataClassCard:
#     rank: str
#     suit: str = 'H'


# queen_of_hearts = DataClassCard(12, False)

# queen_of_hearts_2 = DataClassCard(rank=12, suit='Hearts')

# class Car:
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage
        
#     def __str__(self):
#         return f'Car with color {self.color} and mileage: \
#             {self.mileage}'
            
#     def __repr__(self):
#         return f'{self.__class__.__name__}("{self.color}", {self.mileage})'
    
    
# car = Car('red', 10098)

# print(car) 

# class MyClass:
#     def method(self):
#         return 'instance method', self
    
#     @classmethod
#     def class_method(cls):
#         return 'class method', cls
    
#     @staticmethod
#     def static_method():
#         return 'static method'

# obj = MyClass()
# (obj.method())

