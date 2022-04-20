# Example

import pandas as pd

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

alta_gt_100 = alta_2[alta_2.tobs > 100]

# %%

# query method accepts a sting, and evaluates it
alta_gt_100_query = alta_2.query('tobs > 100')

# %%

months = ['December', 'January']
# use @ to reference variables
alta_dec_jan = alta_2.query('date.dt.month_name().isin(@months)')

# %%

alta_d_j_gt_10 = alta_2.query('date.dt.month_name().isin(@months) and snow > 10')

# %%

# boolean array method
# need to use '&' instead of 'and'
# need to use '|' instead of 'or'
# need to use '~' instead of 'not'
jan_dec = alta_2.date.dt.month_name().isin(months)
gt_10 = alta_2.snow > 10
alta_d_j_gt_10_2 = alta_2[jan_dec & gt_10]

# %%

# can in-line operations, but need to be careful and separate by ()

# %%

# returns a series
date_snow = (alta_2
             .set_index('date')
             ['snow'])

# %%

# returns a dataframe
date_snow_2 = (alta_2
               .set_index('date')
               [['snow']])

# %%

# .loc returns [row, column name]
date_snow_3 = (alta_2
               .set_index('date')
               .loc[:, 'snow'])

# %%

# .iloc => index version of .loc
date_snow_4 = (alta_2
               .set_index('date')
               .iloc[:, 2])
