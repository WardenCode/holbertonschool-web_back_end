#!/usr/bin/env python3
"""
Annotate the below function's parameters and
return values with the appropriate types
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Take an iterable of sequences and generate a list of tuples,
    that contain the sequence and it's length

    Args:
        lst (Iterable[Sequence]): Iterable of sequences

    Returns:
        List[Tuple[Sequence, int]]: List of tuples that contain
        the sequence and it's length
    """
    return [(i, len(i)) for i in lst]
