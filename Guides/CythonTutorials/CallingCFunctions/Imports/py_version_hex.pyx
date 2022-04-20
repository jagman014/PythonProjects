from cpython.version cimport PY_VERSION_HEX
# set of CPython-C API declarations

# Python version >= 3.2 final ?
print(PY_VERSION_HEX >= 0x030200F0)
