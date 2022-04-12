# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:00:19 2019

@author: jaredalbert
"""
from collections import Counter

import doctest


def sum_counters(l1, l2):
    """Aggregate collections.Counter objects by summing counts

    :param counters: list/tuple of counters to sum
    :return: aggregated counters with counts summed

    >>> d1 = 'hello'
    >>> d2 = 'world'
    >>> sum_counters(d1,d2)
    'helloworld(intentional error)'
    """
    return (d1+d2)

doctest.testmod()