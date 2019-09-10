#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 22:16:40 2019

@author: Matias Montesinos
"""


import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import style

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2019, 1, 11)


df = web.DataReader("AAPL", 'yahoo', start, end)

#print(df.tail())

close_px = df['Adj Close']

#print(close_px[-1]) #print the last value


mavg = close_px.rolling(window=50).mean()

print(mavg)

close_px.plot(label='AAPL')
mavg.plot(label='mavg')
plt.legend()
plt.show()

