#!/usr/bin/env python3

import sys
import string


def analyze_text(text: str):
    """this function count every kind of characters"""
    if (len(text) == 0):
        return
    char_count = len(text)
    print(f"The text contains {char_count} characters:")
    upper_count = sum(1 for c in text if c.isupper())
    print(f"{upper_count} upper letters")
    lower_count = sum(1 for c in text if c.islower())
    print(f"{lower_count} lower letters")
    punctuation_count = sum(1 for c in text if c in string.punctuation)
    print(f"{punctuation_count} punctuation marks")
    spaces_cout = sum(1 for c in text if c.isspace())
    print(f"{spaces_cout} spaces")
    digits_cout = sum(1 for c in text if c.isdigit())
    print(f"{digits_cout} digits")


def main():

    """does little parsing"""

    try:
        if (len(sys.argv) > 2):
            raise AssertionError("more than one argument.")
        elif (len(sys.argv) == 1):
            text = input("What is the text to count?\n")
        else:
            text = sys.argv[1]
        print(analyze_text.__doc__)
        analyze_text(text)

    except EOFError:
        print("\nEOFError: Exiting...")
        sys.exit(1)

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)

    except KeyboardInterrupt:
        print("\nInterruption... Bye!")
        sys.exit(1)


if __name__ == "__main__":
    main()
