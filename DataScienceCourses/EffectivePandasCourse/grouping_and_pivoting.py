# Example

import pandas as pd
import matplotlib.pyplot as plt

# %%

alta = pd.read_excel('alta.xlsx')


def clean_col(name):
    return name.lower()


def tweak_alta(df):
    return (df
            .rename(columns=clean_col)
            .assign(date=lambda df_: pd.to_datetime(df_.date),
                    year=lambda df_: df_.date.dt.year,
                    tobs_c=lambda df_: (df_.tobs - 32) * (5 / 9)
                    )
            [['date', 'prcp', 'snow', 'snwd', 'tmax', 'tmin', 'tobs', 'tobs_c']]
            )


alta_2 = tweak_alta(alta)

# %%

# sum of the snowfall by year
g_data = (alta_2
          .groupby(alta_2.date.dt.year)
          .snow
          .sum())

# %%

(alta_2
 .groupby(alta_2.date.dt.year)
 .snow
 .sum()
 .plot())

plt.show()

# %%

# maximum snow depth by year
g_data_1 = (alta_2
            .groupby(alta_2.date.dt.year)
            .snwd
            .max())

# %%

(alta_2
 .groupby(alta_2.date.dt.year)
 .snwd
 .max()
 .plot())

plt.show()

# %%

# maximum snow depth by month
(alta_2
 .groupby(alta_2.date.dt.month)
 .snwd
 .max()
 .plot())

plt.show()

# %%

# maximum snow depth by month per year
(alta_2
 .groupby(pd.Grouper(key='date', freq='m'))
 .snwd
 .max()
 .plot())

plt.show()

# %%

# maximum snowfall by ski season
# 'A-JUN' -> Annual ending in June (Jan - Jun)
(alta_2
 .groupby(pd.Grouper(key='date', freq='A-JUN'))
 .snow
 .sum()
 .plot())

plt.show()

# %%

# group by multiple columns
g_data_2 = (alta_2
            .groupby([alta_2.date.dt.year, alta_2.date.dt.month])
            .snwd
            .mean())

# %%

g_data_3 = (alta_2
            .groupby([alta_2.date.dt.year, alta_2.date.dt.month])
            .snwd
            .mean()
            .unstack())

# %%

(alta_2
 .groupby([alta_2.date.dt.year, alta_2.date.dt.month])
 .snwd
 .mean()
 .unstack()
 .plot())

plt.show()

# %%

with plt.style.context('fivethirtyeight'):
    with plt.style.context({'font.family': 'Arial'}):
        (alta_2
         .groupby([alta_2.date.dt.year.rename('year'),
                   alta_2.date.dt.month.rename('month')])
         .snwd
         .mean()
         .unstack()
         .rename(columns=dict(enumerate(
            'Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec'.split(','), 1)))
         .interpolate()
         .plot(cmap='jet', figsize=(12, 4), title='Average Monthly Snow Depth (in)')
         .legend(bbox_to_anchor=(1, 1))
         )

        plt.show()

# %%

with plt.style.context('fivethirtyeight'):
    with plt.style.context({'font.family': 'Arial'}):
        (alta_2
         .groupby([alta_2.date.dt.year.rename('year'),
                   alta_2.date.dt.month.rename('month')])
         .snwd
         .mean()
         .unstack()
         .rename(columns=dict(enumerate(
            'Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec'.split(','), 1)))
         .interpolate()
         .plot.bar(cmap='jet', figsize=(12, 4), title='Average Monthly Snow Depth (in)')
         .legend(bbox_to_anchor=(1, 1))
         )

        plt.show()

# %%

# can have multiple columns
g_data_4 = (alta_2
            .groupby([alta_2.date.dt.year.rename('year'),
                      alta_2.date.dt.month.rename('month')])
            [['snwd', 'snow']]
            .mean()
            .unstack())


# %%

# can have multiple aggregations
def first(s):
    return s.iloc[0]


g_data_5 = (alta_2
            .groupby([alta_2.date.dt.year.rename('year'),
                      alta_2.date.dt.month.rename('month')])
            [['snwd', 'snow']]
            .agg([first, 'median', 'std', 'max']))

# %%

# or per column aggregation
g_data_6 = (alta_2
            .groupby([alta_2.date.dt.year.rename('year'),
                      alta_2.date.dt.month.rename('month')])
            .agg({'snow': ['mean'], 'snwd': ['max', 'min'], 'tobs': [first]}))


# %%

# flatten columns
def to_flat_cols(df_):
    cols = ['_'.join(cs) for cs in df_.columns.to_flat_index()]
    df_.columns = cols
    return df_


g_data_7 = (alta_2
            .groupby([alta_2.date.dt.year.rename('year'),
                      alta_2.date.dt.month.rename('month')])
            [['snwd', 'snow']]
            .agg([first, 'median', 'std', 'max'])
            .pipe(to_flat_cols))

# %%

# flatten index
g_data_8 = (alta_2
            .groupby([alta_2.date.dt.year.rename('year'),
                      alta_2.date.dt.month.rename('month')])
            [['snwd', 'snow']]
            .agg([first, 'median', 'std', 'max'])
            .pipe(to_flat_cols)
            .reset_index())
