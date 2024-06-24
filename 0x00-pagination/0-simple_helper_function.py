#!/usr/bin/env python3
"""
Module: 0-simple_helper_function

This module defines the index_range function for pagination.

Functions:
    index_range(page: int, page_size: int) -> tuple[int, int]:
        Returns a tuple containing the start index and end index
        for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing the start index and end index for pagination.

    Args:
        page (int): Page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        tuple: Start index and end index.
    """
    start = (page - 1) * page_size
    return (start, start + page_size)
