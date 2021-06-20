# %%
# Spearman's rho only cares about the ranks of the numbers in the data
# it is similar to Pearson's r but only conserns the order of the values
# i.e. whether larger x corresponds to larger y
# -1 <= rho <= 1, |rho| = 1 monotonically increasing / decreasing function

# %% 
# Kendell's tau compares the concordance of pairs of coordinates
# concordant if (xi > xj & yi > yj) | (xi < xj & yi < yj)
# discordant if (xi < xj & yi > yj) | (xi > xj & yi < yj)
# neither if (xi == xj) | (yi == yj)
# calculated as tau = (n+ - n-) / sqrt[(n+ + n- + nx)(n+ + n- + ny)]
# where n+ -> # of concordant, n- -> # of discordant, nx and ny are # of ties
# (ties that occur in both x and y aren't counted)
# -1 <= tau <= 1, tau = 1 -> all concordant, tau = -1 -> all discordant

# %%
# scipy implementation
import pandas as pd
import numpy as np
import scipy.stats

x = np.arange(10, 20)
y = np.array([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])
z = np.array([5, 3, 2, 1, 0, -2, -8, -11, -15, -16])

# %%
# can obtain the ranking with rankdata
# will rank tied values as their average rank by default
# nan values are treated as large

print(scipy.stats.rankdata(x))
print(scipy.stats.rankdata(y))
print(scipy.stats.rankdata(z))

# %%
# can also obtain ranks by adding 1 to argsort
# argsort returns indicies if values where sorted

print(np.argsort(y) + 1)

# %%
# can use spearmanr to get rho
# for larger arrays, need to specify the axis (0 -> columns, 1 -> rows)

results = scipy.stats.spearmanr(x, y)

print(results)
print(results.correlation)
print(results.pvalue)

rho, p = scipy.stats.spearmanr(x, y)

print(rho)
print(p)

# %%
# providing >2D arrays returns correlation and p-value matricies

xyz = np.array([x, y, z])

corr_matrix, p_matrix = scipy.stats.spearmanr(xyz, axis=1)

print(corr_matrix)
print(p_matrix)

# %%
# can use kendalltau to get tau
# works in a similar way to spearmanr, 
# except cannot take a single 2D array

result = scipy.stats.kendalltau(x, y)

print(result)
print(result.correlation)
print(result.pvalue)

tau, p = scipy.stats.kendalltau(x, y)

print(tau)
print(p)

# %%
# pandas implementation

x, y, z = pd.Series(x), pd.Series(y), pd.Series(z)
xy = pd.DataFrame({'x-values': x, 'y-values': y})
xyz = pd.DataFrame({'x-values': x, 'y-values': y, 'z-values': z})

# %%
# can use corr and corrwith as before with Pearson's r

print(x.corr(y, method='spearman'))
print(xy.corr(method='spearman'))
print(xyz.corr(method='spearman'))
print(xy.corrwith(z, method='spearman'))

# %%
# similar method for Kendall's tau

print(x.corr(y, method='kendall'))
print(xy.corr(method='kendall'))
print(xyz.corr(method='kendall'))
print(xy.corrwith(z, method='kendall'))
