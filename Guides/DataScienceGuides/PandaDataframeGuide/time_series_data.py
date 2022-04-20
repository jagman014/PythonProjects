import pandas as pd
import os

# %%
# .date_range method will produce a range of datetimes within a given range

temp_c = [8.0, 7.1, 6.8, 6.4, 6.0, 5.4, 4.8, 5.0,
          9.1, 12.8, 15.3, 19.1, 21.2, 22.1, 22.4, 23.1,
          21.0, 17.9, 15.5, 14.4, 11.9, 11.0, 10.2, 9.1]

dt = pd.date_range(start='2019-10-27 00:00:00.0', periods=24, freq='H')

temp = pd.DataFrame(data={'temp_c': temp_c}, index=dt)

# %%
# indexing and slicing work in the same manor with datetimes

print(temp['2019-10-27 05':'2019-10-27 14'])

# %%
# can use the .resample method to obtain different frequencies

print(temp.resample(rule='6h').mean())

# %%
# can use .rolling to do rolling-window analysis

print(temp.rolling(window=3).mean())

# %%

temp.to_csv(os.path.join(os.getcwd(), 'temp.csv'))
