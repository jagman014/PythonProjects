# %%
import pandas as pd

nba = pd.read_csv('nba_all_elo.csv')

# %%
# can obtain data subsets with boolean arrays

current_decade = nba[nba['year_id'] > 2010]
print(current_decade.shape)

# %%
# can also use notnull method to return a boolean array
# notna returns a similar result

games_with_notes = nba[nba['notes'].notnull()]
print(games_with_notes.shape)

# %%
# can also use str methods on object types

ers = nba[nba['fran_id'].str.endswith('ers')]
print(ers.shape)

# %%
# can also apply multiple criteria
# '_iscopy' removes duplicate entries
# can only use '&' (AND) and '|' (OR)

print(
    nba[
        (nba['_iscopy'] == 0) &
        (nba['pts'] > 100) &
        (nba['opp_pts'] > 100) &
        (nba['team_id'] == 'BLB')
    ]
)
