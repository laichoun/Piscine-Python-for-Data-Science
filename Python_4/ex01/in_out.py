#!/usr/bin/python3

def outer(x: int | float, function) -> object:
    count = 10
    def inner() -> float:
        print("print the ", function(x))
        print (function.__name__)
        return (function(x))
    return (inner)


def square(x: int | float) -> int | float:
    if (isinstance(x, int) or isinstance(x, float)):
        sqrt = x ** 2
        return (sqrt)
    # else:
    #    raise TypeError("Type error: Only float or int accepted")


def pow(x: int | float) -> int | float:
    if (isinstance(x, int) or isinstance(x, float)):
        pow = x ** x
        return (pow)
    else:
        raise TypeError("Type error: Only float or int accepted")




def main():
    print("hello")
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())


if (__name__ == "__main__"):
    main()
