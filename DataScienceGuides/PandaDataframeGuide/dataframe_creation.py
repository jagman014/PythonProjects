import numpy as np
import pandas as pd
import os

# %%
# creation with dictionaries
# keys -> columns
# values -> data

d = {'x': [1, 2, 3], 'y': np.array([2, 4, 8]), 'z': 100}
df = pd.DataFrame(d)

# %%
# can control index column, and column order

df_1 = pd.DataFrame(d, index=[100, 200, 300], columns=['z', 'y', 'x'])

# %%
# creation with a list of dictionaries, or list of lists
# best to add column labels with lists of lists

l = [{'x': 1, 'y': 2, 'z': 100},
     {'x': 2, 'y': 4, 'z': 100},
     {'x': 3, 'y': 8, 'z': 100}]

l_1 = [[1, 2, 100],
       [2, 4, 100],
       [3, 8, 100]]

df_2 = pd.DataFrame(l)
df_3 = pd.DataFrame(l_1, columns=['x', 'y', 'z'])

# %%
# can also use numpy arrays

arr = np.array([[1, 2, 100],
                [2, 4, 100],
                [3, 8, 100]])

df_4 = pd.DataFrame(arr, columns=['x', 'y', 'z'])

# %%
# default setting copy in df = False:
# changes of array, change df

arr[0, 0] = 1000

# setting copy=True, removes this by making the df a copy of the array

# %%

data = {
    'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
    'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai',
             'Manchester', 'Cairo', 'Osaka'],
    'age': [41, 28, 33, 34, 38, 31, 37],
    'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
}

row_labels = [101, 102, 103, 104, 105, 106, 107]

df_5 = pd.DataFrame(data=data, index=row_labels)

# %%
# can save dataframes to files

directory = os.getcwd()
filename = os.path.join(directory, 'data.csv')

df_5.to_csv(filename)

# %%
# can then reload them to a variable
# sometimes need to specify index column

df_6 = pd.read_csv(filename, index_col=0)
