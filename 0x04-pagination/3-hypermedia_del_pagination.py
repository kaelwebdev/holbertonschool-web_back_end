#!/usr/bin/env python3
"""
    Deletion-resilient hypermedia pagination
    The goal here is that if between two queries,
    certain rows are removed from the dataset,
    the user does not miss items from dataset when changing page.
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) ->\
            Dict[str, Any]:
        """
            returns information without considering the deleted indices
        """
        assert type(index) is int and type(page_size) is int
        assert 0 <= index < len(self.indexed_dataset())

        return {
            "index": index,
            "data": self.dataset()[index: index + page_size],
            "page_size": len(self.dataset()[index: index + page_size]),
            "next_index": index + page_size
        }
