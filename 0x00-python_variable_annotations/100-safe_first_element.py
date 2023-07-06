#!/usr/bin/env python3
"""Duck-typed annotations python"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''correct duck-typed annotations'''
    if lst:
        return lst[0]
    else:
        return None
