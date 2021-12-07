import cython
from cython.cimports.libc.math import sin
# C math library


@cython.cfunc
def f(x: cython.double) -> cython.double:
    return sin(x * x)
