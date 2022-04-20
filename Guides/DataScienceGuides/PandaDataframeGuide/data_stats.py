import pandas as pd
import os

# %%

filename = os.path.join(os.getcwd(), 'data_1.csv')
df = pd.read_csv(filename, index_col=0)

# %%
# .describe method provides many statistical methods on the dataframe
# count, mean, standard deviation, min, max, and quartiles

print(df.describe())

# %%
# each statistic in describe has a separate method
# can apply to entire dataframe or individual columns

print(df.mean())
