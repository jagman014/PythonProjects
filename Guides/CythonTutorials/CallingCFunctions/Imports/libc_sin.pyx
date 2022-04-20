from libc.math cimport sin
# C math library

cdef double f(double x):
    return sin(x * x)
