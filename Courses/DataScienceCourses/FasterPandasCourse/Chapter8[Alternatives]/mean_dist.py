"""Using vaex, calculate the mean taxi ride distance in "taxi.csv.xz" per
VendorID.
"""
import vaex

# load data into dataframe
df = vaex.read_csv('taxi.csv.xz', compression='xz')

# using vaex groupby -> cols, aggreagation
result = df.groupby('VendorID', vaex.agg.mean(df['trip_distance']))

print(result)
