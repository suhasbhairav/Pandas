import pandas as pd
import numpy as np

s = pd.Series()
print(s)

arr = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(arr)
print(s)

arr = np.array([1,20,198, 8, 89])
s = pd.Series(arr)
print(s)

arr = np.array([1,7,77,2,9,2,8])
s = pd.Series(arr, index=[1,2,3,4,5,6,7])
print(s)

data = {'a': 1, 'b': 0, 'c':2}
s = pd.Series(data)
print(s)

#creating series from scalar
s= pd.Series(10, index=[1,2,3])
print(s)

print(s[1])
print(s[:2])

print(s[[1,3]])