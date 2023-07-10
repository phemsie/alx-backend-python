#!/usr/bin/env python3
""" asynchronous coroutine waits for a random delay between 0 and max_delay """
from typing import List
import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    ''' spawn n times wait for a random delay and returns List'''
    waitList = []
    spawnList = []
    for i in range(n):
        waitList.append(wait_random(max_delay))
    for t in asyncio.as_completed(waitList):
        spawnList.append(await t)
    return spawnList
