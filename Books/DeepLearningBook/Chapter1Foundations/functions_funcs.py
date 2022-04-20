# NumPy code caveats for use of functions
# caveat #1 use of NumPy arrays
import numpy as np


# Code caveat #2 type-checked functions
def square(x: np.ndarray) -> np.ndarray:
    """
    Square each element in the input ndarry
    """
    return np.power(x, 2)


def leaky_relu(x: np.ndarray) -> np.ndarray:
    """
    Apply "Leaky ReLU" function to each element in ndarry
    """
    return np.maximum(0.2 * x, x)


def sigmoid(x: np.ndarray) -> np.ndarray:
    """
    Apply the sigmoid function to each element in the input array
    """
    return 1 / (1 + np.exp(-x))
