import pandas as pd
import os

# %%

filename = os.path.join(os.getcwd(), 'data_1.csv')
df = pd.read_csv(filename, index_col=0)

# %%
# can filter data via boolean arrays from numpy
# NOT -> ~, AND -> &, OR -> |, XOR -> ^

print(df[df['django-score'] >= 80])

print(df[(df['py-score'] >= 80) & (df['js-score'] >= 80)])

# %%
# can also use the .where method
# but will return the column and index where the condition is satisfied

print(df['django-score'].where(cond=df['django-score'] >= 80, other=0.0))
