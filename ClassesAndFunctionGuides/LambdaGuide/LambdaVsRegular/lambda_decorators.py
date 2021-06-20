# Defining a decorator

def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")

        return f(*args, **kwargs)

    return wrap


# Applying decorator to a function
@trace
def add_two(x):
    return x + 2


# Calling the decorated function
print(add_two(3))

# Applying decorator to a lambda, can't use @decorator syntax
print((trace(lambda x: x ** 2))(3))

# better example with map()
print(list(map(trace(lambda x: x*2), range(3))))

# can also use lambda as a decorator, but is not recommended
