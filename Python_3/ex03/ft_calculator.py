#!/usr/bin/python3

class calculator:
    """
Do the overloading operators + - * /
    """
    def __init__(self, val):
        self.value = val

    def __add__(self, object) -> None:
        myList = [x + object for x in self.value]
        return calculator(myList)

    def __mul__(self, object) -> None:
        myList = [x * object for x in self.value]
        return calculator(myList)

    def __sub__(self, object) -> None:
        myList = [x - object for x in self.value]
        return calculator(myList)

    def __truediv__(self, object) -> None:
        if (object == 0):
            raise ValueError("Not possible to divide with 0")
        else:
            myList = [x / object for x in self.value]
            return calculator(myList)

    def __repr__(self):
        return (f"{self.value}")


def main():
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    print(v1 + 5)
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    try:
        v3 / 5
        v3/0
    except ValueError as e:
        print(e)


if (__name__ == "__main__"):
    main()
