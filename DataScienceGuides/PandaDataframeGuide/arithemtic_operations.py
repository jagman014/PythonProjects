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
# can apply vectorised calculations to data columns

print(df['py-score'] + df['js-score'])

print(df['py-score'] / 100)

# %%
# can also insert calculations into columns

df['total'] = 0.4 * df['py-score'] + 0.3 * df['django-score'] + 0.3 * df['js-score']
