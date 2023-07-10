#!/usr/bin/env python3
'''An async coroutine wait_n that takes 2 integer arguments'''

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' Spawns wait_random n times with the specified max_delay '''
    # create a list to store all the tasks
    events = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    # wait for all tasks to complete and gather their results
    delays = await asyncio.gather(*events)

    # return the list of delays sorted in ascending order
    return sorted(delays)
