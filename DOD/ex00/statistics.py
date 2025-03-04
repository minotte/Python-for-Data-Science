def median(lst: list) -> list:
    """
    Calculates the median of a sorted list.

    Args:
        lst: Sorted list of numbers.

    Returns:
        float: The median of the list.
    """
    n = len(lst)
    if n % 2:
        return lst[n // 2]
    else:
        median = (lst[n // 2 - 1] + lst[n // 2]) / 2
        return median


def quartilles(lst: list) -> list:
    """
    Calculates the first (Q1) and third (Q3) quartiles of a sorted list.

    Args:
        lst: Sorted list of numbers.

    Returns:
        list: A list containing [Q1, Q3].
    """
    mid = len(lst) // 2
    quartille = []

    if len(lst) % 2 == 0:
        lower_half = lst[:mid]
        upper_half = lst[mid:]
    else:
        lower_half = lst[:mid]
        upper_half = lst[mid + 1:]

    Q1 = median(lower_half)
    quartille.append(Q1)
    Q3 = median(upper_half)
    quartille.append(Q3)
    return quartille


def mean(data) -> float:
    """
    Calculates the mean (average) of a list of numbers.

    Args:
        data: List of numbers.

    Returns:
        float: The mean of the list.
    """
    return (sum(data) / len(data))


def standard_deviation(data: list) -> float:
    """
    Calculates the standard deviation of a list of numbers.

    Args:
        data : List of numbers.

    Returns:
        float: The standard deviation of the list.
    """
    var = variance(data)
    std = var ** 0.5
    return std


def variance(data: list) -> float:
    """
    Calculates the variance of a list of numbers.

    Args:
        data: List of numbers.

    Returns:
        float: The variance of the list.
    """
    m = mean(data)
    var = sum((x - m) ** 2 for x in data) / len(data)
    return var


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Prints statistical calculations for a list of numbers based on
    the provided `kwargs` options.

    Args:
        *args: A list of numbers for statistical calculations.
        **kwargs: Options specifying which calculation to perform.
                  Possible values:
                  - "mean" : Mean (average)
                  - "median" : Median
                  - "quartile" : First (Q1) and third (Q3) quartiles
                  - "std" : Standard deviation
                  - "var" : Variance

    Returns:
        None: Prints the results directly.
    """
    try:
        data = sorted(args)
        for value in kwargs.values():
            if len(args) == 0:
                print("ERROR")
            elif value == "mean":
                print("mean : ", mean(data))
            elif value == "median":
                print(f"median : {median(data)}")
            elif value == "quartile":
                print(f"quartile : {quartilles(data)}")
            elif value == "std":
                print(f"standard_deviation : {standard_deviation(data)}")
            elif value == "var":
                print(f"variance : {variance(data)}")

    except Exception:
        print("Error: List not valid")
        return
