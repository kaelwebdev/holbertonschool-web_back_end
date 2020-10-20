#!/usr/bin/env python3
"""
    function wait_random with async/await
    protip:
    random.random() -> range [0.0, 1.0)
    random.uniform(a, b) -> range [a, b]
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ return random float from range 0 to max_delay """
    r_n = random.uniform(0, max_delay)
    await asyncio.sleep(r_n)
    return r_n
