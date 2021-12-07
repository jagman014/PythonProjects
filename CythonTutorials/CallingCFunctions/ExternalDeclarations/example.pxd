# Example if the math.h header was external
# *.pxd used for c library in pure python mode
# *.pxd allows for sharing between cython files, like header files in c
"""
>>> sin(0)
0.0
"""

cdef extern from "math.h":
    # cpdef provides python wrapper for c functions
    cpdef double sin(double x)
