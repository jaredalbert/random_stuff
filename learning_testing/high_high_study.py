# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:44:49 2019

@author: jaredalbert
"""
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import pprint


path_spy='C:/Users/jaredalbert/Desktop/python_scripts/GSPC.csv'



df = pd.read_csv(path_spy, parse_dates=True)
df['Date']=pd.to_datetime(df['Date'])
df = df.set_index(df['Date'])

df2 =  df[df['Date'].dt.year>1959]

#df2['250_day_shift']=df2['Adj Close'].diff(periods = 250)
df2['Highest'] = df2['Adj Close'].rolling(window =250).max()
df2['Lowest'] = df2['Adj Close'].rolling(window =250).min()
#df2['Highest_out'] = df2['Adj Close'].rolling(window = -250)
df3= df2[['Date',  'Adj Close', 'Highest', 'Lowest']]
df3['shift_close'] = df3['Adj Close'].shift(-250)
df3['ln_change'] = np.log(df3['Adj Close']/df3['Adj Close'].shift(-250))
df3['today_highest'] = np.where(df3['Highest']==df3['Adj Close'], True, False)
df3['high_forcast'] = df3['ln_change'][np.where(df3['Highest']==df3['Adj Close'], True, False)]
df3['today_lowest'] = np.where(df3['Lowest']==df3['Adj Close'], True, False)
df3['low_forcast'] = df3['ln_change'][np.where(df3['Lowest']==df3['Adj Close'], True, False)]
print(f"high forcast: {df3['high_forcast'].describe()}")
print(f"low forcast: {df3['low_forcast'].describe()}")


#print (df3['today_highest'].sum()/df3.shape[0])
#
#df4=df3['Date'][df3['today_highest']].dt.month
#
#
#df4.hist(bins = 12)
#plt.show()
#changes = []
#for i in range(-20,20):
#    df2['ln_change'] = np.log(df2['Adj Close']/df2['Adj Close'].shift(i))
#    mean_change = df2[df2.Date.isin(df.IPO_date)].ln_change.mean()
#    changes.append((i, format(mean_change,'.4f')))
#
#
#change = pd.DataFrame(changes, columns=['offset', 'ln_change'])
#change.offset = change.offset.astype('int')
#change.ln_change = change.ln_change.astype('float')
#
#
#change.plot(x='offset', y='ln_change')
#plt.title('Mean LN return of SPY to IPO Date which is date 0 on the chart')
#plt.ylabel('Natural log change between the offset day and the IPO day')
#plt.xlabel('Days around the IPO. Day 0 is the IPO day')
#plt.show()

