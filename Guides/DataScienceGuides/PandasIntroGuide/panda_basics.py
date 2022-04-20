# %%
import pandas as pd

nba = pd.read_csv('nba_all_elo.csv')
type(nba)

# %%
# len will only return the number of rows
# shape will return the dimensionality

print(len(nba))
print(nba.shape)

# %%
# head will show the first 5 rows

nba.head()

# %%
# can set pandas to display data better in ipython console
# max.columns sets what is shown in the scroll
# precision is for decimal places

pd.set_option('display.max.columns', None)
pd.set_option('display.precision', 2)

# %%
# tail will show the last 5 rows
# as with head you can specify the number of rows in the method

nba.tail()
