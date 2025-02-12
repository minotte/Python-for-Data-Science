#!/usr/bin/env python3

from typing import Any
import math

def NULL_not_found(object: any) -> int:

    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, float) and math.isnan(object):
        print(f"Cheese: {object} {type(object)}")
    elif object == 0 and isinstance(object, int):
        print(f"Zero: {object} {type(object)}")
    elif object == "" and isinstance(object, str):
        print(f"Empty: {type(object)}")
    elif object is False:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")
        return 1

    return 0


# Write a function that prints the object type of all types of "Null".
# Return 0 if it goes well and 1 in case of error.
# Your function needs to print all types of NULL

# $>python tester.py | cat -e
# Nothing: None <class 'NoneType'>$
# Cheese: nan <class 'float'>$
# Zero: 0 <class 'int'>$
# Empty: <class 'str'>$
# Fake: False <class 'bool'>$
# Type not Found$
# 1$