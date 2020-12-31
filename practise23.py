import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({'A': np.random.rand(1000)-1, 'B': np.random.randn(1000)+1 }, columns=list("AB"))
print(df)
print(df.plot.hist())
plt.show(block=True)