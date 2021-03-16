#!/usr/bin/env python3
'''type-annotated function safely_get_value'''
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    '''returns value'''
    if key in dct:
        return dct[key]
    else:
        return default
