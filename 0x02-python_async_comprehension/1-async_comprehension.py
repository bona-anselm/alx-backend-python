#!/usr/bin/env python3
""" A  coroutine async_comprehension """
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        The coroutine collects 10 random numbers using an async
        comprehensing over async_generator, then return the 10 random
        numbers.
    """
    return [x async for x in async_generator()]
