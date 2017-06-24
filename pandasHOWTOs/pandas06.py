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

sub_dataframe = new_dataframe[['State','Population','WhitePopulation','BlackPopulation','HispanicPopulation','AsianPopulation','HawaiianPopulation','IndianPopulation','OtherPopulation']].copy()
print "Doing the grouping by state"
sum_frame = sub_dataframe.groupby(['State'], sort=False).sum()
print sum_frame.sort_values (['Population'], ascending=[False])