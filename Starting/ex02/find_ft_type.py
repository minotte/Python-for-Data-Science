#!/usr/bin/env python3

from typing import Any

def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list):
        print(type(object))
    else:
        print("Type not found")
    return 42

# >python find_ft_type.py | cat -e