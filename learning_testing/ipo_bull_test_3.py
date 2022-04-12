# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:44:49 2019

@author: jaredalbert
"""
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

path_ipo = 'C:/Users/jaredalbert/Desktop/python_scripts/IPO_Study/25_biggest_us_IPOs.csv'
path_spy='C:/Users/jaredalbert/Desktop/python_scripts/IPO_Study/SPY.csv'

df = pd.read_csv(path_ipo, names = ['ticker', 'IPO_date', 'valuation'], parse_dates=True)
df['IPO_date']=pd.to_datetime(df['IPO_date'])


df2 = pd.read_csv(path_spy, parse_dates=True)
df2['Date']=pd.to_datetime(df2['Date'])
df2 = df2.set_index(df2['Date'])

changes = []
for i in range(-20,20):
    df2['ln_change'] = np.log(df2['Adj Close']/df2['Adj Close'].shift(i))
    mean_change = df2[df2.Date.isin(df.IPO_date)].ln_change.mean()
    changes.append((i, format(mean_change,'.4f')))


change = pd.DataFrame(changes, columns=['offset', 'ln_change'])
change.offset = change.offset.astype('int')
change.ln_change = change.ln_change.astype('float')


change.plot(x='offset', y='ln_change')
plt.title('Mean LN return of SPY to IPO Date which is date 0 on the chart')
plt.ylabel('Natural log change between the offset day and the IPO day')
plt.xlabel('Days around the IPO. Day 0 is the IPO day')
plt.show()

