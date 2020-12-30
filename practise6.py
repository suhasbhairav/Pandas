import pandas as pd

import numpy as np

#when you iterate a df, you get column names

N=20
df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
   })

for col in df:
    print(col)


df = pd.DataFrame(np.random.randn(10,3), columns=['c1','c2','c3'])

print(df)
for key, value in df.iteritems():
    print(key, value)


for row_index, row in df.iterrows():
    print(row_index, row)

for row in df.itertuples():
    print(row)