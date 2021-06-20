# Matrx multiplication function
import numpy as np


def matmul_forward(X: np.ndarray,
                   W: np.ndarray) -> np.ndarray:
    """
    Computes the forward pass of a matrix multiplication
    """
    
    assert X.shape[1] == W.shape[0], \
    f"""
    For matrix multiplication, the number of columns in the first array should
    match the number of rows in the second, instead the number of columns in 
    the first array is {X.shape[1]} and the number of rows in the second array 
    is {W.shape[0]}
    """

    # matrix multiplication
    N = np.dot(X, W)

    return N
