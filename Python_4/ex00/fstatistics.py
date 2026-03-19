#!/usr/bin/python3

import statistics

def aff(arg):
    for i in arg:
        print (i)

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
    for i in lst:
        print (i)
    for key, value in kwargs.items():
        if (value == "mean" and len(args) > 0):
            tot = 0
            for val in lst :
                tot += val
            mean = (tot / len(lst))
            print(f"mean : {mean}")
        elif (value == "median" and len(lst) > 0):
            indexMedian = len(lst) // 2
            if (len(lst) % 2 != 0):
                # median = int((len(lst)+ 1)/2)
                print(f"median : {lst[indexMedian]}")
            else:
                median = (lst[indexMedian] + lst[indexMedian -1])/2
                print(f"median : {median}")
        # elif (value == "std" and len(args) > 0):
        #     print(f"std : {pstdev(args)}")
        # elif (value == "var" and len(args) > 0):
        #     print(f"var : {pvariance(args)}")
        elif (value == "quartile" and len(args) > 0):
            print(f"quartile : {statistics.quantiles(args, n=3)}")
            indexMedian = len(lst) // 2
            listQ1 = []
            listQ3 = []
            if (len(lst) % 2 != 0):
                for i in range(0, indexMedian):
                    listQ1.append(lst[i])
                for i in range(indexMedian +1, len(lst)):
                    listQ3.append(lst[i])
                indexQ1 = len(listQ1) // 2
                indexQ3 = len(listQ3) // 2
                print(f"quartile Q1 : {listQ1[indexQ1]}")
                print(f"quartile Q3 : {listQ3[indexQ3 - 1]}")
                if (len(listQ1) % 2 != 0):
                    print(f"quartile Q1 : {listQ1[indexQ1]}")
                else:
                    q1 = (listQ1[indexQ1] + listQ1[indexQ1 -1])/2
                    print(f"quartile Q1 :{q1}")
                if (len(listQ3) % 2 != 0):
                    print(f"quartile Q3 : {listQ3[indexQ3]}")
                else:
                    q3 = (listQ3[indexQ3] + listQ3[indexQ3 -1])/2
                    print(f"quartile Q3 :{q3}")
            else:
                print(lst[indexMedian])
                for i in range(0, indexMedian):
                    print("q1      ", lst[i])
                    listQ1.append(lst[i])
                for i in range(indexMedian, len(lst)):
                    print("q3      ", lst[i])
                    listQ3.append(lst[i])
                indexQ1 = len(listQ1) // 2
                indexQ3 = len(listQ3) // 2
                print("ind q1 : ", listQ1[indexQ1])
                print("ind q3 : ", listQ3[indexQ3])
                if (len(listQ1) % 2 != 0):
                    print(f"quartile Q1 : {listQ1[indexQ1]}")
                else:
                    q1 = (listQ1[indexQ1] + listQ1[indexQ1 -1])/2
                    print(f"quartile Q1 :{q1}")
                if (len(listQ3) % 2 != 0):
                    print(f"quartile Q3 : {listQ3[indexQ3]}")
                else:
                    q3 = (listQ3[indexQ3] + listQ3[indexQ3 -1])/2
                    print(f"quartile Q3 :{q3}")
        elif (len(args) == 0):
            print("ERROR")


def main():
    ft_statistics(1,2,3,4,5,6,7,8,9,10, toto="mean", tutu="median",
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
