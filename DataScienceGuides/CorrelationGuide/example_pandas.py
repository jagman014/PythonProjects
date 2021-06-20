# %%
import pandas as pd

x =pd.Series(range(10, 20))

y = pd.Series([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])

# %%
# pandas Series contain a .corr method

# Pearson's r
print(x.corr(y))

# Spearman's rho
print(x.corr(y, method='spearman'))

# Kendall's tau
print(x.corr(y, method='kendall'))
