# Example
import pandas as pd
import sqlite3

url = ('https://github.com/mattharrison/datasets/raw/master/' +
       'data/alta-noaa-1980-2019.csv')
alta = pd.read_csv(url)

# %%
# save as excel file
alta.to_excel('alta.xlsx')

# %%
alta_2 = pd.read_excel('alta.xlsx', index_col=0)
# index_col=0 used as index was written to file

# %%
# save as sql
con = sqlite3.connect('alta.db')
con.execute("DROP TABLE IF EXISTS alta")
alta.to_sql('alta', con)

# %%
alta_3 = pd.read_sql('SELECT * from alta', con)
