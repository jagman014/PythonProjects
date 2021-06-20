# Derviation of matrix multiplication function
import numpy as np


def matmul_backward_first(X: np.ndarray, W: np.ndarray) -> np.ndarray:
    """
    Computes the backward pass of a matrix multiplication with respect to the first argument.
    """

    # backward pass
    dNdX = np.transpose(W, (1, 0))

    return dNdX
