#!/usr/bin/env python3
"""
Simple Helper Module
"""
import csv
import math
from typing import List, Tuple


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
        """Returns a list of inner lists, where each inner list represents
        a data row from the dataset.
        """
        assert type(page_size) is int and type(page) is int
        assert page > 0
        assert page_size > 0
        self.dataset()
        r = index_range(page, page_size)
        if r[0] >= len(self.__dataset):
            return []
        else:
            return self.__dataset[r[0]:r[1]]

	def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """return a tuple of size two containing a start index and an end index"""
		start_index = page * page_size - page_size
		end_index = page * page_size
		return (start_index, end_index)
