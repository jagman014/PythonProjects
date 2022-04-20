# works but is best avoided
def throw(ex):
    raise ex


# extracts raise statement to use within lambda function
(lambda: throw(Exception('Something bad happened')))()
