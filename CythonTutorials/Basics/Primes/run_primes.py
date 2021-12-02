import primes_py
import primes_py_compiled
import primes_cy
import primes_cy_cpp

print('Python: ')
print(primes_py.primes(100))
print()

print('Python Compiled: ')
print(primes_py_compiled.primes(100))
print()

print('Cython: ')
print(primes_cy.primes(100))
print()

print('Cython C++: ')
print(primes_cy_cpp.primes(100))
print()
