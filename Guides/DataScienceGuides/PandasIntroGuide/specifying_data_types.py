# %%
import pandas as pd

df = pd.read_csv('nba_mod.csv', index_col=0)

# %%

print(df.info())

# %%
# some columns need to be converted into appropriate data types

df['date_game'] = pd.to_datetime(df['date_game'])
print(repr(df['date_game'].dtype))

# %%
# some columns can become categorical (like factors in R)
# defaults to ordered=False

print(df['game_location'].nunique())
print(df['game_location'].value_counts())

df['game_location'] = pd.Categorical(df['game_location'])
print(repr(df['game_location'].dtype))

# %%
# changing to appropriate data types can save on memory

print(df.info())
