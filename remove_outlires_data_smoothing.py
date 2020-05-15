# -*- coding: utf-8 -*-
"""
Created on Fri May 15 18:55:08 2020

@author: marcin
"""

from scipy.stats import iqr
data = [-2,8,13,19,34,49,50,53,59,64,87,89,1456]

print(iqr(data, axis=0))


import numpy as np
Q1 = np.quantile(data,0.25)
Q3 = np.quantile(data,0.75)
IQR = Q3 - Q1

print(IQR)


import pandas as pd
from scipy import stats
df=pd.DataFrame({'data':[-2,8,13,19,34,49,50,53,59,64,87,89,1456]})
df['z_score']= stats.zscore(df['data'])

print(df)

print(
df.loc[df['z_score'].abs()<=3], '\n\n'
)



# Finding Exponential Smoothing values using Pandas
df['ewm_alpha_1']=df['data'].ewm(alpha=0.1).mean()
df['ewm_alpha_3']=df['data'].ewm(alpha=0.3).mean()
df['ewm_alpha_6']=df['data'].ewm(alpha=0.6).mean()
print(df)