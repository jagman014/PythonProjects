# %%
# joining frames based on columns or indicies
import pandas as pd

climate_temp = pd.read_csv('climate_temp.csv')
climate_precip = pd.read_csv('climate_precip.csv')

precip_one_station = climate_precip[climate_precip['STATION']
                                    == "GHCND:USC00045721"]

# %%
# join is an object function, whereas merge is a module function
# enables the specification of only one dataframe
# defaults to left-outer join on indicies

precip_one_station.join(climate_temp, 
                        lsuffix='_left', 
                        rsuffix='_right')

# %%
# flipping for the larger dataframe will produce NaN values

climate_temp.join(precip_one_station,
                  lsuffix='_left',
                  rsuffix='_right')

# %%
# inner join akin to inner merge from 'merge_combine.py'
# need to set the indicies to be columns to join on columns

inner_joined_total = climate_temp.join(
    climate_precip.set_index(['STATION', 'DATE']),
    lsuffix='_x',
    rsuffix='_y',
    on=['STATION', 'DATE']
)

print(inner_joined_total.head())

# %%
# bare join call

climate_temp.join(climate_precip, lsuffix='_left')
