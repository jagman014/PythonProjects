# python 3.8
from typing import List, Union

def sum_list(numbers: List[Union[float, int]]) -> float:
    pass

# python 3.10
def sum_list(numbers: list[float | int]) -> float:
    pass

# optional
address: str | None

# union at runtime
isinstance(address, str | int)

# type alias
from typing import TypeAlias

Card: TypeAlias = tuple[str, str]
Deck: TypeAlias = list[Card]

# type guards
def get_ace(suit: str | None) -> tuple[str, str]:
    if suit is None: # guards the or None
        suit = "♠"
    
    return (suit, 'A')

# type guard declaration
from typing import TypeGuard, Any

# custom type guard
def is_deck_of_cards(obj: Any) -> TypeGuard[Deck]:
    return isinstance(obj, Deck)

def get_score(card_or_deck: Card | Deck) -> int:
    if is_deck_of_cards(card_or_deck):
        # calculate score of deck of cards
        pass

    # calculate score of card
    pass

# decorators
# pre 3.10
import functools
from typing import Callable, TypeVar

R = TypeVar('R')

# wraps function with some args
def decorator(func: Callable[..., R]) -> Callable[..., R]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> R:
        ...
    return wrapper

# 3.10
from typing import ParamSpec

P = ParamSpec('P') # pass type hints through decorator

def decorator(func: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        ...
    return wrapper

# introspect annotations
import inspect

def mean(numbers: list[int | float]) -> float:
    return sum(numbers) / len(numbers)

inspect.get_annotations(mean)
