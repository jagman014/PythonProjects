import pandas as pd

data = {
    'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
    'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai',
             'Manchester', 'Cairo', 'Osaka'],
    'age': [41, 28, 33, 34, 38, 31, 37],
    'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
}

row_labels = [101, 102, 103, 104, 105, 106, 107]

# %%

df = pd.DataFrame(data=data, index=row_labels)

# %%

df.head(n=2)

# %%

df.tail(n=2)

# %%
# dataframe access similar to that of dictionaries
# can also use dot notation if column name is a valid python name

cities = df['city']

# %%
# dataframe columns correspond to pd.Series
# access series data same as with dictionary labels

print(cities[102])

# %%
# access rows via .loc[index]
# also an instance of a series

print(df.loc[103])
