def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate the Body Mass Index (BMI) for a list of individuals.

    Args:
        height (list[int | float]): A list of heights in meters.
        weight (list[int | float]): A list of weights in kilograms.

    Returns:
        list[float]: A list of BMI values, calculated using the formula:
                     BMI = weight / (height ** 2)

    Raises:
        ValueError: If height and weight lists are not of the same length.
        TypeError: If any value in the lists is not an integer or float.
    """
    try:
        if len(height) != len(weight):
            raise AssertionError("not the same size")

        if not all(isinstance(h, (int, float)) and h > 0 for h in height):
            raise ValueError("Heights must be positive numbers")

        if not all(isinstance(w, (int, float)) and w > 0 for w in weight):
            raise ValueError("Weights must be positive numbers")

        bmi = [w / (h ** 2) for h, w in zip(height, weight)]
        return bmi

    except AssertionError as e:
        print(f"AssertionError: {e}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Compares BMI values to a given limit and returns a list of boolean values.

    Parameters:

    bmi : list[int | float]
        A list of BMI values.
    limit : int
        The threshold value for BMI.

    Returns:
        list[bool]
        A list where each element is True if the BMI is greater than the limit,
        otherwise False.

    Raises:
        AssertionError: If the BMI list contains non-numeric values or
        if the limit is not an integer.
    """
    try:
        if not all(isinstance(b, (int | float)) for b in bmi):
            raise AssertionError("must be numbers.")
        if not isinstance(limit, int):
            raise AssertionError("limit must be an integer")
        return [b > limit for b in bmi]

    except AssertionError as e:
        print(f"AssertionError: {e}")
