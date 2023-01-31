#!/usr/bin/env python3
"""
def get_hyper(self, page: int = 1,
                page_size: int = 10) -> Dict[str, Union[int, List, None]]:

Returns a dictionary containing the following key-value pairs:
    page_size: Length of the returned dataset page
    page: Current page number
    data: the dataset page
    next_page: number of the next page or None
    prev_page: number of the previous page or None
    total_pages: the total number of pages in the dataset as an integer
"""

import csv
import math
from typing import Dict, List, Tuple, Union


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

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str, Union[int, List, None]]:
        """
        Get a Hyper media pagination response

        Args:
            page (int, optional): Page requested. Defaults to 1.
            page_size (int, optional): Size of each page. Defaults to 10.

        Returns:
            Dict[str, Union[int, List, None]]: Hyper media pagination
            with data
        """

        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return ({
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if (page + 1) <= total_pages else None,
            "prev_page": page - 1 if (page - 1) > 0 else None,
            "total_pages": total_pages,
        })
