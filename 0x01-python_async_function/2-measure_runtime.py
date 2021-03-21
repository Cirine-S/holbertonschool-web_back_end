#!/usr/bin/env python3
'''asynchronous coroutine'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''measures the total execution time for wait_n and returns total_time/n'''
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
	end_time = time.perf_counter()
    elapsed = end_time - start_time
    return elapsed / n
