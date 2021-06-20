# Example function
def foo_1(value):
    if value:
        return value
    else:
        return None


# Equivalent example
def foo_2(value):
    """
    Empty return function implies: return None
    """
    if value:
        return value
    else:
        return


# Another equivalent
def foo_3(value):
    """
    No return statement implies: return None
    """
    if value:
        return value

# When to use:
# If there are no return statements, don't include a 'return None'
# If the function does have a return function, write an explicit return None
# Allows for conciseness, however can cause confusion
