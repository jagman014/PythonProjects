# %%

import math
import timeit

# %%

print(math.pow(2, 5))  # 32.0
print(math.pow(5, 2.4))  # 47.5913...
print(math.pow(1.0, 3))  # 1.0

# %%

print(math.pow(4, 0))  # 1.0
print(math.pow(math.nan, 0))  # 1.0

print(math.pow(0, 2))  # 0.0
print(math.pow(0, 2.3))  # 0.0
print(math.pow(0, -2))  # ValueError

# %%

# python has 2 alternative, "**", and pow()
print(3 ** 2)  # 9
print(2 ** 3.3)  # 9.849155...

print(pow(3, 2))
print(pow(2, 3.3))

# %%

# pow can take a third param, modulus
print(pow(32, 6, 5))  # 4
print((32 ** 6) % 5 == pow(32, 6, 5))  # True

# %%

print(timeit.timeit("10 ** 308"))  # 4.0511627
print(timeit.timeit("pow(10, 308)"))  # 4.1732381
print(timeit.timeit("math.pow(10, 308)", setup="import math"))  # 0.4116116

# %%

# base e exponetials

print(math.exp(21))  # 1318815734.48...
print(math.exp(-1.2))  # 0.301194...

# %%

print(timeit.timeit("math.e ** 308", setup="import math"))  # 0.3831018
print(timeit.timeit("pow(math.e, 308)", setup="import math"))  # 0.5151934
print(timeit.timeit("math.exp(308)", setup="import math"))  # 0.3013019

# %%

# radioactive decay
half_life = 38.1
initial = 100
time = 100
remaining = initial * math.exp(-math.log(2) * time / half_life)

print(f"Remaining quantity of Sr-90: {remaining}")
# 16.2141813
