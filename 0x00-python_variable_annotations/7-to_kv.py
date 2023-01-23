#!/usr/bin/env python3
"""
Write a type-annotated function to_kv that
takes a string k and an int OR float v as arguments and
returns a tuple. The first element of the tuple is the string k.

The second element is the square of the int/float v and
should be annotated as a float.

You need to keep the same order to pass the checks (Union[int, float]).
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and value, to create a tuple key value.

    Args:
        k (str): String to be used as key on the tuple
        v (int | float): Value to be used as value on the tuple

    Returns:
        tuple[str, int | float]: Tuple key value generated
    """
    result: Tuple[str, float] = (k, v ** 2)

    return (result)
