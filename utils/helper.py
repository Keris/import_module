import time

from utils.timefunc import timeit


@timeit
def greet(greeting, delay=0):
    time.sleep(delay)
    if delay > 0:
        print('{} after 2 seconds'.format(greeting))
    else:
        print(greeting)


def dump_config():
    from config import default_settings
    print('loglevel : {}'.format(default_settings.loglevel))


if __name__ == '__main__':
    greet('Hello, world!')
    greet('Hello, China!', 2)
    dump_config()
