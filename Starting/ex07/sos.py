#!/usr/bin/env python3

import sys


NESTED_MORSE = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
        "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-",
        "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-",
        "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "0": "-----",
        "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
        "6": "-....", "7": "--...", "8": "---..", "9": "----.", " ": "/"
    }


def convert_morse(txt: str) -> str:
    """
    convert_morse(txt:str) -> str:

    Convert a given text into Morse code.
    Args:
        txt (str): The input string to be converted into Morse code.

    Returns:
        str: The Morse code representation of the input text.

    Raises:
        AssertionError: If the input contains characters not present
        in NESTED_MORSE.

    Example:
        >>> convert_morse("SOS")
        '... --- ...'
    """
    try:
        txt = txt.upper()
        if any(char not in NESTED_MORSE for char in txt):
            raise AssertionError("AssertionError: the arguments are bad")
        morse = " ".join(NESTED_MORSE[char] for char in txt)
        return morse

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError(": the arguments are bad")
        morse = convert_morse(sys.argv[1])
        print(morse)

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)

    except KeyboardInterrupt:
        print("\nInterruption... Bye!")
        sys.exit(1)


if __name__ == "__main__":
    main()
