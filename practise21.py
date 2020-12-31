import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(10,4), columns=list('ABCD'))
print(df)
print(df.plot.bar(stacked=True))
plt.show(block=True)
