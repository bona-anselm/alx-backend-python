#!/usr/bin/env python3
""" An asynchronous coroutine, that waits for a random seconds """
import asyncio
import random


async def wait_random(max_delay=10):
    """
        Asynchronous coroutine that waits for a random delay between 0
        and max_delay (inclusive) seconds and returns it.

        Args:
            max_delay (float, optional): The maximum delay in seconds.
            Defaults to 10.

        Returns:
            float: The randomly generated delay.
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
