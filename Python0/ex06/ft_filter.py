#!/usr/bin/env python3.10

def ft_filter2(function, iterable):
    """
    This function is without List Comprehension
    It takes 2 arguments : the function and the iterable
    It iterates over the iterable and applies the function to
    each element.
    If the function is None then it returns the value truthy
    """
    result = []
    for item in iterable:
        if (function is None):
            if (item):
                result.append(item)
        else:
            if (function(item) is True):
                result.append(item)
    return (result)


def ft_filter(function, iterable):
    """
    This function is with List Comprehension
    It takes 2 arguments : the function and the iterable
    It iterates over the iterable and applies the function to
    each element.
    If the function is None then it returns the value truthy
    """
    if (function is None):
        result = [item for item in iterable if item]
    else:
        result = [item for item in iterable if function(item)]
    return (result)


def est_positif(n):
    """
    This function takes a number as arguments and returns
    if it's a positive number or not
    """
    return n > 0


def main():
    """
    Call the function filter
    """
    nombres = [-1, 0, 1, 2, -3, 0]
    nombres_positifs = ft_filter(est_positif, nombres)
    print(list(nombres_positifs))  # Sortie: [1, 2]


if __name__ == "__main__":
    main()
