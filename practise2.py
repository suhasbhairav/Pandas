import pandas as pd
import numpy as np

df = pd.DataFrame()
print(df)

data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data)
print(df)

data = [10, 230, 39.2, 34, 78, 9, 15]
df = pd.DataFrame(data)
print(df)

data = [['Alex', 10], ['Bob', 12], ['Camel', 25], ['Elephant', 23]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)

data = [['Parrot', 2], ['Pigeon', 29], ['Cow', 15]]
df = pd.DataFrame(data, columns=['Name', 'Sum'])
print(df)

data = [['SB', 121], ['BK', 12], ['SS', 45]]
df = pd.DataFrame(data, columns=['Initials', 'Number'], dtype=float)
print(df)

data = [['SB', 121, 8.9], ['AB', 26, 98.9], ['AK', 78, 9.1]]
df = pd.DataFrame(data, columns=['Initials', 'Sum', 'Diff'])
print(df)

del df['Diff']
print(df)

df.pop('Sum')
print(df)
d = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
}

d1 = {
    'three': pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f']),
    'four': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
}
df2 = pd.DataFrame(d1)
df = pd.DataFrame(d)
print(df)

print(df.loc['b'])

print(df.iloc[2])
print(df.iloc[1:3])
print(df[1:3])

df = df.append(df2)
print(df)

df = df['one']
print(df)

df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a', 'b'])
df = df.append(df2)

print(df)

df = df.drop(0)
print(df)
