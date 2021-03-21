#!/usr/bin/env python3
'''asynchronous coroutine'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''returns the given argument'''
    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    return x
