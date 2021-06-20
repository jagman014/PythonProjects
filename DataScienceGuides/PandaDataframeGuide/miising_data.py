import pandas as pd
import numpy as np

# %%

df = pd.DataFrame({'x': [1, 2, np.nan, 4]})

# %%
# pandas methods innately ignore NaN, unless told not to

print(df.mean())

print(df.mean(skipna=False))

# %%
# .fillna method can get rid of NaN's

# explicit fill
print(df.fillna(value=0))

# fill with value in above row
print(df.fillna(method='ffill'))

# fill with value from row below
print(df.fillna(method='bfill'))

# %%
# can also use interpolation
# can also apply inplace keyword to modify existing dataframe

print(df.interpolate())

# %%
# can also just drop NaN

print(df.dropna())
