#!/usr/bin/env python3
"""
    function task_wait_n with async/await
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ return array of delays"""
    d: List[float] = []
    for i in range(n):
        d.append(task_wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(d)]
