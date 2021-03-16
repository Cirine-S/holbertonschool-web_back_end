#!/usr/bin/env python3
'''type-annotated function safe_first_element'''
from typing import List, Iterable, Sequence, Tuple, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''returns an element'''
    if lst:
        return lst[0]
    else:
        return None
