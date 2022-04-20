# new decorators
import functools


def normal(func):
    return func


def shout(func):
    @functools.wraps(func)
    def shout_decorator(*args, **kwargs):
        return func(*args, **kwargs).upper()
    
    return shout_decorator


# before in 3.8

@normal
def first():
    return 'It was the best of times,'


@shout
def second():
    return 'It was the worst of times,'


print(first())
print(second())

# in 3.9, can create a dictionary of decorators
# decorators are bound at module load
# decorator cannot be changed once set

DECORATORS = {
    'normal': normal,
    'shout': shout,
}

voice = input('Choose: ')


@DECORATORS[voice]
def third():
    return 'In a hole in the ground there lived a hobbit.'


print(third())
