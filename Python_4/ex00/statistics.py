#!/usr/bin/python3

def aff(arg):
    """
Function for the display. Takes as argument the list and prints each value
    """
    for i in arg:
        print(i)


def ft_mean(arg):
    """
Function that gives the mean of a list"""
    tot = 0
    for val in arg:
        tot += val
    mean = (tot / len(arg))
    return (mean)


def ft_stdev(arg, mean):
    """
Function that gives the standard dev of a population
formula : (sum ((xi - mu)^2))/N

xi is each entry
mu is the mean
N is the number of entries
    """
    sum = 0
    for val in arg:
        sum += (val - mean)**2
    stdev = (sum / len(arg))**0.5
    return (stdev)


def sort(args):
    '''
Insertion sort
    '''
    arg = list(args)
    for i in range(1, len(arg)):
        inser_index = i
        # print("arg i", arg[i], i)
        curvalue = arg.pop(i)
        for j in range(i-1, -1, -1):
            # print("print arg j", arg[j], j)
            if (arg[j] > curvalue):
                inser_index = j
                # print("inser index j", j)
        arg.insert(inser_index, curvalue)
        #     aff(arg)
    return (arg)


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
Docstring for ft_statistics

:param *args: Arbitrary arguments : When we do not know the number of
arg in the function.
:param **kwargs: Key arbitrary argument : dictionnary of key value
:type kwargs: any

// is for the floor division (5/2 -> 2.5 5//2 -> 2)
    """
    lst = sort(args)
    for key, value in kwargs.items():
        if (value == "mean" and len(args) > 0):
            mean = ft_mean(lst)
            print(f"mean : {mean}")
        elif (value == "median" and len(lst) > 0):
            indexMedian = len(lst) // 2
            if (len(lst) % 2 != 0):
                print(f"median : {lst[indexMedian]}")
            else:
                median = (lst[indexMedian] + lst[indexMedian - 1])/2
                print(f"median : {median}")
        elif (value == "std" and len(args) > 0):
            mean = ft_mean(lst)
            stdev = ft_stdev(lst, mean)
            print(f"std : {(stdev)}")
        elif (value == "var" and len(args) > 0):
            mean = ft_mean(lst)
            stdev = ft_stdev(lst, mean)
            var = round((stdev ** 2), 7)
            print(f"var : {var}")
        elif (value == "quartile" and len(args) > 0):
            q1 = int((len(lst) - 1 + 1)/4)
            q3 = int(3*(len(lst) - 1 + 1)/4)
            print(f"quartile : [{float(lst[q1])}, {float(lst[q3])}]")
        elif (len(args) == 0):
            print("ERROR")


def main():
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median",
                  tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh",
                  ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if (__name__ == "__main__"):
    main()
