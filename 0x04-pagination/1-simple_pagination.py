#!/usr/bin/env python3
"""
def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:

Use assert to verify that arguments are int's and greater than 0.
If the input arguments are out of range for the dataset,
an empty list should be returned.
"""

import csv
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a list of rows, using pagination from the DATA_FILE

        Args:
            page (int, optional): Page to select. Defaults to 1.
            page_size (int, optional): Size of the page. Defaults to 10.

        Returns:
            List[List]: List of rows of DATA_FILE
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0

        init, end = index_range(page, page_size)

        return (self.dataset()[init: end])
