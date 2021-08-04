"""Calculate the minimal and maximal distance driven from the data at
    taxi.csv.xz
Consume as little memory as possible and don't load more than 50,000 rows at a
time.
"""

import pandas as pd

# set initial values
min_dist, max_dist = float('inf'), float('-inf')

# load csv, only relevant col and 50,000 rows at a time
dfs = pd.read_csv('taxi.csv.xz', usecols=['trip_distance'], chunksize=50_000)

# iterate over chuncks to get min and max
for df in dfs:
    # obtain min and max of chunk
    desc = df['trip_distance'].describe()

    # compare with previous min and max
    min_dist = min(min_dist, desc['min'])
    max_dist = max(max_dist, desc['max'])

print('min', min_dist, 'max', max_dist)
