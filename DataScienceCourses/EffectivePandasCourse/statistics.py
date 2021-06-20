# Examples
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

# returns summary statistics
summary = alta_2.describe()
# count = number of non-missing values
# mean, standard deviation, min, max and quartiles

# %%

# many aggregate functions / methods (min, max, mean, median, kurt, skew)
skew = alta_2.skew()  # skew gives relative positions of mean, median, mode

# %%

# default 50th percentile
quant_50 = alta_2.quantile()

# %%

quants_10_90 = alta_2.quantile([.1, .9])

# %%

# can collect multiple aggregate functions
stats = alta_2.agg(['kurt', 'skew', 'mean', 'median'])

# %%

# Pierson correlation coefficient
corr = alta_2.corr()

# %%

# returns individual correlations
prcp_snow_corr = alta_2.prcp.corr(alta_2.snow)
