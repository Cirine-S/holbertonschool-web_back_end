#!/usr/bin/env python3
'''Async coroutine'''
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' It measures the total runtime and return it'''
    s = time.perf_counter()
    r = await asyncio.gather(*(async_comprehension() for i in range(4)))
    return time.perf_counter() - s
