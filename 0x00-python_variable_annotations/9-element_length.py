#!/usr/bin/env python3
"""Strongly typed python"""
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns collection tuple'''
    return [(i, len(i)) for i in lst]
