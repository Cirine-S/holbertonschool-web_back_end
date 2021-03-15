#!/usr/bin/env python3
'''type-annotated function add'''

from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Returns a list.
    '''
    return [(i, len(i)) for i in lst]
