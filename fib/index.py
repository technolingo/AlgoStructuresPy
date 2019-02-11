def memoize(fn):
    cache = {}

    def wrapped(*args, **kwargs):
        # use a frozenset for kwargs instead of sorted() + str()
        # to accommodate the greatest number of data types possbile
        key = (args, frozenset(kwargs.items()))
        if cache.get(key):
            return cache.get(key)
        result = fn(*args, **kwargs)
        cache[key] = result
        print(cache)
        return result
    return wrapped


@memoize
def fib(n, **kwargs):
    '''
        Get the n-th number in a fibonacci sequence,
        assuming the first 3 numbers are 0, 1, 1
        and we count from the 0th.
    '''

    if n < 2:
        return n
    result = fib(n - 1) + fib(n - 2)
    return result
