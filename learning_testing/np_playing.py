# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:42:32 2019

@author: jaredalbert
"""

import numpy as np
np.random.seed(10)

x = np.random.random((1000, 3))

print (x[:5,:])

diff = x.reshape(1000, 1, 3) - x
print(diff.shape)