# import_modules

I try to figure out how to import modules in python correctly, I studied three cases:

1. Import from a python script in the same directory
2. Import from another package when in a package
3. Import from a script in this package when in a package

I got following insights:

1. If you want to create a python package, just create a folder and add an empty script `__init__.py` in it
2. Pay attention to **PYTHONPATH**, you can use `sys.path` to check it
3. There are two roots that you should distinguish, they are content roots and source roots,
the former is the directory the script resides in while the latter is the project directory,
for example, if we are dealing with script `helpy.py` under utils in this project, the content roots with absolute path
is `/Users/lqdu/PycharmProjects/import_modules/utils` while the source roots is `/Users/lqdu/PycharmProjects/import_modules`
(this is the case on my pc, they will be different on yours)
4. To make everything works as expected, just add source roots to **PYTHONPATH**, in PyCharm, both content roots and source
roots are added to **PYTHONPATH**

## Project directory structure

```
import_modules
|--config
|  |--__init__.py
|  |--default_settings.py
|--utils
|  |--__init__.py
|  |--checkpath.py
|  |--helper.py
|  |--timefunc.py
|--foobar.py
|--main.py
```

## Examples

In this section, I give you some examples of the three cases.

### Import from a python script in the same directory

An example is given as a function `import_from_script_in_same_dir` in `main.py`:

```python
def import_from_script_in_same_dir():
    from foobar import foo, bar
    foo()
    bar()
    # Alternative import way
    import foobar
    foobar.foo()
    foobar.bar()
```

Here, `foobar.py` and `main.py` are in the same directory, we have two ways to import.

### Import from another package when in a package

You can reference as an example in this case the function `dump_config` defined in `utils/helper.py`.

```python
def dump_config():
    from config import default_settings
    print('loglevel : {}'.format(default_settings.loglevel))
```

Here, we are in package utils and import from package config. If we don't change **PYTHONPATH** and just run `helper.py`,
we'll encounter an error of `ModuleNotFoundError` as follows:

```
(py36) ╭─lqdu@bogon ~/PycharmProjects/import_modules
╰─$ python utils/helper.py
Traceback (most recent call last):
  File "utils/helper.py", line 3, in <module>
    from config import default_settings
ModuleNotFoundError: No module named 'config'
```

If we further check the **PYTHONPATH**, we'll find that content roots is added to the path while the source roots isn't.
You can fix it by adding the source roots to the path. If you work in PyCharm, you will not encounter this because PyCharm
will add content roots and source roots to the path in its defaults.

### Import from a script in this package when in a package

See the function `greet` in `helper.py` for an example in this case.

```python
import time
from utils.timefunc import timeit


@timeit
def greet(greeting, delay=0):
    time.sleep(delay)
    if delay > 0:
        print('{} after 2 seconds'.format(greeting))
    else:
        print(greeting)
```

Here, we are in package utils and `timefunc.py` is a script in it and we import from it in `helper.py`.

## Conclusion

To make everything works as expected, just add source roots to **PYTHONPATH**, in PyCharm, both content roots and source
roots are added to **PYTHONPATH** in its defaults.