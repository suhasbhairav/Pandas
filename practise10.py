import pandas as pd
import numpy as np

s = pd.Series([1,2,3,4,5])
print(s.pct_change())

s = pd.DataFrame(np.random.randn(7, 2))
print(s)
print(s.pct_change())


#covariance is applied on series data

s1 = pd.Series(np.random.randn(10))
s2 = pd.Series(np.random.randn(10))

print(s1.cov(s2))

s3 = pd.Series(np.random.randn(10))
s4 = pd.Series(np.random.randn(10))
print(s3.cov(s4))

#Covariance on Dataframe computes COV for all the columns

s3 = pd.DataFrame(np.random.randn(5,2), columns=['A', 'B'])
print(s3['A'].cov(s3['B']))


#Correlation
print(s3['A'].corr(s3['B']))

#Ranking
print(s3.rank())