#!/usr/bin/env python3

"""
    function make_multiplier with annotations
    protip: you can see callabe with a function
    representation. So we can return an
    anonymous function and hint at its structure.
    Callable(typeArgs, typeReturn).
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return function that multiplies float by multiplier """
    return lambda x: x * multiplier
