# Immediately Invoked Function Expression (IIFE)
print((lambda x, y: x + y)(2, 3))


# higher order functions
def high_ord_func(x, func):
    return x + func(x)


print(high_ord_func(2, lambda x: x * x))
print(high_ord_func(2, lambda x: x + 3))
