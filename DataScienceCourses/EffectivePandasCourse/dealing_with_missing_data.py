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

missing_data = alta_2.isna()

# %%

# columns with missing data (apply any to axis 0)
missing_data_1 = alta_2.isna().any()

# %%

# columns with missing data
missing_data_2 = alta_2.isna().sum()

# %%

# .mul -> multiply, mean of this gives percent missing
missing_data_3 = alta_2.isna().mul(100).mean()

# %%

# where any part of the row is missing
missing_data_4 = alta_2.isna().any(axis=1)

# %%

missing_data_5 = alta_2[alta_2.isna().any(axis=1)]

# %%

# see where snow depth is missing
missing_data_6 = alta_2.query('snwd.isna()')

# %%

(alta_2
 .set_index('date')
 .loc['1980-04':'1980-05']
 .snwd
 .plot())

plt.show()

# %%

# dealing with missing data
# talk to subject matter expert, or:
# - drop data <--
# - impute data
# - (add indicator column)

(alta_2
 .set_index('date')
 .loc['1980-04':'1980-05']
 .snwd
 .dropna()
 .plot())

plt.show()

# %%

# impute
(alta_2
 .set_index('date')
 .loc['1980-04':'1980-05']
 .snwd
 .fillna(alta_2.snwd.mean())
 .plot())

plt.show()

# %%

# interpolate good for continuous data
(alta_2
 .set_index('date')
 .loc['1980-04':'1980-05']
 .snwd
 .interpolate()
 .plot())

plt.show()

# %%

# forward fill
(alta_2
 .set_index('date')
 .loc['1980-04':'1980-05']
 .snwd
 .ffill()
 .plot())

plt.show()

# %%

# backward fill
(alta_2
 .set_index('date')
 .loc['1980-04':'1980-05']
 .snwd
 .bfill()
 .plot())

plt.show()

# %%

# indicator column
missing_data_7 = (alta_2
                  .assign(snwd_missing=alta_2.snwd.isna(),
                          smwd=lambda df_: df_.snwd.interpolate()))

# %%

(alta_2
 .set_index('date')
 .loc[:'1984-08']
 .snwd
 .interpolate()
 .plot(figsize=(10, 4)))

plt.show()

# %%

# interpolate not to good for large amounts of missing data
# e.g. 1985 for this data
(alta_2
 .set_index('date')
 .loc['1984-08':'1990-08']
 .snwd
 .interpolate()
 .plot(figsize=(10, 4)))

plt.show()
