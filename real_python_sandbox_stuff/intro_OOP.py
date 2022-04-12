# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 19:08:20 2022

@author: Windows10
"""

class Dog:
    
    species = 'canine'
    
    def __init__(self, name, age, gender):
        self.name =  name
        self.age = age
        self.gender = gender
    
    @property
    def dog_years(self):
        return self.age * 7 
    
    def speak(self, sound):
        return f'{self.name} says {sound}'
        
philo = Dog('philo', 5, 'M')
mikey = Dog('Mikey', 6, 'm')
