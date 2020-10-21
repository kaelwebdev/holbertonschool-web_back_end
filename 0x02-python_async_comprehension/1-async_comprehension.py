#!/usr/bin/env python3
"""
    function async_generator with async comprehension
"""
import random
from typing import List
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """return 10 random numbers from generator as a List"""
    return [i async for i in async_generator()]
