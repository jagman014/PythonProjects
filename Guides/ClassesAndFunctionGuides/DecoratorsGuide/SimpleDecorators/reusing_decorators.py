# can be used just like other functions
from DecoratorsGuide.decorators import do_twice


@do_twice
def say_whee():
    print("Whee!")


say_whee()
