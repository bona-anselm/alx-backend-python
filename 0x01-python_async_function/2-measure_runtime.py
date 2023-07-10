#!/usr/bin/env python3
'''
    A measure_time function that takes two integers n and max_delay as
    arguments
'''
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
        A measure_time function that takes two integers n and max_delay
        as arguments
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
