import numpy as np
import pandas as pd

s = pd.Series(np.random.randn(5))
print(s)

print(s.axes)
print(s.empty)
print(s.ndim)

print(s.size)
print(s.values)

print(s.head())
print(s.tail())

d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8])}

df = pd.DataFrame(d)
print(df)

# transpose - rows and columns will interchange
print(df.T)
print(df.axes)
print(df.ndim)
print(df.size)
print(df.shape)
print(df.empty)
print(df.head())
print(df.head(3))
print(df.tail())
print(df.values)
