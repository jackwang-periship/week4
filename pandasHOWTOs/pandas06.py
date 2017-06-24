'''
Created on Jun 23, 2017

@author: jwang02
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


new_dataframe = pd.read_csv('../docs//ZIPCodes.csv')
print new_dataframe.describe()
print new_dataframe.columns

print "Doing the grouping by state"
print new_dataframe.groupby("State").sum()