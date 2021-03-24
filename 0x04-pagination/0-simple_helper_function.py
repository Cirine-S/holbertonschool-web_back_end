#!/usr/bin/env python3
"""
Simple Helper func
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
	start_index = page * page_size - page_size
	end_index = page * page_size
	return (start_index, end_index)
