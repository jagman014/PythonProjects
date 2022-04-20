# %%
%matplotlib inline
import pandas as pd

nba = pd.read_csv('nba_all_elo.csv')

# %%
# series and dataframe objects have a plot method

(
    nba[nba['fran_id'] == 'Knicks']
    .groupby('year_id')
    .pts
    .sum()
    .plot()
)

# %%
# can also define the type of plot with the 'kind' keyword

(
    nba
    .fran_id
    .value_counts()
    .head(10)
    .plot(kind='bar')
)
