#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for sorting lists.

Module contents:
    - searching: search for an item in a list and returns all
    the list components that contains the to_search variable.

Created on XX XX XX
@author: Evan Cole
"""
def searching(a:list, to_search) -> list:
    """ 
    returns a list with the number of character 
    that are the same as the characters in the input
    Parameters:
    to_search: the variable to search for
    a: list to search variable in
    Returns:
    a list with the variable 'search' repeated
    >>> searching(['hiba','Daffallah','ice cream'],'i')
    ['hiba', 'ice cream']
    >>> searching (['wafaa','Juice'],'j')
    ['Juice']
    >>> searching (['abdallah','bismallah'],'allah')
    ['abdallah', 'bismallah']
    """
    assert isinstance(to_search, str), "input must be character or string"
    c = []
    while a:
        if to_search.lower() in a[0].lower():
            c.append(a[0])
        a = a[1:]
    return c
