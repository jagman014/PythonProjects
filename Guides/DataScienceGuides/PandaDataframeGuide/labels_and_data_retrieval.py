import pandas as pd
import numpy as np
import os

# %%
filename = os.path.join(os.getcwd(), 'data.csv')

df = pd.read_csv(filename, index_col=0)

# %%
# obtain row labels with .index, and columns with .columns
# extracted as special sequences

row_labels = df.index

col_labels = df.columns

# %%
# can extract and assign as other sequences
# modifying particular items produce type errors

print(df.columns[1])

df.index = np.arange(10, 17)

# %%
# can convert df to numpy array
# can use either .to_numpy() or .values
# only returns the data of the frame

arr = df.to_numpy()

# %%
# mainly uses numpy array data types
# can obtain / modify dtypes of frame

data_types = df.dtypes

# %%
# dtype keyword argument expects a data type or a dictionary

df_ = df.astype(dtype={'age': np.int32, 'py-score': np.float32})

# %%
# can return properties of dataframe

# number of dimensions
dimensions = df_.ndim

# number of elements per dimension
shape = df_.shape

# number of total elements
size = df_.size

# %%
# can also check memory usage of  columns of the frame
# can remove index usage with index=False
# given in units of bytes

memory = df_.memory_usage()
