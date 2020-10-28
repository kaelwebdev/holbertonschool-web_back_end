#!/usr/bin/env python3
"""
    class Server
"""
import csv
import math
from typing import List, Dict, Union

index_range = __import__('0-simple_helper_function').index_range


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
        get current page data
        """
        assert type(page_size) is int and page_size > 0 and type(page) is int\
            and page > 0
        r = index_range(page, page_size)
        start = r[0]
        end = r[1]
        if start >= len(self.dataset()):
            return []
        return self.dataset()[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> \
            Dict[str, Union[int, List[list]]]:
        """
        return dictionary (with pages info)
        """
        t_p = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": len(self.get_page(page, page_size)),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page + 1 <= t_p else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": t_p
        }
