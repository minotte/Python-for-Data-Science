import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    slice_me(family: list, start: int, end: int) -> list:
    This project implements a function that takes a 2D array as input,
    prints its shape, and returns a truncated version of the array based
    on the provided start and end arguments using slicing.

    Args:
        - family (list[list[float]]): A 2D list containing numerical values.
        - start (int): The starting index for slicing.
        - end (int): The ending index for slicing.

    Error:
        - if the lign of family are not equals
        - if start and end are not in the martrice
        - family need to be a list of list
        - start and end need to be int
    Return:
        - the new array2d
    """

    try:

        if not isinstance(family, list) or\
           any(not isinstance(row, list) for row in family):
            raise AssertionError("must be list")

        # check validity of the array
        row_len = len(family[0])
        if any(len(row) != row_len for row in family):
            raise AssertionError("All rows must have the same length")

        if not isinstance(start, int):
            raise AssertionError("start should be int")

        if not isinstance(end, int):
            raise AssertionError("end should be int")

        # print initial form : (lign, collumn)
        print(f"My shape is : {np.shape(family)}")

        trunc_family = family[start:end].copy()
        print(f"My new shape is : {np.shape(trunc_family)}")

        return trunc_family

    except AssertionError as e:
        print(f"Error: {e}")
