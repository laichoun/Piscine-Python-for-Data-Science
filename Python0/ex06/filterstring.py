#!/usr/bin/env python3.10

import sys


def listOfWords(s, n):
    result = []
    result = [item for item in s if (len(item) > n)]
    # for item in s:
    #     if (len(item) > 4):
    #         result.append(item)
    return (result)


def main():
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
