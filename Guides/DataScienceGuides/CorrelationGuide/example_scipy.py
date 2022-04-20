# %%
import numpy as np
import scipy.stats

x = np.arange(10, 20)

y = np.array([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])

# %%
# scipy contains all methods in the stats module
# all methods also return the corresponding p-value

# Pearson's r
print(scipy.stats.pearsonr(x, y))

# Spearman's rho
print(scipy.stats.spearmanr(x, y))

# Kendall's tau
print(scipy.stats.kendalltau(x, y))

# %%
# can use three methods to extract from the tuples

# use of [], 0 <- correlation, 1 <- p-value
# can use .correlation on all methods
# can also just use muliple value assignment unpacking
