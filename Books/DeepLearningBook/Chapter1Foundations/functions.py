# NumPy code caveats for use of functions
# caveat #1 use of NumPy arrays
import numpy as np
import matplotlib.pyplot as plt
from functions_funcs import leaky_relu, square

print('Python list operations:')

a = [1, 2, 3]
b = [4, 5, 6]

print('a + b: ', a + b)

try:
    print(a * b)
except TypeError:
    print('a * b has no meaning for python lists')
print()

print('numpy array operations:')

c = np.array([1, 2, 3])
d = np.array([4, 5, 6])

print('c + d: ', c + d)
print('c * d: ', c * d)

e = np.array([[1, 2], [3, 4]])

print('e:')
print(e)
print('e.sum(axis=0)', e.sum(axis=0))
print('e.sum(axis=1)', e.sum(axis=1))

f = np.array([[1, 2, 3],
              [4, 5, 6]])

g = np.array([10, 20, 30])

print('f + g:\n', f + g)


fig, ax = plt.subplots(1, 2, sharey=True, figsize=(12, 6))  # 2 Rows, 1 Col

input_range = np.arange(-2, 2, 0.01)
ax[0].plot(input_range, square(input_range))
ax[0].plot(input_range, square(input_range))
ax[0].set_title('Square function')
ax[0].set_xlabel('input')
ax[0].set_ylabel('input')

ax[1].plot(input_range, leaky_relu(input_range))
ax[1].plot(input_range, leaky_relu(input_range))
ax[1].set_title('"ReLU" function')
ax[1].set_xlabel('input')
ax[1].set_ylabel('output')

plt.show()
