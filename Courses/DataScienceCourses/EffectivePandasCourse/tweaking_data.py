# Examples
import pandas as pd

# %%

alta = pd.read_excel('alta.xlsx')

# %%

cols = alta.columns


# %%

# generally rename columns to be valid python attributes
# can use dictionary or function
def clean_col(name):
    return name.lower()


# returns a new dataframe
(alta
 .rename(columns=clean_col))

# %%

pd.to_datetime(alta.DATE)

# %%

alta.NAME.value_counts()

# %%

# many string utilities using .str attributes
alta.DATE.str.slice(0, 4).astype(int)

# %%

# can convert to date and pull off year attribute
years = pd.to_datetime(alta.DATE).dt.year


# %%

def to_celsius(val):
    return (val - 32) * (5 / 9)


alta.TOBS.apply(to_celsius)

# %%

# sometimes faster to not use .apply, but use vectorised operations
(alta.TOBS - 32) * (5 / 9)


# %%

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
