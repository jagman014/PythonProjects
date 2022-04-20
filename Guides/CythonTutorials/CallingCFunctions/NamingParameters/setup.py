from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "keywords_py",
        sources=["keyword_args_call_py.py"]
    ),
    Extension(
        "keywords_cy",
        sources=["keyword_args_call_cy.pyx"]
    )
]

setup(
    ext_modules=cythonize(ext_modules, annotate=True)
)
