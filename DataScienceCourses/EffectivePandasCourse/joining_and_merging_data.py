# Example

import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

# %%

# remove non-data rows, set dates as index
part_df = pd.read_csv('2004-PM2.5.csv', skiprows=2, parse_dates=[0])

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

# change datetime info from hourly to daily
part_df_2 = part_df.groupby(pd.Grouper(key='Date', freq='D')).mean().reset_index()

# %%

part_df_2.set_index('Date').plot()

plt.show()

# %%

# .join goes from index not dates
j_data = (alta_2
          .join(part_df_2)
          .set_index('date')
          .loc[lambda df_: df_.index.year == 2004]
          .isna().mul(100).mean())

# %%

# left df is first, right is second
j_data_1 = (alta_2
            .merge(part_df_2, left_on='date', right_on='Date')
            .set_index('date')
            .loc[lambda df_: df_.index.year == 2004]
            .isna().mul(100).mean())

# %%

j_data_2 = (alta_2
            .merge(part_df_2, left_on='date', right_on='Date')
            .corr())

# %%

(alta_2
 .merge(part_df_2, left_on='date', right_on='Date')
 .plot.scatter(x='UG/M3', y='snwd', alpha=.2))

plt.show()

# %%

(alta_2
 .merge(part_df_2, left_on='date', right_on='Date')
 .set_index('date')
 [['snwd', 'UG/M3']]
 .plot())

plt.show()

# %%

# join types demo
df_1 = pd.DataFrame({'name': ['Fred', 'Suzy', 'Suzy', 'Bob'],
                     'pet': ['Dog', 'Dog', 'Cat', 'Fish']})

df_2 = pd.DataFrame({'Name': ['Suzy', 'Suzy', 'Suzy', 'Fred', 'Joe', 'Joe'],
                     'Colour': ['Black', 'Blue', 'Red', 'Green', 'Yellow', 'Blue']})

display(df_1)
display(df_2)

# %%

# default 'how' is inner
j_data_3 = df_1.merge(df_2.assign(name=df_2.Name))

# %%

# df_1 columns that overlap with df_2, obtain cross products for like data
j_data_4 = df_1.merge(df_2.assign(name=df_2.Name), how='left')

# %%

# df_2 columns that overlap with df_1
j_data_5 = df_1.merge(df_2.assign(name=df_2.Name), how='right')

# %%

j_data_6 = df_1.merge(df_2.assign(name=df_2.Name), how='outer')
# can add a validate='1:1' to check whether the data sets have unique keys
# or 1:many or many:1 validations

# %%

# can drop duplicates to make data 1:1
j_data_7 = (df_1
            .drop_duplicates(subset='name')
            .merge(df_2
                   .drop_duplicates(subset='Name')
                   .assign(name=df_2.Name), how='left', validate='1:1'))
