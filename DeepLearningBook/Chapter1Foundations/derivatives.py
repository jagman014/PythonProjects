# Derivative example code using limit approximation
from typing import Callable
import numpy as np


def deriv(func: Callable[[np.ndarray], np.ndarray],
          input_: np.ndarray,
          delta: float = 0.01) -> np.ndarray:
    """
    Evaluates the derivative of a function 'func' at every element in the input
    """
    return (func(input_ + delta) - func(input_ - delta)) / (2 * delta)
