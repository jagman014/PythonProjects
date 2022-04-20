import pandas as pd
import numpy as np
import os

# %%

filename = os.path.join(os.getcwd(), 'data.csv')
df = pd.read_csv(filename, index_col=0)

df['js-score'] = np.array([71.0, 95.0, 88.0, 79.0, 91.0, 91.0, 80.0])
df.insert(loc=4, column='django-score',
          value=np.array([86.0, 81.0, 78.0, 88.0, 74.0, 70.0, 81.0]))

# %%
# pandas dataframes / series can be fed into numpy / scipy functions
# i.e. numpy weighted average

df['total'] = np.average(df.iloc[:, 3:6], axis=1, weights=[0.4, 0.3, 0.3])

# %%

df.to_csv(os.path.join(os.getcwd(), 'data_1.csv'))
