#!/usr/bin/env python3
"""
    function measure_runtime.
    asyncio.gather() ->  sequence concurrently.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ return time of 4 async gather calls """
    tks = []
    t_time = time.time()
    [tks.append(asyncio.create_task(async_comprehension())) for i in range(4)]
    await asyncio.gather(*tks)
    return time.time() - t_time
