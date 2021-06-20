# all free variables bound in the enclosing scope
def outer_func(x):
    y = 4

    def inner_func(z):
        print(f"x = {x}, y = {y}, z = {z}")

        return x + y + z

    return inner_func


for i in range(3):
    closure = outer_func(i)

    print(f"closure({i + 5}) = {closure(i + 5)}")


# inner_func bound to closure, which captures x and y from the outer_func
# redone with lambda
def outer_func(x):
    y = 4

    return lambda z: x + y + z


for i in range(3):
    closure = outer_func(i)

    print(f"closure({i + 5}) = {closure(i + 5)}")

# lambda assigned to closure in this instance
