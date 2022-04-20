# %%
import pandas as pd

city_revenues = pd.Series(
    [4200, 8000, 6500],
    index=['Amsterdam', 'Toronto', 'Tokyo']
)

city_employee_count = pd.Series({"Amsterdam": 5, "Tokyo": 8})

city_data = pd.DataFrame({
    'revenue': city_revenues,
    'employee_count': city_employee_count
})

# %%
# can combine dataframes using concat 
# which combines on axis=0 by default

further_city_data = pd.DataFrame(
    {'revenue': [7000, 3400], 'employee_count': [2, 2]},
    index=['New York', 'Barcelona']
)

all_city_data = pd.concat([city_data, further_city_data], sort=False)
print(all_city_data)

# %%
# can also concat on axis=1 for the columns

city_countries = pd.DataFrame({
    'country': ['Netherlands', 'Japan', 'Netherlands', 'Canada', 'Spain'],
    'capital': [1, 1, 0, 0, 0]},
    index=['Amsterdam', 'Tokyo', 'Rotterdam', 'Toronto', 'Barcelona']
)

cities = pd.concat([all_city_data, city_countries], axis=1, sort=False)
print(cities)

# %%
# concat defaults to full-outer join
# can be changed with the 'join' keyword

print(pd.concat([all_city_data, city_countries], axis=1, join='inner'))

# %%
# can also use merge in a similar method to SQL joins

countries = pd.DataFrame({
    'population_millions': [17, 127, 37],
    'continent': ['Europe', 'Asia', 'North America']
},
index=['Netherlands', 'Japan', 'Canada']
)

print(pd.merge(cities, countries, left_on='country', right_index=True))

# %%
# merge performs an inner join by default
# changed with the 'how' keyword

print(
    pd.merge(
        cities,
        countries,
        left_on='country',
        right_index=True,
        how='left'
    )
)
