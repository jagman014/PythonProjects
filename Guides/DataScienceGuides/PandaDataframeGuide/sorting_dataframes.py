import pandas as pd
import os

# %%

filename = os.path.join(os.getcwd(), 'data_1.csv')
df = pd.read_csv(filename, index_col=0)

# %%
# uses .sort_values method, can pass the axis keyword to change between rows and columns
# inplace keyword will overwrite the dataframe with the sorted data

print(df.sort_values(by='js-score', ascending=False))

# %%
# can sort multiple rows as well

print(df.sort_values(by=['total', 'py-score'], ascending=[False, False]))
