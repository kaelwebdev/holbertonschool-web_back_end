#!/usr/bin/env python3
"""
    function async_generator with yield and async/await
"""

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """ Create generator of random values with range """
    for n in range(10):
        await asyncio.sleep(1)
        yield 10 * random.random()
