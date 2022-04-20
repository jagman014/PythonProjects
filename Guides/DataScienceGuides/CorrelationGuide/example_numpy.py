# %%
import numpy as np

x = np.arange(10, 20)

y = np.array([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])

# %%
# can use corrcoef to return a matrix of Pearson correlation coefficents
# [x|x correlation, x|y correlation,
#  y|x correlation, y|y correlation]

r = np.corrcoef(x, y)

print(r)
