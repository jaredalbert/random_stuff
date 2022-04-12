# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 16:49:00 2020

@author: jaredalbert
"""

import pandas as pd
import numpy as np
import scipy
from sklearn.preprocessing import StandardScaler
import scipy.stats
import matplotlib.pyplot as plt
#%matplotlib inline
# Load data and select first column

from sklearn import datasets
path_spy='C:/Users/jaredalbert/Desktop/python_scripts/GSPC.csv'



df = pd.read_csv(path_spy, parse_dates=True)
df['Date']=pd.to_datetime(df['Date'])
df = df.set_index(df['Date'])
df['ln_change'] = np.log(df['Adj Close']/df['Adj Close'].shift(1))

data_set = datasets.load_breast_cancer()
y=data_set.data[:,0]

# Create an index array (x) for data

x = np.arange(len(y))
size = len(y)