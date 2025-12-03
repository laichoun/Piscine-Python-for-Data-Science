#!/usr/bin/env python3.10

def ft_filter2(function, iterable):
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
    if (function is None):
        result = [item for item in iterable if item]
    else:
        result = [item for item in iterable if function(item)]
    return (result)


def est_positif(n):
    return n > 0


def main():
    nombres = [-1, 0, 1, 2, -3, 0]
    nombres_positifs = ft_filter(est_positif, nombres)
    print(list(nombres_positifs))  # Sortie: [1, 2]


if __name__ == "__main__":
    main()
