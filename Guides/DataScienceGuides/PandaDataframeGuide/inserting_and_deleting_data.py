import pandas as pd
import numpy as np
import os

# %%

filename = os.path.join(os.getcwd(), 'data.csv')
df = pd.read_csv(filename, index_col=0)

# %%
# adding a new row data field
# need to set indices to be the same as the df being added to
# name sets the relevant index of the new data series
# can then just .append to the df

john = pd.Series(data=['John', 'Boston', 34, 79], index=df.columns, name=108)

df = df.append(john)

# %%
# can just as easily remove data with .drop
# removes rows specified by the labels keyword in this case

df = df.drop(labels=[108])

# %%
# can add a column in the same manor as a dictionary

df['js-score'] = np.array([71.0, 95.0, 88.0, 79.0, 91.0, 91.0, 80.0])
df['total-score'] = 0.0

# %%
# .insert allows insertion between columns

df.insert(loc=4, column='django-score',
          value=np.array([86.0, 81.0, 78.0, 88.0, 74.0, 70.0, 81.0]))

# %%
# delete columns with del keyword

del df['total-score']

# %%
# or by specifying axis=1 for .drop

df = df.drop(labels='age', axis=1)
