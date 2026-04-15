#!/usr/bin/python3

def square(x):
    if (isinstance(x, int) or isinstance(x, float)):
        sqrt = x ** 2
        return (sqrt)
    else:
        raise TypeError("Type error: Only float or int accepted")


def pow(x):
    if (isinstance(x, int) or isinstance(x, float)):
        pow = x ** x
        return (pow)
    else:
        raise TypeError("Type error: Only float or int accepted")


def outer(x, function):
    """
A closure is a function that captures variables from its outer scope
and can continue to use them even after the outer function has
finished executing.
nonlocal is used to modify the enclosing scope inside an inner function
    """
    count = 0
    def inner():
        nonlocal count, x
        # print(count)
        x = function(x)
        count +=1
        return (x)
    return inner


def main():
    print("hello")
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if (__name__ == "__main__"):
    main()
