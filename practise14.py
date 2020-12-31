import pandas as pd
import numpy as np

left = pd.DataFrame({
   'id':[1,2,3,4,5],
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5']})

right = pd.DataFrame({'id':[1,2,3,4,5],
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5']})

print(left)
print(right)

print(pd.merge(left, right, on="id"))

print(pd.merge(left, right, on="subject_id"))

print(pd.merge(left, right, on=['id', 'subject_id']))

print(pd.merge(left, right, on=["id", "subject_id"], how="left"))

print(pd.merge(left, right, on=["id", "subject_id"], how="right"))

print(pd.merge(left, right, on=["id"], how="outer"))

print(pd.merge(left, right, on=["id"], how="inner"))

