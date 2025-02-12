
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
        - if the lign of familly are not equals   
        - if start and end are not in the martrice
        - familly need to be a list of list
        - start and end need to be int
    """

    try:
 
        if len(familly)
            raise AssertionError("please not null")
        row_len = [len(row) for row in familly]
        if not isinstance(start, int) and start >=0 and start <= line
            raise AssertionError("start should be int")
        if not isinstance(stop, int) and stop >=0 and stop <= line
            raise AssertionError("stop should be int")
    except AssertionError as e:
        print(f"Error: {e}")