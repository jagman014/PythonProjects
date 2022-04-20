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

# can't plot much with datetime columns
(alta_2
 .drop(columns='date')
 .plot())

plt.show()

# %%

# can set the index to the date
(alta_2
 .set_index('date')
 .plot())

plt.show()

# %%

# filter columns containing 't'
(alta_2
 .set_index('date')
 .filter(regex=r'^t.*', axis='columns')
 .plot())

plt.show()

# %%

# can change figure dimensions
(alta_2
 .set_index('date')
 .filter(regex=r'^t.*', axis='columns')
 .plot(figsize=(10, 4)))

plt.show()

# %%

# resample dates by month ('M') mean aggregation
# check .resample documentation
(alta_2
 .set_index('date')
 .filter(regex=r'^t.*', axis='columns')
 .resample('M')
 .mean()
 .plot(figsize=(10, 4)))

plt.show()

# %%

# .iloc pull off certain rows
(alta_2
 .set_index('date')
 .filter(regex=r'^t.*', axis='columns')
 .resample('M')
 .mean()
 .iloc[-100:]
 .plot(figsize=(10, 4)))

plt.show()

# %%

font = 'Arial'

with plt.style.context('fivethirtyeight'):
    with plt.style.context({'font.family': font}):
        (alta_2
         .set_index('date')
         .filter(regex=r'^t.*', axis='columns')
         .resample('M')
         .mean()
         .iloc[-100:]
         .plot(figsize=(10, 4), title='Temperatures at Alta')
         .legend(bbox_to_anchor=(1, 1)))

        plt.show()

# %%

# bar plot - average per month
(alta_2
 .groupby(alta_2.date.dt.month_name())
 .snow
 .mean()
 .plot.barh())

plt.show()

# %%

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

MonthType = pd.CategoricalDtype(categories=months, ordered=True)

(alta_2
 .assign(month=alta_2.date.dt.month_name().astype(MonthType))
 .groupby('month')
 .snow
 .mean()
 .plot.barh())

plt.show()

# %%

with plt.style.context('fivethirtyeight'):
    with plt.style.context({'font.family': font}):
        ax = (alta_2
              .assign(month=alta_2.date.dt.month_name().astype(MonthType))
              .groupby('month')
              .snow
              .mean()
              .plot.barh(title='Average Daily Snowfall / in, at Alta'))
        ax.set_ylabel('')

        plt.show()

# %%

# pie chart
(alta_2
 .assign(month=alta_2.date.dt.month_name().astype(MonthType))
 .groupby('month')
 .snow
 .mean()
 .plot.pie())

plt.show()

# %%

# scatter plot
(alta_2
 .plot.scatter(x='tobs_c', y='snwd'))

plt.show()

# %%

# alpha is the transparency
(alta_2
 .sample(2_000)
 .plot.scatter(x='tobs_c', y='snwd', alpha=.2))

plt.show()

# %%

(alta_2
 .sample(2_000)
 .plot.scatter(x='tobs_c', y='snow', alpha=.2))

plt.show()

# %%

temp_for_snow = alta_2.query('snow > 0').tobs_c.max()

# %%

with plt.style.context('fivethirtyeight'):
    (alta_2
     .sample(2_000)
     .plot.scatter(x='tobs_c', y='snow', alpha=.2,
                   title='Snowfall vs Temp (C)'))

    plt.show()

# %%

# histogram
(alta_2
 .query('snow > 0')
 .tobs_c
 .plot.hist())

plt.show()

# %%

with plt.style.context('fivethirtyeight'):
    with plt.style.context({'font.family': font}):
        (alta_2
         .query('snow > 0')
         .tobs_c
         .plot.hist(title='Temp (C) during snowfall'))

        plt.show()
