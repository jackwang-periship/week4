'''
Created on Jun 23, 2017

@author: jwang02
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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

# We can also sort a DataFrame along a given data dimension. 
# For example, we might want to sort by the values in column B:
# print df.sort_values(columns='dog')

# We can also sort the rows (axis = 0) and columns (axis = 1) by their index/header values:
#print df.sort_index(axis=0, ascending=False)
# print df.sort_index(axis=1)

print "To select only only the first few rows of a DataFrame, use the :head() function"
print df.head()
print ""
print "To view only the last few rows, use the :tail() function. Note that by default, "
print "both :head() and :tail() return 5 rows. You can also specify the number you want"
print "by passing in an integer."
print df.tail(2)
print ""
print "Selecting a single column yields a Series, equivalent to df:cat:"
print df['cat']
print ""
print "We can also select a subset of the rows using slicing."
print "You can select either by integer indexing:"
print df[1:4]
print "Or by value (for example, slicing on a date range might come in handy):"
print df['20150127':'20150129']
print ""
print "To select more than one column at a time, try :loc[]):"
print df.loc[:,['cat','dog']]
print ""
print "And of course, you might want to do both at the same time:"
print df.loc['20150127':'20150129',['cat','dog']]

print ""
print "*****************************"
print "Boolean Indexing"
# Sometimes it's useful to be able to select all rows that meet some criteria. 
# For example, we might want all rows where the value of cat is greater than 0:
print df[df['cat'] > 0]
# Or perhaps we'd like to eliminate all negative values:
nonneg_only = df[df > 0]
print nonneg_only
# And then maybe we'd like to drop all the rows with missing values:
print nonneg_only.dropna()
# Oops. . . maybe not. How about we set them to zero instead?
print nonneg_only.fillna(value=0)
# But what if your values aren't numeric? No problem, we can also do ltering. First, let's copy the
# DataFrame and add a new column of nominal values:
df2 = df.copy()
df2['color'] = ['blue', 'green','red','blue','green','red','blue']
print df2
# Now we can use the :isin() function to select only the rows with `green' or `blue' in the color column:
print df2[df2['color'].isin(['green','blue'])]

print ""
print "*****************************"
print "Basic Math"
print "It's simple to get the mean across all numeric columns:"
print df.mean()
print "We can also perform the same operation on rows:"
print df.mean(1)
print "Median also behaves as expected:"
print df.median()
print "You can also use the :apply() function to evaluate functions to the data."
print "For example, we might want to perform a cumulative summation (thanks, numpy!):"
print df.apply(np.cumsum)
print "Or apply your own function, such as Finding the spread (max value - min value):"
print df.apply(lambda x: x.max() - x.min())