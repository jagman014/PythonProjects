# %%
# concatinating frames based on axis
import pandas as pd

climate_temp = pd.read_csv('climate_temp.csv')
climate_precip = pd.read_csv('climate_precip.csv')

precip_one_station = climate_precip[climate_precip['STATION']
                                    == "GHCND:USC00045721"]

# %%
# can use append as a shortcut to concat
# defaults to full-outer join, on the index (axis=0)

double_precip = pd.concat([precip_one_station,
                           precip_one_station])

# %%

reindexed = pd.concat([precip_one_station,
                       precip_one_station],
                      ignore_index=True)

# %%
# outer join on indicies

outer_joined = pd.concat([climate_precip, climate_temp])

# %%
# inner join on indicies

inner_joined = pd.concat([climate_temp, climate_precip],
                          join='inner')

# %%
# inner join on columns

inner_joined_cols = pd.concat([climate_temp, climate_precip],
                              axis=1,
                              join='inner')

# %%
# use key to create heirachical axis labels

heirachical_keys = pd.concat([climate_temp, climate_precip],
                             keys=['temp', 'precip'])

# %%
# append is used in a similar method

appended = precip_one_station.append(precip_one_station)
