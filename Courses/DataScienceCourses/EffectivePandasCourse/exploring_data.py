# Examples
import pandas as pd
from IPython.display import display

# %%

alta = pd.read_excel('alta.xlsx', index_col=0)

# %%

# access methods on column names
# data.COLUMN_NAME.method or data['COLUMN_NAME'].method

# %%

types = alta.dtypes

# %%

# method
alta.info()

# %%

# methods are callable can take parameters have () after
# properties are not callable don't take ()

# %%

# top 5 rows, .T -> transpose
head = alta.head().T

# %%

sample = alta.sample(5)

# %%

shape = alta.shape  # returns (# of rows, # of columns)

# %%

index = alta.index  # returns Int64Index, returns index

# %%

with pd.option_context('display.min_rows', 3):
    display(alta)

# %%

# display select amount of rows or columns in the console
with pd.option_context('display.max_columns', 4):
    display(alta)
