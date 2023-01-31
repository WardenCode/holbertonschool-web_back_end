#!/usr/bin/env python3
"""
def index_range(page: int, page_size: int) -> Tuple[int, int]:

The function should return a tuple of size two containing a
start index and an end index corresponding to the range of indexes
to return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Get the start and end index of the solicited page

    Args:
        page (int): Actual page
        page_size (int): Size of each page

    Returns:
        Tuple[int, int]: Tuple that contains the
        start and end index of the solicited page
    """
    first_page_element_idx: int = (page - 1) * page_size
    last_page_element_idx: int = page * page_size

    return (first_page_element_idx, last_page_element_idx)
