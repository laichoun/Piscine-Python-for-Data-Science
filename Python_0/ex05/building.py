#!/usr/bin/env python3.10

import sys


def calculationSumChar(arg):
    """
    This function calculates the sum of upper-case characters,
    lower-case characters, punctuation characters, digits
    and spaces in a string.

    It takes one parameter : the string and returns a dictionnary
    """
    count = {
        "countLowerCase": 0,
        "countUpCase": 0,
        "countSpace": 0,
        "countDigit": 0,
        "countPunctuation": 0
    }
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for i in arg:
        if (i.islower()):
            count["countLowerCase"] += 1
        elif (i.isupper()):
            count["countUpCase"] += 1
        elif (i.isspace()):
            count["countSpace"] += 1
        elif (i.isdigit()):
            count["countDigit"] += 1
        elif (i in punctuation_chars):
            count["countPunctuation"] += 1
    return (count)


def printMessage(dicCount, arg):
    """
    This function prints the messages of the couters in the disCount

    The disCount parameter is a dictionnary where there is:
        "countLowerCase",
        "countUpCase",
        "countSpace",
        "countDigit",
        "countPunctuation".

    The parameter "arg" is the string put as argument (argv[1])
    """
    print(f"The text contains {len(arg)} characters:")
    print(f"{dicCount['countUpCase']} upper letters")
    print(f"{dicCount['countLowerCase']} lower letters")
    print(f"{dicCount['countPunctuation']} punctuation marks")
    print(f"{dicCount['countSpace']} spaces")
    print(f"{dicCount['countDigit']} digits")


def main():
    try:
        dicCount = {}

        if (len(sys.argv) > 2):
            raise AssertionError
        elif (len(sys.argv) == 2):
            arg = sys.argv[1]
            dicCount = calculationSumChar(arg)
            printMessage(dicCount, arg)
        else:
            # arg = input ("What is the text to count?\n") + " "
            print("What is the text to count?")
            arg = sys.stdin.read()
            if (arg == ""):
                pass
            else:
                arg.replace('\n', ' ')
            dicCount = calculationSumChar(arg)
            printMessage(dicCount, arg)

    except AssertionError:
        print("AssertionError: more than one argument is provided")


if (__name__ == "__main__"):
    main()


# def sumLowerCaseChar(arg) -> int:
#     count = 0
#     for i in arg:
#         if (i.islower()):
#             count += 1
#     return (count)


# def sumUpCaseChar(arg) -> int:
#     count = 0
#     for i in arg:
#         if (i.isupper()):
#             count += 1
#     return (count)


# def sumSpaceChar(arg) -> int:
#     count = 0
#     for i in arg:
#         if (i.isspace()):
#             count += 1
#     return (count)


# def sumDigit(arg) -> int:
#     count = 0
#     for i in arg:
#         if (i.isdigit()):
#             count += 1
#     return (count)


# def sumPunctuationMark(arg) -> int:
#     count = 0
#     punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
#     for i in arg:
#         if (i in punctuation_chars):
#             count += 1
#     return (count)
