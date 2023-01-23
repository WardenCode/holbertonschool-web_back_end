#!/usr/bin/env python3
"""
Type-annotated function make_multiplier that
takes a float multiplier as argument and
returns a function that multiplies a float by multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a new function that can multiply a new number by multiplier

    Args:
        multiplier (float): Number to generate the new
        multiplier function

    Returns:
        Callable[[float], float]: A new function that multiply
        a new number by "multiplier"
    """

    def func(number: float) -> float:
        return (multiplier * number)

    return (func)
