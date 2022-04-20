import pandas as pd
import os

# %%

df = pd.read_csv(os.path.join(os.getcwd(), 'data_1.csv'), index_col=0)

# %%
# .items / .iteritems methods return column iterable
# returns a tuple with column names and the column as a Series

for col_label, col in df.iteritems():
    print(col_label, col, sep='\n', end='\n\n')

# %%
# similar with the .iterrows method
# returns a tuple of row label and row data as a Series

for row_label, row in df.iterrows():
    print(row_label, row, sep='\n', end='\n\n')

# %%
# .itertuples iterates over rows returning named tuples
# name keyword set to 'Pandas' by default, index is also True by default

for row in df.loc[:, ['name', 'city', 'total']].itertuples():
    print(row)
