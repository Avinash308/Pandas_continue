# Pandas_continue
working on dataset using pandas, grouping,removing columns and so on

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
df=pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
df.head(5)

#removing Unamed columns
df.drop(df.columns[df.columns.str.contains('Unnamed',case = False)], axis = 1, inplace=True)
df.head(5)

#distribution of male and female
np.round((df['Gender'].value_counts())/len(df)*100,2)

#show top five most preferred names
#Grouping the values on basis of name and count and taking a sum followed by sorting in descending order to get the most #common five names in the data set.

df.groupby('Name')['Count'].sum().sort_values(ascending=False).head(5)

#what is the median name occurance in the dataset
#Finding the median value using Id
df.median()['Id']
#populating median name using ID
df[df['Id'] == df.median()['Id']]['Name']

#DISTRIBUTION OF MALE AND FEMALE BORN COUNT USING STATE
#Grouping the data by state and gender
df.groupby(['State','Gender'])['Count'].sum()

graph = df.groupby(['State','Gender'])['Count'].sum()
graph.unstack().plot(kind='bar',width=0.8,stacked=True, color=['Orange','Blue'], grid=False,figsize=(15,5))
