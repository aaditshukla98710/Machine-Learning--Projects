# -*- coding: utf-8 -*-
"""Sales Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VBi5DaeznjFLcN2rw_j1fg-UOvR3hVqS
"""

import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns 
import missingno as msno

df_train=pd.read_csv('/content/Train (1).csv',encoding='latin')
df_test=pd.read_csv('/content/Test (1).csv',encoding='latin')

print(df_train.head(),'\n\n')
print(df_test.head())

df_train.shape

print(df_train.describe(),'\n\n')
print(df_test.describe())

df_train['Item_Weight'].describe()

print( df_train.isnull().sum(),'\n\n')
print(df_test.isnull().sum())

print(msno.matrix(df_train),'\n\n')
print(msno.matrix(df_test
))

df_train['Item_Weight'].fillna(df_train['Item_Weight'].mean(),inplace=True)
df_test['Item_Weight'].fillna(df_test['Item_Weight'].mean(),inplace=True)

df_train.isnull().sum()

df_train['Item_Weight'].describe()

df_train['Outlet_Size'].value_counts()

df_train['Outlet_Size'].mode()

df_train['Outlet_Size'].fillna(df_train['Outlet_Size'].mode()[0],inplace=True)
df_test['Outlet_Size'].fillna(df_test['Outlet_Size'].mode()[0],inplace=True)

df_train.isnull().sum()

print(msno.matrix(df_train),'\n\n')
print(msno.matrix(df_test
))

df_train.drop(['Item_Identifier','Outlet_Identifier'],axis=1,inplace=True)
df_test.drop(['Item_Identifier','Outlet_Identifier'],axis=1,inplace=True)

df_train

import dtale

dtale.show(df_train)

from pandas_profiling import ProfileReport

profile = ProfileReport(df_train, title="Pandas Profiling Report")

profile





















