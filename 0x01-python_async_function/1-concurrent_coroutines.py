#!/usr/bin/env python3
"""
    function wait_n with async/await
    protip: You should use a task when
    you want your coroutine to effectively
    run in the background. There are situations
    when you want operations to run in parallel.
    In that case asyncio.create_task is the
    appropriate tool, because it turns over the
    responsibility to execute the coroutine to
    the event loop. This allows you to start several
    coroutines and sit idly while they execute,
    typically waiting for some or all of them to finish
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ return array of delays"""
    d: List[float] = []
    for i in range(n):
        d.append(asyncio.create_task(wait_random(max_delay)))
    return [await delay for delay in asyncio.as_completed(d)]
