#!/usr/bin/env python3.10

import sys


def listOfWords(s, n):
    """
    This function is not used it was only pedagogical
    This function takes 2 arg : the string and the length to compare to.
    It returns a list filtered with words that have a length higher than
    the n put as argument
    """
    result = []
    result = [item for item in s if (len(item) > n)]
    # for item in s:
    #     if (len(item) > 4):
    #         result.append(item)
    return (result)


def main():
    """
    This function checks the number of arguments put.
    Thanks to a List Comprehension I can easily filter what is needed.
    The lambda function is an anonymous function
    """
    try:
        if (len(sys.argv) != 3):
            raise AssertionError
        else:
            s = sys.argv[1]
            n = sys.argv[2]
            res = []
            # mylist = []
            print(f"string : {s} and number : {n}")
            try:
                nbr = int(n)
            except ValueError:
                raise AssertionError(("the arguments are bad"))
            res = s.split()
            # mylist = lambda res, nbr: [it for it in res if (len(it) > nbr)]
            # print(mylist(res, nbr))
            print((lambda res, nbr: [it for it in res if (len(it) > nbr)])
                  (res, nbr))

    except AssertionError:
        print("AssertionError: the arguments are bad")


if (__name__ == "__main__"):
    main()
