#!/usr/bin/env python3
""" asynchronous coroutine waits for a random delay between 0 and max_delay """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' waits for a random delay range max_delay '''
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return wait
