def import_from_script_in_same_dir():
    from foobar import foo, bar
    foo()
    bar()
    # Alternative import way
    import foobar
    foobar.foo()
    foobar.bar()


def import_from_custom_pkg():
    from utils import checkpath, helper
    checkpath.show_path()
    helper.greet('Hello from main')


if __name__ == '__main__':
    import_from_script_in_same_dir()
    import_from_custom_pkg()
