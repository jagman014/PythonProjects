# %%
import pandas as pd

nba = pd.read_csv('nba_all_elo.csv')

city_revenues = pd.Series(
    [4200, 8000, 6500],
    index=['Amsterdam', 'Toronto', 'Tokyo']
)

# %%
# Series data has many different aggregation methods

print(city_revenues.sum())
print(city_revenues.max())

# %%
# Dataframe columns act as Series

points = nba['pts']
print(type(points))

print(points.sum())

# %%
# can aggregate multiple columns in a Dataframe
# groupby defaults to sorting keys

print(
    nba.groupby('fran_id', sort=False)['pts'].sum()
)

# %%
# can also group multiple columns

print(
    nba[
        (nba['fran_id'] == 'Spurs') &
        (nba['year_id'] > 2010)
    ].groupby(['year_id', 'game_result'])['game_id'].count()
)
