#!usr/bin/env python3

from typing import Any

def all_thing_is_obj(object: any) -> int:
    print(type(object))
    return 42

# >python find_ft_type.py | cat -e