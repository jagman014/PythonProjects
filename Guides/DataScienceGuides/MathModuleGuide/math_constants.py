# %%
import math

# %%
# Pi, ratio of diameter to circumference of a circle
# given to 15 d.p.

print(math.pi)

# %%
# calculate circumference

r = 3
circumference = 2 * math.pi * r

print(
    f"Circumference of a Circle = 2 * {math.pi:.4} * {r} = {circumference:.4}"
)

# %%
# area of a circle

r = 5
area = math.pi * (r ** 2)

print(
    f"Area of a Circle = {math.pi:.4} * {r} ^ 2 = {area:.4}"
)

# %%
# Tau, ratio of radius to circumference (2 * Pi)

print(math.tau)

# %%

r = 3
circumference = math.tau * r

print(
    f"Circumference of a Circle = {math.tau:.4} * {r} = {circumference:.4}"
)

# %%
# Euler's number, e

print(math.e)

# %%
# Infinity, inf

print(f"Positive Infinity = {math.inf}")
print(f"Negative Infinity = {-math.inf}")

# %%
# equivilent to float('inf')

print(float('inf') == math.inf)

# %%
# relates to the concept of infinity, therefore larger than any number
# 1 x 10 ^ 308 is the largest floating point number with double precision
# the same can be said for -inf being the smallest

print(math.inf > 1e308)

# %%
# any operations with inf return inf (or NaN in special cases)

print(math.inf + 1e308)
print(math.inf / 1e308)

# %%
# Not a number (NaN), non-numerical value
# same as float('nan')

print(math.nan)
