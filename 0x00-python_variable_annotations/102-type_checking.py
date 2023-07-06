#!/usr/bin/env python3
"""Duck-typed annotations python"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''Type Checked zoom array'''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
