#!/usr/bin/env python3
"""
    The function should return a tuple of size
    two containing a start index and an end index
    corresponding to the range of indexes to return
    in a list for those particular pagination parameters.
    Page numbers are 1-indexed, i.e. the first page is page 1.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return the position range according to the position
    of the page and the maximum number of records per cycle
    """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
