#!/usr/bin/env python3
""" A type-annotated function """
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        A type-annotated function that computes the length of a list of
        sequences
    """
    return [(i, len(i)) for i in lst]
