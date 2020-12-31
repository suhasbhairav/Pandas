import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(10,4), index=pd.date_range("1/1/2021", periods=10), columns=list('ABCD'))
print(df)

print(df.plot())
plt.show(block=True)

