# %%
import pandas as pd

nba = pd.read_csv('nba_all_elo.csv')

# %%
# dataframe can be copied with the copy method
# without changing the original dataframe

df = nba.copy()
print(df.shape)

# %%
# can define new columns the same way as dictionary keys

df['difference'] = df.pts - df.opp_pts
print(df.shape)

# %%
# new columns have the same properties as the old ones

print(df['difference'].max())

# %%
# can also rename columns with a dictionary and the rename method
# this returns a new dataframe, can use inplace=True to change the original

renamed_df = df.rename(
    columns={'game_result': 'result', 'game_location': 'location'}
)

print(renamed_df.info())

# %%
# can also remove columns with the drop method

print(df.shape)

elo_columns = ['elo_i', 'elo_n', 'opp_elo_i', 'opp_elo_n']

df.drop(elo_columns, inplace=True, axis=1)

print(df.shape)

# %%

df.to_csv('nba_mod.csv')
