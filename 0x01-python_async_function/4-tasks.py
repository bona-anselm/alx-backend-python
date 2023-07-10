#!/usr/bin/env python3
'''
    Function task_wait_n
'''

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
        Executes task_wait_random n times with the specified max_delay.
    '''
    delay = await asyncio.gather(
        *tuple(task_wait_random(max_delay) for i in range(n))
    )
    return sorted(delay)
