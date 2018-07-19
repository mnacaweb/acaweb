# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from functools import wraps


def memoize(func, cache, num_args):
    @wraps(func)
    def wrapper(*args):
        mem_args = args[:num_args]
        if mem_args in cache:
            return cache[mem_args]
        result = func(*args)
        cache[mem_args] = result
        return result

    return wrapper
