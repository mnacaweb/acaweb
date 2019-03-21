# -*- coding: utf-8 -*-



import hashlib
from functools import wraps, partial


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


def hash_file(file, block_size=65536):
    hasher = hashlib.md5()
    for buf in iter(partial(file.read, block_size), b''):
        hasher.update(buf)

    return hasher.hexdigest()


def cv_upload_to(instance, filename):
    instance.cv.open()

    return "cv/{}/{}".format(hash_file(instance.cv), filename)
