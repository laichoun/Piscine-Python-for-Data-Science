#!/usr/bin/python3

class calculator:
    """
Docstring for calculator
The class is designed to be used without instantiation.
no self, no cls
    """
    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
Add 2 vectors
        """
        x = list(zip(V1, V2))
        newList = [float(first + second) for first, second in x]
        return (newList)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
substract 2 vectors
        """
        x = list(zip(V1, V2))
        newList = [float(first - second) for first, second in x]
        return (newList)

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
Dot Product of 2 vectors
        """
        x = list(zip(V1, V2))
        newList = [first * second for first, second in x]
        tot = 0
        for val in newList:
            tot += val
        return (tot)


def main():
    a = [5, 10, 2]
    b = [2, 4, 3]
    print(calculator.dotproduct(a, b))
    print(calculator.add_vec(a, b))
    print(calculator.sous_vec(a, b))


if (__name__ == "__main__"):
    main()
