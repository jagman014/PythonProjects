# can use functions as return values
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    # functions not called, such that it returns a reference to the inner functions
    if num == 1:
        return first_child
    else:
        return second_child


first = parent(1)
second = parent(2)

# can now call inner functions
print(first())
print(second())
