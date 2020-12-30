import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'], columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print(df)

print(df.isnull())

print(df['one'].isnull())

print(df['one'].notnull())

print(df['one'].sum())

print(df['two'].sum())

print(df.fillna(0))

print(df.fillna(method="pad"))
print(df.fillna(method="bfill"))

print(df.dropna())

print(df.dropna(axis=1))