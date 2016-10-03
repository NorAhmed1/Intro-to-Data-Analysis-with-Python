import pandas as pd
import numpy
import seaborn

# SERIES

s = pd.Series([0,1,4,9,16,25],name='squares')
    # be careful b/c the "Series" call is case sensitive
print (s)

print (s.values)

print (s.index)
print (s[0])
print (s[2:4])

pop2014 = pd.Series([100,99.3,95.5,93.5,92.4,84.8,84.5,78.9,74.3,72.8], index=['Java','C','C++','Python','C#','PHP','JavaScript','Ruby','R','Matlab'])
print (pop2014)
                                                                               
print (pop2014.index)
print (pop2014[0:2])
print (pop2014['C++':'C#'])

print (pop2014.iloc[0:2])
    # iloc specifies that you're using numbers
print (pop2014.loc[:'Ruby'])
    # loc specifies that you're using explicit values

print (pop2014[pop2014 > 90])
    # this advanced indexing technique is called a Boolean mask

# you can also create a series from a python dictionary
pop2015 = pd.Series({'Java': 100,'C': 99.9,'C++': 99.4,'Python': 96.5,'C#': 91.3,'R': 84.8,'PHP':84.5,'JavaScript':83.0,'Ruby':76.2,'Matlab':72.4})
print (pop2015)


# DATAFRAMES

twoyears = pd.DataFrame({'2014': pop2014,'2015': pop2015})
print (twoyears)

twoyears = twoyears.sort_values(by='2015',ascending=False)
print (twoyears)
print (twoyears.values)
print (twoyears.index)
print (twoyears.columns)
print (twoyears.iloc[0:2])
print (twoyears.loc['C':'Python'])

twoyears['avg'] = 0.5*(twoyears['2014'] + twoyears['2015'])
    # adds a new column for average between the two years
print (twoyears)
                       

presidents = pd.DataFrame([{'name': 'Barack Obama','inauguration': 2009,'birthyear':1961},
                          {'name': 'George W. Bush','inauguration': 2001,'birthyear':1946},
                          {'name': 'Bill Clinton','birthyear': 1946,'inauguration':1993},
                          {'name': 'George H. W. Bush','birthyear':1924,'inauguration':1989}])
print (presidents)

# can set one of the columns as the ser index:
presidents_indexes = presidents.set_index('name')
print (presidents_indexes)

print (presidents_indexes.loc['Bill Clinton'])
print (presidents_indexes.loc['Bill Clinton']['inauguration'])

presidents_fathers = pd.DataFrame([{'son':'Barack Obama', 'father': 'Barack Obama Sr.'},
                                   {'son': 'George W. Bush','father':'George H. W. Bush'},
                                   {'son': 'George H. W. Bush','father':'Prescott Bush'}])
merged_table = pd.merge(presidents,presidents_fathers,left_on='name',right_on='son').drop('son',axis=1)
print(merged_table)

merged_table2 = pd.merge(presidents,presidents_fathers,left_on='name',right_on='son',how='left').drop('son',axis=1)
print(merged_table2)
    # now Bill Clinton is included


# MULTILEVEL INDEXES

flights = seaborn.load_dataset('flights')
print (flights.head())
flights_indexed = flights.set_index(['year','month'])
print (flights_indexed.head())

print (flights_indexed.loc[1949:1950])

flights_unstacked = flights_indexed.unstack()
print (flights_unstacked)

print (flights_unstacked.sum(axis=1))
flights_unstacked['passengers','total'] = flights_unstacked.sum(axis=1)
print (flights_unstacked)

flights_restacked = flights_unstacked.stack()
print (flights_restacked)

print (flights_restacked.loc[pd.IndexSlice[:,'total'],'passengers'])
print (flights_restacked[flights_restacked['passengers'] > 120])


# AGGREGATING DATA

open('tips.csv','r').readlines()[:10]

tips = pd.read_csv('tips.csv')
print (tips.head())                   
print (tips.mean())
print (tips.describe())

print (tips.groupby('sex').mean())
print (tips.groupby(['sex','smoker']).mean())
   # this creates a pandas multidimensional index

# pivot tables babyyyyyyy
print (pd.pivot_table(tips,'total_bill','sex','smoker'))
print (pd.pivot_table(tips,'total_bill',['sex','smoker'],['day','time']))
