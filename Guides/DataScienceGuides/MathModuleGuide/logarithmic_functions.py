# %%

import math

# %%

# natural log

print(math.log(4))  # 1.3862944
print(math.log(3.4))  # 1.2237754

print(math.log(-3))  # ValueError

# %%

# log(x, n) -> log_n(x)

print(math.log(math.pi, 2))  # 1.6514961
print(math.log(math.pi, 5))  # 0.7112607

# %%

# explicit base 2 and base 10

print(math.log2(math.pi))  # 1.6514961
print(math.log10(math.pi))  # 0.4971499

# %%

# half-time

initial = 100
remaining = 16.21418
time = 100
half_life = (-math.log(2) * time) / math.log(remaining / initial)
print(f"Half-life of the unknown element: {half_life}")
# 38.099998
