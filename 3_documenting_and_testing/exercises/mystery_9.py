#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for sorting lists.

Module contents:
    - sort_list: sorts the list in ascending order.

Created on XX XX XX
@author: Evan Cole
"""
def sort_list(to_sort_list) -> list:
    """Sorts a list in ascending order
    Parameters:
     to_sort_list: the list that needs to be sorted 
    Returns:
     the sorted list
     >>> sort_list([1,2,3])
     [1, 2, 3]
     >>> sort_list([8,5,2])
     [2, 5, 8]
     >>> sort_list([1])
     [1]
    """
    temp = len(to_sort_list)
    for c in range(temp):
        for d in range(0, temp - c - 1):
            if to_sort_list[d] > to_sort_list[d + 1]:
                to_sort_list[d], to_sort_list[d + 1] = to_sort_list[d + 1], to_sort_list[d]
    return to_sort_list

def new_func(to_sort_list):
    assert isinstance(to_sort_list, list), "input must be list"
