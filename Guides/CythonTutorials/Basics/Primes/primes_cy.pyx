def primes(int nb_primes):
    cdef int n, i, len_p
    cdef int p[1000]

    if nb_primes > 1000:
        n = 1000
    
    len_p = 0  # the current number of elements in p
    n = 2

    while len_p < nb_primes:
        # is n prime?
        for i in p[:len_p]:
            if n % i == 0:
                break
            
        # no breaks means the number is prime (for-else)
        else:
            p[len_p] = n
            len_p += 1
        
        n += 1
    
    # copy result to python list
    result_as_list = [prime for prime in p[:len_p]]
    return result_as_list
