from DecoratorsGuide.decorators import count_calls


@count_calls
def say_whee():
    print("Whee!")


say_whee()
say_whee()

# count stored in func.num_calls, defined above as wrapper_count_calls.num_calls
print(say_whee.num_calls)
