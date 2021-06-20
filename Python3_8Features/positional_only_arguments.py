# no keyword arguments allowed
# i.e. float('3.8'), not float(x='3.8')

# written as:
def incr(x, /):
    return x + 1


# can use the '/' to separate positional-only, and keyword arguments
def greet(name, /, greeting='Hello'):
    return f'{greeting}, {name}'


# returns a TypeError, if positional-only arguments are used as keyword arguments
# arguments before the '/' are positional-only
# complimented by the '*' for keyword-only for arguments after it
def to_fahrenheit(*, celsius):
    return 32 + celsius * 9 / 5
# requires keyword argument:
# i.e. to_fahrenheit(celsius=40)


# can combine all three: positional, keyword, and regular
def headline(text, /, border='~', *, width=50):
    return f' {text} '.center(width, border)
