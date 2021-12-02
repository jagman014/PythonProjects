import cython


def primes(nb_primes: cython.int):
    i: cython.int
    p: cython.int[1000]

    if nb_primes > 1000:
        nb_primes = 1000
    
    if not cython.compiled:  # Only if regular Python is running
        p = [0] * 1000       # Make p work almost like a C array
    
    len_p: cython.int = 0  # The current number of elements in p
    n: cython.int = 2

    while len_p < nb_primes:
        # Is n prime?
        for i in p[:len_p]:
            if n % i == 0:
                break

        # If no break occurs we have a prime (for-else)
        else:
            p[len_p] = n
            len_p += 1
            
        n += 1
    
    # Copy result into python list
    result_as_list = [prime for prime in p[:len_p]]
    return result_as_list
