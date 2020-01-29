# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:24:41 2020

@author: usama
"""

import pandas as pd
df = pd.read_csv ('traibn.csv')
df.dropna(axis=0, how='all',inplace=True)
df.to_csv('traibn_copy.csv', index=False)
df1 = pd.read_csv ('traibn_copy.csv')
columns = ['seconds_passed','sat_id','x_sim','y_sim','z_sim']
columns2 = ['seconds_passed','sat_id','Vx_sim','Vy_sim','Vz_sim']
columns3 = ['seconds_passed','sat_id','x','y','z']
columns4 = ['seconds_passed','sat_id','Vx','Vy','Vz']
for i in columns:
    df1[columns].to_csv('train.csv')
for i in columns2:
    df1[columns2].to_csv('train2.csv')
for i in columns3:
    df1[columns3].to_csv('train3.csv')
for i in columns4:
    df1[columns4].to_csv('train4.csv')