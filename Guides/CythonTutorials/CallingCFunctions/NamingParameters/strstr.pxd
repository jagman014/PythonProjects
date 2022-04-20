cdef extern from "string.h":
    # best to name params in declarations, allows cython to use keyword args
    char* strstr(const char* haystack, const char* needle)
