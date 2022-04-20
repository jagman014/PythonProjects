# chain rule derivation
import numpy as np
from derivatives import deriv
from nested_functions import Chain, chain_length_2


def chain_deriv_2(chain: Chain, input_range: np.ndarray) -> np.ndarray:
    """
    Uses the chain rule to compute the derivative of two nested functions:
    (f2(f1(x)))' = f2'(f1(x)) * f1'(x)
    """

    assert len(chain) == 2, \
        'This function requires a "Chain" object of length 2'

    assert input_range.ndim == 1, \
        'Function requires a 1D ndarray as input_range'

    f1 = chain[0]
    f2 = chain[1]

    # df1/dx
    f1_of_x = f1(input_range)

    # df1/du
    df1dx = deriv(f1, input_range)

    # df2/du(f1(x))
    df2du = deriv(f2, f1_of_x)

    # multiply these quantities at each point
    return df1dx * df2du


def plot_chain(ax,
               chain: Chain,
               input_range: np.ndarray) -> None:
    """
    Plots a chain function - a function made up of
    multiple consecutive ndarray -> ndarray mappings -
    Across the input_range

    ax: matplotlib Subplot for plotting
    """

    assert input_range.ndim == 1, \
        "Function requires a 1 dimensional ndarray as input_range"

    output_range = chain_length_2(chain, input_range)
    ax.plot(input_range, output_range)


def plot_chain_deriv(ax, chain: Chain, input_range: np.ndarray) -> None:
    """
    Uses the chain rule to plot the derivative of a function
    consisting of two nested functions.

    ax: matplotlib Subplot for plotting
    """
    output_range = chain_deriv_2(chain, input_range)
    ax.plot(input_range, output_range)
