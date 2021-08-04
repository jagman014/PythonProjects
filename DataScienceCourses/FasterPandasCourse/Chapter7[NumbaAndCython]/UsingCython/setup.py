from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('relu.pyx'))

# run "python setup.py build_ext --inplace"
