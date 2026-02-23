#!/usr/bin/python3

def aff(arg):
    for i in arg:
        print (i)

def sort(args):
    arg = list(args)
    for i in range(1, len(arg)):
        print("arg i", arg[i], i)
        poparg = arg.pop(i)
        for j in range(i-1, -1, -1):
            print('pop arg is', poparg)
            print("print arg j", arg[j])
            if (arg[j] > poparg):   
            #     print('pop', poparg)
            #     print("arg j",arg[j], j)
                arg.insert(j, poparg)
            arg.insert(i, poparg)
            aff(arg)
    return (arg)

def ft_statistics(*args: any, **kwargs: any) -> None:
    """
Docstring for ft_statistics

:param *args: Arbitrary arguments : When we do not know the number of
arg in the function.
:param **kwargs: Key arbitrary argument : dictionnary of key value
:type kwargs: any
    """
    lst = sort(args)
    for i in lst:
        print (i)
    # for key, value in kwargs.items():
    #     if (value == "mean" and len(args) > 0):
    #         tot = 0
    #         for val in args :
    #             tot += val
    #         mean = (tot / len(args))
    #         print(f"mean : {mean}")
    #     elif (value == "median" and len(args) > 0):
    #         if (len(args) % 2 != 0):
    #             median = int((len(args) + 1)/2)
    #             print(f"median : {args[median-1]}")
    #     # elif (value == "std" and len(args) > 0):
    #     #     print(f"std : {pstdev(args)}")
    #     # elif (value == "var" and len(args) > 0):
    #     #     print(f"var : {pvariance(args)}")
    #     # elif (value == "quartile" and len(args) > 0):
    #     #     print(f"quartile : {quantiles(args, n= 3)}")
    #     elif (len(args) == 0):
    #         print("ERROR")


def main():
    ft_statistics(1, 42,360,11,64, toto="mean", tutu="median",
                  tata="quartile")
    # print("-----")
    # ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    # print("-----")
    # ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh",
    #               ejdjdejn="kdekem")
    # print("-----")
    # ft_statistics(toto="mean", tutu="median", tata="quartile")


if (__name__ == "__main__"):
    main()
