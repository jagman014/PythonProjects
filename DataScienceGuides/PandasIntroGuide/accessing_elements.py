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
# can use [] with implicit or explicit indicies

print(city_revenues['Toronto'])
print(city_revenues[1])

# %%
# can use list slicing methods as well

print(city_revenues[-1])
print(city_revenues[1:])
print(city_revenues['Toronto':])

# %%
# two extra methods of loc and iloc

colors = pd.Series(
    ["red", "purple", "blue", "green", "yellow"],
    index=[1, 2, 3, 5, 8]
)

# %%
# loc refers to the label index
# iloc refers to the positional index

print(colors.loc[1])
print(colors.iloc[1])

# %%
# these methods also support slicing
# however iloc is the standard half-open interval, and loc is a closed interval

print(colors.iloc[1:3])
print(colors.loc[3:8])

# %%
# can also pass negative indicies to iloc
# loc -> dict[], iloc -> list[]

print(colors.iloc[-2])

# %%
# can also use [] on dataframe objects
# can use use dot notation if the columns are python viable

print(city_data['revenue'])
print(city_data.revenue)

# %%
# dot notation won't work if it coincides with a method / attribute name

toys = pd.DataFrame([
    {"name": "ball", "shape": "sphere"},
    {"name": "Rubik's cube", "shape": "cube"}
])

print(toys['shape'])
print(toys.shape)

# %%
# can also use loc and iloc methods

print(city_data.loc['Amsterdam'])
print(city_data.loc['Tokyo':'Toronto'])
print(city_data.iloc[1])

# %%
# for tdataframes they can take a second parameter for the columns

print(city_data.loc['Amsterdam':'Tokyo', 'revenue'])
