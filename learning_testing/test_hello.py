# -*- coding: utf-8 -*-
"""
Created on Sun May 26 17:32:59 2019

@author: jaredalbert
"""

from say_hello import hello_name

def test_hello():
    assert hello_name('me') == 'hello me'

