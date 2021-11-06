# Importing

Note = \
"""
Importing:
    import <module>                     used to import whole module
    from <module> import <function>     used to import specific functions from the module
    <module/function> as <var>          used to give aliases name to the module or functions
    from <module> import *              used to import all functions a module

Examples:
    -> import numpy
    -> from numpy import pi
    -> from numpy import pi as ABCD
    -> from numpy import *   

===================================================

Avoid Circular Imports:
if your file name is `logging.py` and you `import logging` then you will get an Circular Import error given below

File Content: (EXAMPLE)
    line1 import logging
    line2
    line3 logging.debug('This is a debug message')
Error:
    Traceback (most recent call last):
    File "d:\SchoolPrograms\logging.py", line 1, in <module>
        import logging
    File "d:\SchoolPrograms\logging.py", line 3, in <module>
        logging.debug('This is a debug message')
    AttributeError: partially initialized module 'logging' has no attribute 'debug' (most likely due to a circular import)

"""

print(Note)
