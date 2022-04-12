# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 19:09:11 2019

@author: jaredalbert
"""

#C:\Users\jaredalbert\Downloads

import os
import csv
from datetime import datetime as dt
from collections import namedtuple
from typing import List


data = []
format = '%Y%m%d:%H:%M:%S'
day = '20190319'

Record = namedtuple('Record', 'Underlying, Action, Quantity,\
                                Price, Time, Exch')

def init():
    #base_folder = os.path.dirname('c:\\Users\\jaredalbert\\Downloads')
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'trades.'+day+'.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        #print(fin.read())
        
        data.clear()
        for row in reader:
            record =  parse_row(row)
            data.append(record)
            

def parse_row(row):
    row['Underlying'] = str(row['Underlying'])
    row['Action'] = str(row['Action'])
    row['Quantity'] = int(row['Quantity'])
    row['Price'] = float(row['Price'])
    row['Time'] = dt.strptime(day+':'+row['Time'], format)
    row['Exch'] = str(row['Exch.'])
    #record = Record(**row)
    record = Record(
            Underlying = row['Underlying'],
            Action = row['Action'],
            Quantity = row['Quantity'],
            Price = row['Price'], 
            Time = row['Time'],
            Exch = row['Exch']
            )
    return record

def highest_price() -> List[Record]:
    return sorted(data, key=lambda x: -x.Price)[0][3]

def lowest_price():
    return sorted(data, key=lambda x: x.Price)[0][3] 
    
    
    

#        
