from DecoratorsGuide.decorators import debug, do_twice


# order matter with respect to when they're called
@debug
@do_twice
def greet(name):
    print(f'Hello {name}')


# here do_twice acts on debug as well
@do_twice
@debug
def greet_1(name):
    print(f'Hello {name}')


greet('Alice')
greet_1('Bob')
