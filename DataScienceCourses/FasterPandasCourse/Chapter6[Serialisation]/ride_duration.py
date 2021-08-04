"""Using "bikes.db", find the 5 bikes (using "bike_id") that has the biggest
90% quantile of ride duration in the first quarter of 2017.
"""
import sqlite3
import pandas as pd

# connect to database
conn = sqlite3.connect('bikes.db')

# use sql to select on relevent columns, in specified time frame
query = """
        SELECT bike_id, duration
        FROM bike_rides
        WHERE year == 2017 AND month < 4
        """

# load dataframe
df = pd.read_sql(query, conn)

# aggregate the 90% quartile of ride duration
result = df.groupby('bike_id')['duration'].quantile(0.9)

# select top five
print(result.sort_values(ascending=False)[:5])
