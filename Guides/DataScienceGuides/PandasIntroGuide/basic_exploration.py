# %%
import pandas as pd
import numpy as np

nba = pd.read_csv('nba_all_elo.csv')

# %%
# info will display each columns data types and count

nba.info()

# %%
# describe will display basic staticstics of each column

nba.describe()

# %%
# describe only does numeric objects by default
# will display descriptors for no-numerics if included

nba.describe(include=np.object)

# %%
# can use column names in a similar manor to dictionary keys

print(nba['team_id'].value_counts())
print(nba['fran_id'].value_counts())

# %%
# can use loc to return specific values depending on a condition

nba.loc[nba['fran_id'] == 'Lakers', 'team_id'].value_counts()

# %%
# can then apply different aggregate functions to this

nba.loc[nba['team_id'] == 'MNL', 'date_game'].agg(('min', 'max'))
