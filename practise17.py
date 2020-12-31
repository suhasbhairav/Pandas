import pandas as pd
import numpy as np

print(pd.Timedelta("2 days 2 hours 2 minutes 2 seconds"))

print(pd.Timedelta("20 days 20 hours 20 minutes 25 seconds"))

print(pd.Timedelta(days=2, hours=24, minutes=20, seconds=10, milliseconds=100, microseconds=600))

s = pd.Series(pd.date_range("2021-1-1", periods=4, freq="D"))
print(s)

s = pd.Series(pd.date_range("2021-1-1", periods=4, freq="h"))
print(s)

s = pd.Series(pd.date_range("2021-1-1", periods=4, freq="D"))
print(s)

td = pd.Series([pd.Timedelta(days=i) for i in range(4)])

print(td)

df = pd.DataFrame(dict(A=s, B=td))
print(df)

df['C'] = df['A'] + df['B']
print(df)

df['D'] = df['A'] - df['B']
print(df)