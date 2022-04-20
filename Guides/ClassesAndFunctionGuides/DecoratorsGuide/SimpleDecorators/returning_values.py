from DecoratorsGuide.decorators import do_twice


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


# decorator ate the return value, makes the object NoneType
hi_adam = return_greeting('Adam')
print(hi_adam)
