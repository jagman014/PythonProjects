from DecoratorsGuide.SimpleDecorators.reusing_decorators import say_whee

print(repr(print))
print(repr(print.__name__))

# function is confused, returns wrapper function ids, fixed by @functools.wraps() in decorator
print(repr(say_whee))
print(repr(say_whee.__name__))
