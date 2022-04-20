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

# zero point of .iloc depends where the index is set
f_data = (alta_2
          .set_index('date')
          .iloc[:, 2])

# %%

# .iloc follows half-open interval, start inclusive -> end exclusive
# whereas .loc uses closed interval, start -> end both inclusive
f_data_2 = (alta_2
            .set_index('date')
            .iloc[12_500:13_500:, 2])

# %%

# useful for getting first / last
f_data_3 = (alta_2
            .set_index('date')
            .iloc[-200:])

# %%

f_data_4 = (alta_2
            .iloc[10:20, 2:6])

# %%

# doesn't work with boolean arrays, but does with numpy array conversion
gt_10 = alta_2.snow > 10
f_data_5 = (alta_2
            .loc[gt_10.to_numpy()])
