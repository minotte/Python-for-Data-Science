def callLimit(limit: int):
    """
    A decorator that limits the number of calls to a function.

    Args:
        limit (int): The maximum number of times the function can be called.

    Returns:
        function: A wrapped function that enforces the call limit.
    """
    count = 0

    def callLimiter(function):
        """
        A wrapper function that enforces a call limit on the given function.

        This function is part of the `callLimit` decorator.
        It keeps track of how many times the decorated function has been called
        and prevents further execution once the limit is exceeded.

        Args:
            function (callable): The function to be wrapped and limited in the
            number of calls.

        Returns:
            callable: A new function (`limit_function`) that checks the call
            count before execution.

        Behavior:
            - If the function has been called fewer times than the specified
            limit, it executes normally.
            - If the function has been called more than the allowed limit, an
            error message is displayed, and the function is not executed.
        """
        nonlocal count

        def limit_function(*args: any, **kwds: any):
            """
            Limits the execution of the decorated function.

            Args:
                *args: Positional arguments for the function.
                **kwargs: Keyword arguments for the function.

            Returns:
                The function result if within the limit, else an error message.
            """
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return
            count += 1
            return function(*args, **kwds)
        return limit_function
    return callLimiter
