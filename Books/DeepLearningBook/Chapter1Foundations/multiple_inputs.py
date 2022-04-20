# Functions with multiple inputs
import numpy as np
from nested_functions import Array_Function


def multiple_inputs_add(x: np.ndarray, y: np.ndarray, 
                        sigma: Array_Function) -> float:
    """
    Function with multiple inputs and addition, forward pass
    """
    assert x.shape == y.shape

    a = x + y
    return sigma(a)
