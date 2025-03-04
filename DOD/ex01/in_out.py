def square(x: int | float) -> int | float:
    """
    pow(x: int | float) -> int | float:
    Computes the square of a given number.

    Args:
        x (int | float): The number to be squared.

    Returns:
        int | float: The square of the input number
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    pow(x: int | float) -> int | float:
    Computes the exponentiation of a number by itself (x ** x).

    Args:
        x (int | float): The number to be raised to the power of itself.

    Returns:
        int | float: The result of x raised to the power of x.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    outer(x: int | float, function) -> object
    Returns an inner function that applies the given function iteratively.

    Args:
        x (int | float): The initial number.
        function (callable): A function to apply iteratively on x.

    Returns:
        object: A callable inner function that, when executed,
                applies the given function to the stored value and updates it.
    """
    def inner() -> float:
        """
        Applies the provided function to the stored value and updates it.

        Returns:
            float: The result of applying the function to the current value.
        """
        nonlocal x
        result = function(x)
        x = result
        return result

    return inner
