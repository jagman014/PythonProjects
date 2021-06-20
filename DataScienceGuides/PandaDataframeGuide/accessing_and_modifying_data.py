#%%
import pandas as pd
import numpy as np
import os

filename = os.path.join(os.getcwd(), 'data.csv')
df = pd.read_csv(filename, index_col=0)

# %%
# can get rows and columns in the usual manor

names = df['name']

row_1 = df.loc[101]

# %%
# can also use accessors
# .loc uses labels
# .iloc uses integer indices
# also .at and .iat for single elements

first_row = df.iloc[0]

# %%
# both also support slicing

cities = df.loc[:, 'city']
# iloc equivalent -> .iloc[:, 1]

sliced_df = df.loc[102:106, ['name', 'city']]
# iloc equivalent -> .iloc[1:6, [0, 1]]

# loc indices are of the closed interval (inclusive start and end)
# iloc follows pythons half open interval (inclusive start, exclusive end)

# %%
# can set data in the same manor as other data types

df.loc[:104, 'py-score'] = [40, 50, 60, 70]
df.loc[105:, 'py-score'] = 0

# %%
# can also use negative indexing with iloc

df.iloc[:, -1] = np.array([88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0])
