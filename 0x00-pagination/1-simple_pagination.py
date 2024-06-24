#!/usr/bin/env python3
"""task 1 on pagination"""
import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple containing a start index and an end index for
    pagination."""
    start = (page - 1) * page_size
    return (start, start + page_size)


class Server:
    """Server class for paginating a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Returns the cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Finds the correct indexes to paginate the dataset and
        returns the appropriate page."""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        return [] if (start >= len(dataset) or
                end >= len(dataset)) else dataset[start:end]
