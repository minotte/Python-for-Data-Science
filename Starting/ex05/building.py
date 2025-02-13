#!/usr/bin/env python3

import sys
import string


def analyze_text(text: str):
    """
    this function count every kind of characters.
    arg:
        string
    return:
        nothing
    """

    char_count = len(text)
    print(f"\nThe text contains {char_count} characters:")
    upper_count = sum(1 for c in text if c.isupper())
    print(f"{upper_count} upper letters")
    lower_count = sum(1 for c in text if c.islower())
    print(f"{lower_count} lower letters")
    punctuation_count = sum(1 for c in text if c in string.punctuation)
    print(f"{punctuation_count} punctuation marks")
    spaces_cout = sum(1 for c in text if c.isspace())
    spaces_cout = sum(1 for c in text if c == '\n')
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
        if (len(sys.argv) > 2):
            raise AssertionError("more than one argument.")
        elif (len(sys.argv) == 1):
            print("What is the text to count?\n")
            text = sys.stdin.readline()
        else:
            text = sys.argv[1]
        # print(analyze_text.__doc__)
        analyze_text(text)

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)

    except KeyboardInterrupt:
        print("\nInterruption... Bye!")
        sys.exit(1)


if __name__ == "__main__":
    main()
