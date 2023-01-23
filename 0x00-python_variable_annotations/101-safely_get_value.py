#!/usr/bin/env python3
"""
Given the parameters and the return values, add
type annotations to the function

In order to pass the checks, be carefull with the order of the Union.

Hint: look into TypeVar
"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Get safely a value of a dictionary (Mapping obj)

    Args:
        dct (Mapping): Mapping obj that contain the keys and values
        key (Any): Key to search on mapping obj (dct)
        default (Union[T, None], optional): Default value in case the
        key doesn't exists on dct. Defaults to None.

    Returns:
        Union[Any, T]: Return the value if exists, default otherwise
    """
    if key in dct:
        return dct[key]
    else:
        return default
