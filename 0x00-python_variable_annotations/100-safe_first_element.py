#!/usr/bin/env python3
""" Function with duck-typed annotations """
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        A function Retrieves the first element of a sequence if it exists.
    """
    if lst:
        return lst[0]
    else:
        return None
