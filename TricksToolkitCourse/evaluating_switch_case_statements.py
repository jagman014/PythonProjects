# Example
# if cond == 'cond_a':
#     handle_a()
# elif cond == 'cond_b':
#     handle_b()
# else:
#     handle_default()

# Alternatively, multiple functions in a list or dictionary (use get to avoid key errors)
# def my_func(a, b):
#     return function_result

# funcs = [my_func]
# funcs[0](a, b)

def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    else:
        return None


# Similar dictionary of functions, not good for memory reasons,
# better to define dictionary as a variable outside of function
def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y
    }.get(operator, lambda: None)()

