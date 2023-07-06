#!/usr/bin/env python3
"""Strongly typed python"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Returns the sum float'''
    return sum(mxd_lst)
