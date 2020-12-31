import pandas as pd
import numpy as np

s = pd.Series(["a", "b", "a", "c", "d", "b"], dtype="category")
print(s)

s1 = pd.Categorical(["A", "b", "B", "A", "a"], ordered=True)
print(s1)

print(s1.describe())

s1.categories = ["Group %s" %  g for g in s1.categories]
print(s1)

print(s1.remove_categories("Group a"))