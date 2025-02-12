#!/usr/bin/env python3

import sys
from ft_filter import ft_filter


def main():
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
