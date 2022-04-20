# %%
# merging based on one or more keys
import pandas as pd

climate_temp = pd.read_csv("climate_temp.csv")
climate_precip = pd.read_csv("climate_precip.csv")

# %%

print(climate_temp.head())
print(climate_precip.head())

# %%

print(climate_temp.shape)
print(climate_precip.shape)

# %%
# merge defaults to inner join, removes non-shared rows

precip_one_station = climate_precip[climate_precip["STATION"] 
                                    == "GHCND:USC00045721"]

inner_merged = pd.merge(precip_one_station, climate_temp)

# %%

print(inner_merged.head())
print(inner_merged.shape)

# %%
# can specifiy the columns to join frames on

inner_merged_total = pd.merge(climate_temp,
                              climate_precip, 
                              on=['STATION', 'DATE'])

print(inner_merged_total.head())
print(inner_merged_total.shape)

# %%
# outer join, keep all rows

outer_merged = pd.merge(precip_one_station, 
                        climate_temp, 
                        how="outer", 
                        on=["STATION", "DATE"])

print(outer_merged.head())
print(outer_merged.shape)

# %%
# left-outer join, keep all left dataframe rows

left_merged = pd.merge(climate_temp,
                       precip_one_station,
                       how='left',
                       on=['STATION', 'DATE'])

print(left_merged.head())
print(left_merged.shape)

# %%

left_merged_reversed = pd.merge(precip_one_station,
                                climate_temp,
                                how='left',
                                on=['STATION', 'DATE'])

print(left_merged_reversed.head())
print(left_merged_reversed.shape)

# %%
# right-outer join, keep all right dataframe rows

right_merged = pd.merge(precip_one_station,
                        climate_temp,
                        how='right',
                        on=['STATION', 'DATE'])

print(right_merged.head())
print(right_merged.shape)
