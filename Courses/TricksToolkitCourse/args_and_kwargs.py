# *args and **kwargs
# Example
def bar(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


# bar() needs at least one required argument
# *args collects all other arguments
# **kwargs collects all 'named' key-word arguments

bar('hello') # takes required argument

bar('hello', 1, 2, 3)  # collects args as a tuple

bar('hello', 1, 2, 3, key1='value', key2=999)  # collects kwargs as a dictionary


# in a wrapping function
def foo(x, *args, **kwargs):
    kwargs['name'] = 'Alice'
    new_args = args + ('extra', )
    bar(x, *new_args, **kwargs)


foo('x')

foo('x', 1, 2, 3)

foo('hello', 1, 2, 3, key1='value', key2=999)


# subclass example
class Car:
    def __init__(self, colour, mileage):
        self.colour = colour
        self.mileage = mileage


# Useful, but has an unhelpful argument set
# Best to add a docstring
class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.colour = 'blue'
