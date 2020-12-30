import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John   ', 'Alber@t', np.nan, '1234','SteveSmith'])

print(s)

print(s.str.lower())

print(s.str.upper())

print(s.str.len())

print(s.str.strip())

print(s.str.split(" "))

print(s.str.get_dummies())

print(s.str.contains(" "))

print(s.str.replace("a", "b"))

print(s.str.islower())