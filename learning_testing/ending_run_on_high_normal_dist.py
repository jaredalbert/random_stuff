# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 21:17:07 2019

@author: jaredalbert
"""
'''
by randomness that a market with 55.2%  up days and 250 trading days
 will end at the high> and does that have any evollutionary
 significance e.g. the battle  of  males to be at a
 maximum relative  to com[petitors in other  fields?'''

from random import sample, seed
import numpy as np
seed = 10
#55% of 250 give 137.5, so to avoid half days went with 55.2% up days
'''249 trading days
149 Up days, or 59.8%
mean Up day: +0.57%
mean Up day: 1.61 pts
sd: 1.32

mean Dwn day: -0.57%
mean Dwn day: -1.63 pts
sd: 1.83'''
up =np.random.normal(1.61, 1.32, 138)
down = np.random.normal(-1.63, 1.83, 112)
total_days = list(np.concatenate((up,down)))

win_count = 0
total_runs= 10



for _ in range(total_runs):
    m=0
    running_total = []
    test_population = sample(total_days, len(total_days))
    print(_,test_population[-3:])
    for i in test_population:
        m = m + i
        running_total.append(m)
    #print(f'running_total,{running_total}')

    if max(running_total) == running_total[-1]:

        win_count += 1
        #print(f'win_count: {win_count}')
print(f'Total number of max high finishes divided by total runs: \
     {win_count/total_runs}')

