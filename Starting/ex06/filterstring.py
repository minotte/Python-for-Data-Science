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
        msg = "the arguments are bad"
        # punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        assert len(sys.argv) == 3, msg
        S, N = sys.argv[1], sys.argv[2]
        assert isinstance(S, str), msg
        assert N[0] in "-+" and N[1:].isdigit() or N.isdigit(), msg
        N = int(N)
        words = S.split()
        assert all(word.isalnum()  for word in words), msg
        filterstring = ft_filter(lambda word: len(word) > N, words)
        fil = filter(lambda word: len(word) > N, words)
        print(list(fil))
        print(list(filterstring))
        print(fil)
        print(filterstring)

    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        sys.exit(1)

    except KeyboardInterrupt:
        print("\nInterruption... Bye!")
        sys.exit(1)


if __name__ == "__main__":
    main()
