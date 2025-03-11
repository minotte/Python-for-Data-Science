#!/usr/bin/env python3

import sys


def analyze_text(text: str):
    """
    this function count every kind of characters.
    arg:
        string
    return:
        nothing
    """

    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    char_count = len(text)
    print(f"\nThe text contains {char_count} characters:")
    upper_count = sum(1 for c in text if c.isupper())
    print(f"{upper_count} upper letters")
    lower_count = sum(1 for c in text if c.islower())
    print(f"{lower_count} lower letters")
    punctuation_count = sum(1 for c in text if c in punctuation)
    print(f"{punctuation_count} punctuation marks")
    spaces_cout = sum(1 for c in text if c.isspace())
    print(f"{spaces_cout} spaces")
    digits_cout = sum(1 for c in text if c.isdigit())
    print(f"{digits_cout} digits")


def main():

    """
    main function and does little parsing
    Args:
        - text
        - if not argument the user can write text.
    Error:
        - more than one argument
    """

    try:
        assert len(sys.argv) <= 2, "more than one argument."
        if (len(sys.argv) == 1):
            print("What is the text to count?\n")
            text = sys.stdin.readline()
        else:
            text = sys.argv[1]
        # print(analyze_text.__doc__)
        analyze_text(text)

    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        sys.exit(1)

    except KeyboardInterrupt:
        print("\nInterruption... Bye!")
        sys.exit(1)


if __name__ == "__main__":
    main()
