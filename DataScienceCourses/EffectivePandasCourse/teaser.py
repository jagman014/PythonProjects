# Example

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = ('https://github.com/mattharrison/datasets/raw/master/' +
       'data/Presidents.xls')
pres = pd.read_excel(url)


# to view type variable name in sciview -> data

# can use .columns to view columns,
# and .sample(x) to view x random entries
# .dtypes shows data types


# %%
# tweak data:
def clean_cols(value):
    return value.replace(' ', '_').replace('#', 'Num').replace('%', 'Per')


def clean_pop(df):
    col = (df
           ['Per_popular']
           .replace('NA()', np.nan)
           .astype(float))
    return col.fillna(col.mean())


pres_2 = (pres
          .rename(columns=clean_cols)
          .assign(date=lambda df_: pd.to_datetime(df_.Year_first_inaugurated,
                                                  format='%Y'),
                  Per_popular=clean_pop)
          )
# .describe() to get data stats
# .corr() give correlation

# %%
(pres_2
 .Age_at_inauguration
 .plot.bar())
plt.show()

# %%
(pres_2
 .set_index('President')
 .Age_at_inauguration
 .plot.barh(figsize=(6, 6))
 )
plt.show()

# %%
(pres_2
 .Political_Party
 .value_counts()
 .plot.pie(figsize=(6, 4)))
plt.show()

# %%
(pres_2
 .Political_Party
 .value_counts()
 .plot.barh(figsize=(6, 4)))
plt.show()

# %%
(pres_2
 .Occupation
 .value_counts()
 .plot.barh(figsize=(6, 4)))
plt.show()

# %%
(pres_2
 .College
 .value_counts()
 .plot.barh(figsize=(6, 4)))
plt.show()

# %%
filtered_pres = pres_2[pres_2.Years_in_office < 4]

# %%
pres_2.Years_in_office.value_counts(dropna=False)

# %%
nan_pres = pres_2[pres_2.Years_in_office.isna()]

# %%
party_sort = (pres_2
              .groupby('Political_Party')
              .mean())
