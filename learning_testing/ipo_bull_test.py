# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 20:31:14 2019

@author: jaredalbert
"""

import pandas  as pd
import numpy as np

my_dict = {'date': ['3/2/16/', '3/3/16', '3/4/16'], 'price': [ 1, 2, 3]}
my_dict2 = {'date': ['4/2/16/', '4/3/16', '4/4/16'], 'price': [ 10, 20, 30]}
print(my_dict)

pd_dict =  pd.DataFrame.from_dict(my_dict)
pd_dict['date']=pd.to_datetime(pd_dict['date'])

pd_dict['log_ret'] = np.log(pd_dict.price/pd_dict.price.shift(1))
pd_dict2 =  pd.DataFrame.from_dict(my_dict2)
pd_dict2['date']=pd.to_datetime(pd_dict2['date'])



pd_dict= pd_dict.append(pd_dict2, ignore_index = True)
pd_dict['log_ret'] = np.log(pd_dict.price) - np.log(pd_dict.price.shift(1))

pd_dict['pct_ret']= pd_dict['price'].pct_change()
print(pd_dict)
#print (pd_dict[pd_dict['date'].isin(['2016-03-02', '2016-04-02' ])])
