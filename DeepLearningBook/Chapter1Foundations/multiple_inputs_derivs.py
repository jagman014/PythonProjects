# Derivatives of multiple input functions
import numpy as np
from nested_functions import Array_Function
from derivatives import deriv


def multiple_inputs_add_backward(x: np.ndarray, y: np.ndarray,
                                 sigma: Array_Function) -> float:
    """
    Computes the derivative of this simple function with respect to
    both inputs
    """
    # Compute "forward pass"
    a = x + y

    # Compute derivatives
    dsda = deriv(sigma, a)

    dadx, dady = 1, 1

    return dsda * dadx, dsda * dady
