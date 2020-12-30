import pandas as pd
import numpy as np

print(pd.get_option("display.max_rows"))

pd.set_option("display.max_rows", 100)
print(pd.get_option("display.max_rows"))

pd.reset_option("display.max_rows")

print(pd.get_option("display.max_rows"))