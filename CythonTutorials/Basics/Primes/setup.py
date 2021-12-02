from setuptools import setup
from Cython.Build import cythonize

# python setup.py build_ext --inplace 
setup(
    # annotate=True generates the html annotated files
    # white lines run as fast as C, yellow is for python
    ext_modules=cythonize(
        [
            'primes_py.py',
            'primes_cy.pyx',
            'primes_py_compiled.py',
            'primes_cy_cpp.pyx'
        ], 
        annotate=True
    )
)
