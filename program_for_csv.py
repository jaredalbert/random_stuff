# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 19:13:42 2019

@author: jaredalbert
"""

import csv_import_Practice
import pprint


pp = pprint.PrettyPrinter(indent=40)

def main():
    csv_import_Practice.init()
    #print(csv_import_Practice.data)
    
    print('highest price paid')
    print(csv_import_Practice.highest_price())
    print('lowest price paid')
    print(csv_import_Practice.lowest_price())
    
    
    
if __name__ == '__main__':
    pp.pprint('starting')
    main()