import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({"a": np.random.rand(1000)-1, "b": np.random.rand(1000)+1}, columns=["a", "b"])
print(df)
print(df.plot.hist(bins=20))

plt.show(block=True)