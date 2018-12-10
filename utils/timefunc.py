import time


def timeit(func):
    def timed(*args, **kwargs):
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        print('{} {:.2f} ms'.format(func.__name__, (te - ts) * 1000))
        return result
    return timed
