import numpy as np


def checkArg(family: list):
    length = len(family)
    if (length == 0):
        raise ValueError("Family empty")
    length0 = len(family[0])
    if (type(family) is list):
        for item in family:
            if (len(item) != length0):
                raise ValueError("ValueError: Must have the same length")
            for i in item:
                if (type(i) not in (int, float)):
                    raise ValueError("ValueError: Only int or float allowed")
    else:
        raise TypeError("TypeError: not a list")


def slice_me(family: list, start: int, end: int) -> list:
    checkArg(family)
    rows = np.size(family, 0)
    line = np.size(family, 1)
    print(f"My shape is : ({rows}, {line})")

    newShape = slice(start, end)

    if (len(family[newShape]) == 0):
        newShapeRows = 0
        newShapeLine = 0
    else:
        newShapeRows = np.size(family[newShape], 0)
        newShapeLine = np.size(family[newShape], 1)
    print(f"My new shape is : ({newShapeRows}, {newShapeLine})")
    return family[newShape]


def main():
    try:
        family = [[1.80, 78.4],
                  [2.15, 102.7],
                  [2.10, 98.5],
                  [1.88, 75.2]]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))

    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
    try:
        family = [[1.80, 78.4],
                  [2.15, True],
                  [2.10, 98.5],
                  [1.88, 75.2]]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))

    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
    try:
        family = [[1.80, 78.4],
                  [2.15, 87],
                  [2.10, 98.5],
                  [1.88, 75.2]]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 2, -2))

    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)


if (__name__ == "__main__"):
    main()
