#!/usr/bin/env python3

"""
    function to_kv with annotations
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Return tuple of string and doubled float value """
    return (k, v * v)
