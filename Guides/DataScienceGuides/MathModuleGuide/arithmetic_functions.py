# %%
import math
import timeit

# %%
# factorials, simple for loop

def fact_loop(num):
    if num < 0:
        return 0
    if num == 0:
        return 1

    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial

print(fact_loop(4))

# %%
# simple recursive loop

def fact_recursion(num):
    if num < 0:
        return 0
    if num == 0:
        return 1

    return num * fact_recursion(num - 1)

print(fact_recursion(4))

# %%
# using math.factorial()
# only accepts positive ints

print(math.factorial(4))

# %%
# can compare with timeit module, executes 1M loops for each call
# math module much faster due to undelying c bindings

print(f'for loop: {timeit.timeit("fact_loop(10)", globals=globals())}')

print(f'recursion: {timeit.timeit("fact_recursion(10)", globals=globals())}')

print(f'math module: {timeit.timeit("math.factorial(10)", setup="import math")}')

# %%
# ceiling function, .ceil()
# ints don't change

print(math.ceil(6))

print(math.ceil(-11))

# %%
# for floats ceil rounds up

print(math.ceil(4.23))

print(math.ceil(-11.453))

# %%
# floor function acts similarly but rounds down

print(math.floor(5.536))

print(math.floor(-6.423))

# %%
# number truncation with trunc()
# removes decimal places
# equivalent to floor for positive, and ceil for negative

print(math.trunc(12.352))

print(math.trunc(-14.52))

print(math.trunc(12.352) == math.floor(12.352))

print(math.trunc(-14.52) == math.ceil(-14.52))

# %%
# closeness to numbers with isclose()
# allows setting of tolerences
# relative defaults to 1e-9
# absolute defaults to 0.0
# will return true if
#       |a - b| <= max(rel_tol * max(|a|, |b|), abs_tol)

print(math.isclose(6, 7))

print(math.isclose(6.999999999, 7))

# %%
# can adjust both tolerences as need be

print(math.isclose(6, 7, rel_tol=0.2))

print(math.isclose(6, 7, abs_tol=1))

print(math.isclose(6, 7, abs_tol=0.2))

# %%
# abs_tol can also be used for small values

print(math.isclose(1, 1.0000001, abs_tol=1e-8))

print(math.isclose(1, 1.00000001, abs_tol=1e-8))

# %%
# nan and inf are not close to anything
# nan is not close to itself
# inf is close to itself

print(math.isclose(math.nan, 1e308))

print(math.isclose(math.nan, math.nan))

print(math.isclose(math.inf, 1e308))

print(math.isclose(math.inf, math.inf))
