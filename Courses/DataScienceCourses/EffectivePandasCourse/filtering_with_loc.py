# Example

import pandas as pd
import datetime

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

# .loc can filter with column or row labels
# dates support partial string indexing
f_data = (alta_2
          .set_index('date')
          .loc['2015':'2016', 'snow'])

# %%

# : operator selects all between given values, include both ends of interval
f_data_1 = (alta_2
            .set_index('date')
            .loc['2015':'2016', 'snow':'snwd'])

# %%

# with lists, only returns the first values with partial index
f_data_2 = (alta_2
            .set_index('date')
            .loc[['2015', '2016'], ['snow', 'snwd']])

# %%

f_data_3 = (alta_2
            .set_index('date')
            .loc[['2015-11-01', '2016-07-04'], ['snow', 'snwd']])

# %%

# may sometimes need to be more specific with partial date slicing
f_data_4 = (alta_2
            .set_index('date')
            .loc[[datetime.datetime(2015, 11, 1), datetime.datetime(2016, 7, 4)],
                 ['snow', 'snwd']])

# %%

# select all rows
f_data_5 = (alta_2
            .set_index('date')
            .loc[:, ['snow', 'snwd']])

# %%

# can take a boolean array, requires the same index
gt_10 = (alta_2
         .set_index('date')
         .snow > 10)

f_data_6 = (alta_2
            .set_index('date')
            .loc[gt_10, ['snow', 'snwd']])


# %%

# by function
f_data_7 = (alta_2
            .set_index('date')
            .loc[lambda df_: df_.snow > 10, ['snow', 'snwd']])

# %%

# boolean arrays and functions useful when intermediate dataframe has changed
f_data_8 = (alta_2
            .set_index('date')
            .rename(columns=str.upper)
            .loc[lambda df_: df_.SNOW > 10])
