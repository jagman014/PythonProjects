# type hints
from typing import Literal, Union, overload, Final, final, TypedDict, Protocol


def double(number: float) -> float:
    return number * 2


# define type of inputs and outputs
# treated as hints, not evaluated at runtime


print(double(3.8))
print(double('This isn\'t a float'))  # Pycharm will give a warning however


# static type checkers to prevent TypeErrors
# i.e. Mypy
# run: mypy [file_name.py]
# in terminal to reveal errors like pycharm does
# these aren't checked at runtime


# Literal type
def get_status(port: int) -> Literal['connected', 'disconnected']:
    pass


# returned value must be in the literal list


# Example skeleton code
def draw_line(direction: Literal['horizontal', 'vertical']) -> None:
    if direction == "horizontal":
        ...  # Draw horizontal line

    elif direction == "vertical":
        ...  # Draw vertical line

    else:
        raise ValueError(f"invalid direction {direction!r}")


draw_line("up")
# without the Literal, neither mypy nor pycharm would find a TypeError

# calculator

ARABIC_TO_ROMAN = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                   (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                   (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]


def _convert_to_roman_numeral(number: int) -> str:
    """Convert number to a roman numeral string"""
    result = list()
    for arabic, roman in ARABIC_TO_ROMAN:
        count, number = divmod(number, arabic)
        result.append(roman * count)
    return "".join(result)


# overload helps with type checking, '...' required for overload syntax
@overload
def add(num_1: int, num_2: int, to_roman: Literal[True]) -> str: ...
@overload
def add(num_1: int, num_2: int, to_roman: Literal[False]) -> int: ...


def add(num_1: int, num_2: int, to_roman: bool = True) -> Union[str, int]:
    """Add two numbers"""
    result = num_1 + num_2

    if to_roman:
        return _convert_to_roman_numeral(result)
    else:
        return result


# Final, variable can't be overwritten
ID: Final = 1

...

ID += 1
# mypy and pycharm return an error for Final type reassignment
# @final decorator
# means classes can't be subclasses
# methods can't be overridden


@final
class Base:
    ...


class Sub(Base):
    ...
# returns an error as final classes can't be subclassed


# TypedDict
class PythonVersion(TypedDict):
    version: str
    release_year: int


py38 = PythonVersion(version='3.8', release_year=2019)


# Protocol
class Named(Protocol):
    name: str


def greet(obj: Named) -> None:
    print(f'Hi, {obj.name}')


class Dog:
    ...


x = Dog()

greet(x)
# error as Dog doesn't have an attribute of name
