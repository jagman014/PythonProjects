# before 3.9 needed to import typing
from typing import List

radius: float = 3.9
radii: List[float] = [3.9, 2.4]

# in 3.9 this is redundant
radius: float = 3.9
radii: list[float] = [3.9, 2.4]

# inbuilt generic type hints
# can be used in 3.7 and 3.8 with
# from __future__ import annotations
