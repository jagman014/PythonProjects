import cython
from cython.cimports.strstr import strstr  # *.pxd file import


def main():
    data: cython.p_char = "hfvcakdfagbcffvschvxcdfgccbcfhvgcsnfxjh"

    pos = strstr(needle="akd", haystack=data)
    print(pos is not cython.NULL)
