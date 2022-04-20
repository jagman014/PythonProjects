# %%
# Pearson (product-moment) correlation coefficient: r
# ratio of covarience to the product of standard deviations
# r = sum[(xi - xbar)(yi - ybar)] / 
#       {sqrt[sum[(xi - xbar) ^ 2]] * sqrt[sum[(yi - ybar) ^ 2]]}
# r bound to -1 <= r <= 1, |r| -> perfect linear correlation
# r close to zero, indicates that the inputs are independent

# %%
import numpy as np
import scipy.stats

x = np.arange(10, 20)

y = np.array([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])

# %%
# can use scipy.stats.linregress to obtain the relevant results
# then using the dot notation for clear numeric access
# will return nan if any data points are missing

results = scipy.stats.linregress(x, y)

print(results.slope)
print(results.intercept)
print(results.rvalue)
print(results.pvalue)
print(results.stderr)  # standard error in gradient

# %%
# this can also be done with a 2D array

xy = np.array([[10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
               [2, 1, 4, 5, 8, 12, 18, 25, 96, 48]])

print(scipy.stats.linregress(xy))

# %%
# will return the same result with the transpose

print(scipy.stats.linregress(xy.T))

# %%
# the pearson corrilations in scipy and numpy both return nan
# if nan is provided, whereas pandas corr ignores nan values
# both pandas corr and np.corrcoef can deal with >2D arrays
# can also use .corrwith DF method in pandas for >2D correlation
