# for the math.h library on unix systems
from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "demo",
        sources=["demo.pyx"],
        libraries=["m"]  # unix specific, linked library
    )
]

setup(
    name="Demos",
    ext_modules=cythonize(ext_modules)
)
