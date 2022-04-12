# -*- coding: utf-8 -*-
import numpy as np
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt


"""
Created on Mon Mar 18 19:52:17 2019

@author: jaredalbert
"""
'''Dice roll simulator'''
np.random.seed = 1


class Dice_sim:
    def __init__(self, num_dice=2, num_sides=6, num_rolls=60):
        self.num_dice = num_dice
        self.num_sides = num_sides
        self.num_rolls = num_rolls

    def __str__(self):
        return 'dice simulator'

    def roll(self):
        roll_list = []
        for _ in range(self.num_rolls):
            rolls = np.sum(np.random.choice(self.num_sides , self.num_dice, replace = True) + 1)
            roll_list.append(rolls)
        c = (Counter(roll_list))
        df = pd.DataFrame.from_dict(c, orient = 'index').reset_index()
        df.columns = ['keys', 'sums']
        df.set_index('keys', drop = True, inplace = True )
        df.sort_index(inplace = True)
        df.plot()
        plt.show()
        return sorted(c.items()), #df, pd.crosstab(df.index, df.sums) #pd.crosstab(index = c.keys(), columns = c.values())
            
            