from libc.stdlib cimport atoi
# standard cimport files in venv/lib/Cython/includes
# atoi converts char[] to int

cdef parse_charptr_to_py_int(char* s):
    assert s is not NULL, "Byte string value is NULL"
    return atoi(s)  # atoi, has no error detection
