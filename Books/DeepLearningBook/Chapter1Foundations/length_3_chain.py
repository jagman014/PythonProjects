# Three function chain rule
import numpy as np

from nested_functions import Chain, chain_length_2
from derivatives import deriv
from chain_rule import chain_deriv_2


def chain_length_3(chain: Chain, x: np.ndarray) -> np.ndarray:
    """
    Evaluates three functions in a row, in a "Chain".
    """
    assert len(chain) == 3, \
        "Length of input 'chain' should be 3"

    f1 = chain[0]
    f2 = chain[1]
    f3 = chain[2]

    return f3(f2(f1(x)))


def chain_deriv_3(chain: Chain, input_range: np.ndarray) -> np.ndarray:
    """
    Uses the chain rule to compute the derivative of three nested functions:
    (f3(f2(f1(x))))' = f3'(f2(f1(x))) * f2'(f1(x)) * f1'(x)
    """

    assert len(chain) == 3, \
        "This function requires 'Chains' of length 3"

    f1 = chain[0]
    f2 = chain[1]
    f3 = chain[2]

    # f1(x)
    f1_of_x = f1(input_range)

    # f2(f1(x))
    f2_of_x = f2(f1_of_x)

    # df3du
    df3du = deriv(f3, f2_of_x)

    # df2du
    df2du = deriv(f2, f1_of_x)

    # df1dx
    df1dx = deriv(f1, input_range)

    # multiplying these quantities together at each point
    return df1dx * df2du * df3du


def plot_chain(ax, chain: Chain,
               input_range: np.ndarray, length: int = 2) -> None:
    """
    Plots a chain function - a function made up of
    multiple consecutive ndarray -> ndarray mappings - across one range

    ax: matplotlib Subplot for plotting
    """

    assert input_range.ndim == 1, \
        "Function requires a 1 dimensional ndarray as input_range"
    if length == 2:
        output_range = chain_length_2(chain, input_range)
    elif length == 3:
        output_range = chain_length_3(chain, input_range)

    ax.plot(input_range, output_range)


def plot_chain_deriv(ax, chain: Chain,
                     input_range: np.ndarray, length: int = 2) -> None:
    """
    Uses the chain rule to plot the derivative of two nested functions.

    ax: matplotlib Subplot for plotting
    """

    if length == 2:
        output_range = chain_deriv_2(chain, input_range)
    elif length == 3:
        output_range = chain_deriv_3(chain, input_range)

    ax.plot(input_range, output_range)
