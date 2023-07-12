#!/usr/bin/env python3
""" A type-annotated function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        A unction make_multiplier that takes a float multiplier as
        argument and returns a function that multiplies a float by
        multiplier
    """
    return lambda value: value * multiplier
