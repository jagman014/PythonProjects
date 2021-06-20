# %%
# Series objects
import pandas as pd

revenues = pd.Series([5555, 7000, 1980])

print(revenues)

# %%
# series wraps the components and their indicies
# stored as a numpy array

print(revenues.values)
print(revenues.index)

# %%
# can define an explicit index for the series values
# acts more like a dicitionary than a list like above

city_revenues = pd.Series(
    [4200, 8000, 6500],
    index=['Amsterdam', 'Toronto', 'Tokyo']
)

print(city_revenues)

# %%
# can also be constructed via a ditionary to give explicit indicies

city_employee_count = pd.Series({"Amsterdam": 5, "Tokyo": 8})

print(city_employee_count)

# %%
# can use these indicies like dictionary keys

print(city_employee_count.keys)

print('Tokyo' in city_employee_count)
print('New York' in city_employee_count)

# %%
# Dataframe objects
# can be created from a set of Series objects
# any missing values are replaced with NaN

city_data = pd.DataFrame({
    'revenue': city_revenues,
    'employee_count': city_employee_count
})

print(city_data)

# %%
# just like Series you can call for the indicies and the values

print(city_data.index)
print(city_data.values)

# %%
# can also call the axes data
# 0 -> rows, 1 -> columns

print(city_data.axes)
print(city_data.axes[0])
print(city_data.axes[1])

# %%
# keys for a dataframe only refer to the columns

print(city_data.keys)

print('Amsterdam' in city_data)
print('revenues' in city_data)
