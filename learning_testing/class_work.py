# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:11:56 2019

@author: jaredalbert
"""


class Try:
    def __init__(self, text):
        self.text = text

    def token(self):
        return (self.text.split(' '))

    def new_token(self):
        return(self.token())

    def new_new_token(self):
        return self.new_token() + ['yes']

class Try2(Try):
    def __init__(self, text):
        self.text = text
        self.response = 'this is a response'
        Try.__init__(self, text)
            #self.text = text
    def __str__(self):
        return ('just reponsing')

def main(x):
    import cProfile
    profiler = cProfile.Profile()
    profiler.enable()
    z = Try(x).token()
    return(print(z))


    profiler.print_stats(sort='cumtime')
    profiler.disable()
if __name__ == '__main__':
    print('starting')
    x = 'this is a test string'
    main(x)




