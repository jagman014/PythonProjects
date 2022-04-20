"""What is the median trip duration in 2017, only in active kiosks?
- Trip data in austin-bikes-1.csv.xz
- Kiosk status data in austin-kiosk.csv
"""
import pandas as pd

bike_df = pd.read_csv('austin-bikes-1.csv.xz', low_memory=False)

# set kiosk id as index
kiosk_df = pd.read_csv('austin-kiosk.csv', index_col='Kiosk ID')

df = pd.merge(bike_df, kiosk_df, left_on='Checkout Kiosk ID', right_index=True)

# query dataframe
active_2017 = df.query(
    '`Kiosk Status` == "active" & Year == 2017 & `Trip Duration Minutes` > 0'
    )

# calculate median
print(active_2017['Trip Duration Minutes'].median())
