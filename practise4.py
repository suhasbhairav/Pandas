import pandas as pd
import numpy as np

#Descriptive Statistics

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}

df = pd.DataFrame(d)
print(df)

print(df.sum())

print(df.sum(1))

print(df.mean())

print(df.std())

print(df.count())

print(df.median())

print(df.mode())

print(df.min())

print(df.max())

