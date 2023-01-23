#!/usr/bin/env python3
"""
Augment the following code with the correct duck-typed annotations:

You need to keep the same order to pass the checks (Union[Any, None]).
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Get the first elements of a sequence.

    Args:
        lst (Sequence[Any]): Sequence of elements

    Returns:
        Union[Any, None]: First element of a sequence, None otherwise
    """
    if lst:
        return lst[0]
    else:
        return None
