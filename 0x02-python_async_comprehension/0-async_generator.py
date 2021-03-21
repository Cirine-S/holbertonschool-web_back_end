#!/usr/bin/env python3
'''
Contains a coroutine.
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''it'll loop 10 times, wait, then yield a random number between 0 & 10'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
