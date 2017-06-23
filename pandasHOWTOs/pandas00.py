'''
Created on Jun 20, 2017

@author: student
'''
import pandasHOWTOs as pd
import numpy as np
# import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])
print s

# s = pandasHOWTOs.Series([1,3,5,np.nan,6,8])


# dates = pd.date_range('20130101', periods=7)

# print dates
# 
# df = pd.DataFrame(np.random.randn(7,4),
#                   index=dates,
#                   columns={'dog', 'cat', 'mouse', 'duck'})
# print df
# 
# df2 = pd.DataFrame( { 'A' : 1.,
#                       'B' : pd.Timestamp('20130102'),  
#                       'C' : pd.Series(1, index=list(range(4)), dtype='float32'),  
#                       'D' : np.array([3] * 4, dtype='int32'),
#                       'E' : pd.Categorical(['test', 'train', 'test', 'train']),
#                       'F' : 1.,
#                     }
#                 )
# print df2


