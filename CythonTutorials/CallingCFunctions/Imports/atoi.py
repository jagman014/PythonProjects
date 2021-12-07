import cython
from cython.cimports.libc.stdlib import atoi
# standard cimport files in venv/lib/Cython/includes
# atoi converts char[] to int


@cython.cfunc
def parse_charptr_to_py_int(s: cython.p_char):
    assert s is not cython.NULL, "byte string value is NULL"
    return atoi(s)  # atoi, has no error detection
