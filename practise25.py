import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.DataFrame(np.random.rand(10,5), columns=list("ABCDE"))
print(df)
print(df.plot.box())

plt.show(block=True)

