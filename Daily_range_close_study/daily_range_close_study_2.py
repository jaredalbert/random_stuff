# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 11:07:23 2021

@author: Windows10
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

path_spy = 'C:/Users/Windows10/Desktop/from old dell/Python_files/Daily_range_close_study/SPY_daily_1993_2021.csv'

def dist(v1, v2):
    return (v1 - v2) /v1 * 100

df = pd.read_csv(path_spy,  parse_dates=True)

df['NormRange'] = dist(df['High'],df['Low'])
df['Bins'] = pd.qcut(df['NormRange'], 10,labels= np.arange(1,11))
df['Bin_vals'] = pd.qcut(df['NormRange'], 10)

df['DistLow'] = dist(df['Close'],df['Low'])
df['DistHigh'] = dist(df['Close'],df['High'])

#sns.scatterplot(data=df,x=df['Date'], y = df['DistHigh'][df['Bins']==10])
sns.distplot(df['DistHigh'][df['Bins']==9],kde=False, color='red', bins=100)
plt.ylabel('Close\'s percentage off the high')
plt.xlabel('histogram bins')
plt.title("Blow up of largest range decile")
#plt.ylim(-4,0)
plt.show()
# sns.swarmplot(x=df['DistLow'], y=df['Bins'])
# plt.xlabel('Close\'s percentage off the low')
# plt.ylabel('Decile rank of the high-low range for that day')
# plt.show()

# sns.swarmplot(x=df['DistHigh'], y=df['Bins'])
# plt.xlabel('Close\'s percentage off the high')
# plt.ylabel('Decile rank of the high-low range for that day')
# plt.show()
