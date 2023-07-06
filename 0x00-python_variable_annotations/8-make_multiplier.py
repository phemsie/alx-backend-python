#!/usr/bin/env python3
"""Strongly typed python"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns a function that multiplies'''
    def mul(n: float) -> float:
        '''returns multiplication'''
        return n * multiplier
    return mul
