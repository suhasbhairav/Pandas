import pandas as pd
import numpy as np

#.loc() -> label based
#.iloc() -> integer based
#.ix() -> both label and integer based


df = pd.DataFrame(np.random.rand(8,4), index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], columns=['A', 'B', 'C', 'D'])

print(df.loc[:, ['A', 'C']])

print(df.loc[['a', 'b'], ['A', 'D']])

print(df.loc[['a', 'c'], ['B', 'D']])

print(df.loc['a':'h'])

print(df.loc['a']>0.8)

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
print(df.iloc[:2])

print(df.iloc[:5, 2:4])

print(df.iloc[1:3, 1:3])

print(df['A'])
print(df[0:2])
