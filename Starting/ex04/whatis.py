#!/usr/bin/env python3

import sys
from typing import Any


if (len(sys.argv) == 1):
    exit(1)
elif (len(sys.argv) == 2):
    try:
        nb = int(sys.argv[1])
        if nb % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
        exit(0)
    except ValueError:
        print("AssertionError: argument is not an integer")
        exit(1)
else:
    print("AssertionError: more than one argument is provided")
    exit(1)



# $> python whatis.py 14
# I'm Even.
# $>
# $> python whatis.py -5
# I'm Odd.
# $>
# $> python whatis.py
# $>
# $> python whatis.py 0
# I'm Even.
# $>
# $> python whatis.py Hi!
# AssertionError: argument is not an integer
# $>
# $> python whatis.py 13 5
# AssertionError: more than one argument is provided
