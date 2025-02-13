#!/usr/bin/env python3

import sys
from ft_filter import ft_filter


def main():
    """
    it's main fonction of the programme and call ft_filter to
    The program should return every word from S 
    that have a length greater than N.
    args:
        - 1st : string
        - 2nd : int
    Error:
        - if different than two arguments.
        - if the argument have punctuation or invisible character
        - if it's not a int
    Print:
        every word from S that have a length greater than N
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        S, N = sys.argv[1], sys.argv[2]
        try:
            N = int(N)
        except ValueError:
            raise AssertionError("the arguments are bad")

        if not isinstance(S, str):
            raise AssertionError("the arguments are bad")
        words = S.split()
        if not all(word.isalpha() for word in words):
            raise AssertionError("the arguments are bad")
        filterstring = ft_filter(lambda word: len(word) > N, words)
        print(list(filterstring))

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)

    except KeyboardInterrupt:
        print("\nInterruption... Bye!")
        sys.exit(1)


if __name__ == "__main__":
    main()
