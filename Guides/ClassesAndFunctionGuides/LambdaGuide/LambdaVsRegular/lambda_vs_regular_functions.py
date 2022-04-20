import dis

# lambda
add = lambda x, y: x + y

print(type(add))
print(dis.dis(add))
print(add)  # returns <lambda> as function name, not useful for traceback


# vs def
def add(x, y):
    return x + y


print(type(add))
print(dis.dis(add))
print(add)  # returns add as function name, more useful in traceback

# lambda functions cannot contain any statements
# i.e. return, assert, raise, pass
# will return a syntax error if they're used
# can be used as single line functions

print((lambda x: (x % 2 and 'odd' or 'even'))(3))

# lambda functions also cannot contain type hints
# supports standard function arguments cues
# i.e. positional, named, *args, **kwargs, keyword-only
