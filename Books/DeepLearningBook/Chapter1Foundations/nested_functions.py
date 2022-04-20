# Nested functions example
from typing import List, Callable
import numpy as np

# Function takes in an ndarry as an argument and produces an ndarray
Array_Function = Callable[[np.ndarray], np.ndarray]

# Chain is a list of functions
Chain = List[Array_Function]


def chain_length_2(chain: Chain, a: np.ndarray) -> np.ndarray:
    """
    Evaluates two functions in a row, in a chain
    """
    assert len(chain) == 2, \
        "Length of input 'chain' should be 2"

    f1 = chain[0]
    f2 = chain[1]

    return f2(f1(a))
