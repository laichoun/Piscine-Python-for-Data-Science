#!/usr/bin/env python3.10

import sys


def convertToMorse(arg):
    """
    This function takes as arg the string to convert. A dictionnary is created
    with the value in Morse.
    We convert the character in uppercase and we put it in the variable char.
    Then we add the value of the corresponding key to the string s.
    The res variable is the substring s without the space at the end.
    """
    s = ""
    char = ""
    res = ""
    NESTED_MORSE = {" ": "/ ",
                    "A": ".- ",
                    "B": "-... ",
                    "C": "-.-. ",
                    "D": "-.. ",
                    "E": ". ",
                    "F": "..-. ",
                    "G": "--. ",
                    "H": ".... ",
                    "I": ".. ",
                    "J": ".--- ",
                    "K": "-.- ",
                    "L": ".-.. ",
                    "M": "-- ",
                    "N": "-. ",
                    "O": "--- ",
                    "P": ".--. ",
                    "Q": "--.- ",
                    "R": ".-. ",
                    "S": "... ",
                    "T": "- ",
                    "U": "..- ",
                    "V": "...- ",
                    "W": ".-- ",
                    "X": "-..- ",
                    "Y": "-.-- ",
                    "Z": "--.. ",
                    "0": "----- ",
                    "1": ".---- ",
                    "2": "..--- ",
                    "3": "...-- ",
                    "4": "....- ",
                    "5": "..... ",
                    "6": "-.... ",
                    "7": "--... ",
                    "8": "---.. ",
                    "9": "----. ",
                    }
    for x in arg:
        if x.islower():
            char = x.upper()
        else:
            char = x
        s += NESTED_MORSE[char]
    res = s[0: len(s)-1]
    print(res)


def main():
    """
    This function checks for the argv to only have one param after the name
    of the file.
    Then check is each character in the string is alphanum or space and then
    call the function convertToMorse.
    If any issue occurs an error is raised : AssertionError
    """
    try:
        if (len(sys.argv) != 2):
            raise AssertionError
        arg = sys.argv[1]
        for x in arg:
            if (not x.isalnum() and x != ' '):
                raise AssertionError
            # print(x)
        convertToMorse(arg)

    except AssertionError:
        print("AssertionError: the arguments are bad")


if (__name__ == "__main__"):
    main()
