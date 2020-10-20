#!/usr/bin/env python3
"""
    function measure_time with asyncio
    protip: time.perf_counter() is other
    alternative.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measures total execution time for wait_n """
    t_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    t_time = time.time() - t_time
    return t_time / n
