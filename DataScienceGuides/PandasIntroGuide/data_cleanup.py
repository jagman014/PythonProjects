# %%
import pandas as pd

nba = pd.read_csv('nba_all_elo.csv')

# %%
# info method will show all non-null counts

print(nba.info())

# %%
# easiest method to deal with missing data is to ignore it
# this is done with the dropna method

rows_without_missing_data = nba.dropna()
print(rows_without_missing_data.shape)

# %%
# a more sensible solution would be to drop the missing columns
# done by defining the axis keyword

data_without_missing_columns = nba.dropna(axis=1)
print(data_without_missing_columns.shape)

# %%
# can replace missing data with the fillna method

data_with_default_notes = nba.copy()

data_with_default_notes['notes'].fillna(
    value='no notes at all',
    inplace = True
)

print(data_with_default_notes['notes'].describe())

# %%
# invalid and inconsistent data can give unexpected results
# for this example any forfeited or any win / loss inconsistencies

print(nba[nba.pts == 0])

print(
    nba[
        (nba.pts > nba.opp_pts) &
        (nba.game_result != 'W')
    ].empty
)

print(
    nba[
        (nba.pts < nba.opp_pts) &
        (nba.game_result != 'L')
    ].empty
)
