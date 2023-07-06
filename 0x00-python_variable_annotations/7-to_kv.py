#!/usr/bin/env python3
"""Strongly typed python"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Returns the union tuple'''
    return k, v ** 2
