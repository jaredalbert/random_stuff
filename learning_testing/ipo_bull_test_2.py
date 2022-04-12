# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:44:49 2019

@author: jaredalbert
"""
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
#df = pd.read_csv('c:/Users/jaredalbert/Desktop/python scripts/IPO Study/file:///C:/Users/jaredalbert/Desktop/python scripts/IPO Study/25_biggest_us_IPOs')

path_ipo = 'C:/Users/jaredalbert/Desktop/python_scripts/IPO_Study/25_biggest_us_IPOs.csv'
path_spy='C:/Users/jaredalbert/Desktop/python_scripts/IPO_Study/SPY.csv'
df = pd.read_csv(path_ipo, names = ['ticker', 'IPO_date', 'valuation'], parse_dates=True)
df['IPO_date']=pd.to_datetime(df['IPO_date'])
dates = list(df['IPO_date'])

df2 = pd.read_csv(path_spy, parse_dates=True)
df2['Date']=pd.to_datetime(df2['Date'])
#df2['ln_change']=np.log(df2['Adj Close']/df2['Adj Close'].shift(-20))
df2 = df2.set_index(df2['Date'])

changes = []
for i in range(-20,20):
    df2['ln_change'] = np.log(df2['Adj Close']/df2['Adj Close'].shift(i))
    df3 = df2[df2.Date.isin(df.IPO_date)].ln_change.mean()
    print(format(df3, '.4f'))
    changes.append((i, format(df3,'.4f')))
#print(changes)
change = pd.DataFrame(changes, columns=['offset', 'ln_change'])
change.offset = change.offset.astype('int')
change.ln_change = change.ln_change.astype('float')
print(change.dtypes)
change.plot(x='offset', y='ln_change')
plt.title('Mean LN return of SPY to IPO Date which is date 0 on the chart')
plt.ylabel('Natural log change between the offset day and the IPO day')
plt.xlabel('Days around the IPO. Day 0 is the IPO day')

plt.show()

#print(dates[0])
#print(df2.loc[df['IPO_date']])
#for i in dates:
#    #print(i, dates[0])
#    print(df2.loc[i])
#print(df[df['IPO_date']< datetime.datetime(2002,12,31)].sort_values('IPO_date',ascending=False).count())
#df3 = df2[df2.Date.isin(df.IPO_date)]
#print(f'mean: ',format(df3.ln_change.mean(),'.4f'),
#      f'Std: ',format(df3.ln_change.std(),'.4f'))
