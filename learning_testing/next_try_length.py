# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:00:34 2019

@author: jaredalbert
"""

def find_length(s: str)->int:
    counter = {}
    distance, largest = 0,0
    for i in range(len(s)):
        if s[i] in counter:
            distance = max(distance, counter[s[i]] )
            print('counter[s[i]]', s[i], counter[s[i]])
            print(f'distance, {distance} \
              counter[s[i]]')
        largest = max(i - distance, largest)
        counter[s[i]] = i




    return largest

s = "nnna"
print(find_length(s))

