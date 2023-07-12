#!/usr/bin/env python3
""" A type-annotated function """


from typing import Any, Mapping, Optional, TypeVar, Union

T = TypeVar('T')
Resp = Union[Any, T]
Defl = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Defl = None) -> Resp:
    """
        A function that retrieves a value from a dict using a given key.
    """
    if key in dct:
        return dct[key]
    else:
        return default
