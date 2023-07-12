#!/usr/bin/env python3
""" a coroutine called async_generator will loop 10 times"""

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    '''will loop 10 times, each time asynchronously'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
