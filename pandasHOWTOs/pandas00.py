'''
Created on Jun 20, 2017

@author: student
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


s = pd.Series([1,3,5,np.nan,6,8])
print s

dates = pd.date_range('20130101', periods=7)
print dates

df = pd.DataFrame(np.random.randn(7,4),
                    index=dates,
                    columns={'dog', 'cat', 'mouse', 'duck'})
print df

df2 = pd.DataFrame( {   'A' : 1.,
                        'B' : pd.Timestamp('20130102'),  
                        'C' : pd.Series(1, index=list(range(4)), dtype='float32'),  
                        'D' : np.array([3] * 4, dtype='int32'),
                        'E' : pd.Categorical(['test', 'train', 'test', 'train']),
                        'F' : 1.,
                     }
                 )
print df2

# We can access the data types of each column in a DataFrame as follows:
print df2.dtypes
print df2.index
print df2.columns
print df2.values

# To get a quick statistical summary of your data, use the :describe() function:
print df2.describe()

# DataFrames have a built-in transpose:
print df.T

