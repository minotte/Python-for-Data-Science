#!/usr/bin/env python3

def ft_tqdm(lst: range) -> None:
    """
    ft_tqdm(lst: range)
    A simplified version of tqdm to visualize progress in the terminal.

    Args:
        lst (range): A range of values to iterate over.

    Yields:
        int: The current value of the iteration.

    Example:
        >>> for i in ft_tqdm(range(10)):
        ...     sleep(0.1)
    """
    total = len(lst)
    col = 80

    for i in lst:
        percent = ((i+1) / total) * 100
        bar_length = int(((i+1) / total) * col)
        progress = "=" * bar_length + ">" + " " * (col - bar_length)
        print(f"\r{int(percent)}%|[{progress}]| {i+1}/{total}", end="")
        yield i
