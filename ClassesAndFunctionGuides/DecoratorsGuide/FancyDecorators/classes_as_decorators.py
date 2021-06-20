import functools


# class need to take the function as an argument
class CountCalls:
    def __init__(self, func):
        # need this instead of @function.wraps for classes
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    # __call__ is  executed after every call
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CountCalls
def say_whee():
    print("Whee!")


say_whee()
say_whee()

# adds class methods to the function
print(say_whee.num_calls)
