#!/usr/bin/env python3
""" asynchronous coroutine waits for a random delay """
from typing import List
import asyncio
import random


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    ''' spawn n times wait calling task_wait_random'''
    waitList = []
    spawnList = []
    for i in range(n):
        waitList.append(task_wait_random(max_delay))
    for t in asyncio.as_completed(waitList):
        spawnList.append(await t)
    return spawnList
