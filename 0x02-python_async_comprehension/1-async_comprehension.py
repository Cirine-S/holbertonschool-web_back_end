#!/usr/bin/env python3
'''Async coroutine'''
import asyncio
import random
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    ''' it will return the 10 random numbers'''
    x = [i async for i in async_generator()]
    return x
