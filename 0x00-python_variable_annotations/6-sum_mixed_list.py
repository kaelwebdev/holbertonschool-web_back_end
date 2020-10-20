#!/usr/bin/env python3

"""
    function sum_mixed_list with annotations
    protip: Use Union when something
    could be one of a few types
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Return sum of list containing ints and/or floats """
    return sum(mxd_lst)
