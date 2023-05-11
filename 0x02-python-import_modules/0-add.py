#!/usr/bin/python3
"""
First make the file usable as a script as well as an importable module
because the code that parses the command line only runs if the module is
executed as the "main" file
"""
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
"""
If the module is imported, the code is not run, so "import add" will not
run code. This is often used either to provide a convenient user interface
to a module, or for testing purposes like running the module as a script
executes a test suite. https://docs.python.org/3.4/tutorial/modules.html
"""
