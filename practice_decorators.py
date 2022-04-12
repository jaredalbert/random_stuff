# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 09:04:42 2019

@author: jaredalbert
"""
#
#def add_2(func):
#    def wrap_add_2(*args, **kwargs):
#        print('starting')
#        print (func(*args, **kwargs) + 3)
#    return wrap_add_2
#
#
##print ([add_2(i) + 1 for i in range(7)])
#
#@add_2
#def trying(num):
#    return (num)
#
#trying(4)
#trying(10)

#print(f'print {add_2(3)}')

#def my_decorator(func):
#    def wrapper():
#        print("Something is happening before the function is called.")
#        func()
#        print("Something is happening after the function is called.")
#    return wrapper
#
#def say_whee():
#    print("Whee!")
#
#
#say_whee = my_decorator(say_whee)
#say_whee()











import functools
def test_2(func):
    @functools.wraps(func)
    def wrapper_test_2(*args, **kwargs):
        print('starting test')
        x = (func(*args, **kwargs))
        print('ending test')
        return x
    return wrapper_test_2

#@test_2
def oddball(*args, **kwargs):
    for item in list(*args):
        x = 2* item
        print( x)
    print({k:v for v,k in kwargs.items()})

my_list = [23,3,4,5]

#oddball(my_list)
#print([2*i for i in my_list])

#oddball([2, 'hey'], **dict(x=2, y=[3,4,5]))
keywords = dict(keyword1 = 'foo', keyword2 = 'bar')
oddball(my_list)
