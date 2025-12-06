
import sys

def returnNumberWithoutSigne(num) :
    s = ""
    i = 0
    while (i < len(num)):
        if (num[i] == "+" or num[i] == "-"):
            i +=1
        s = s + num[i]
        #print(s)
        i +=1
    return (s)

def checkOddEven(arg):
    if (arg.isnumeric()):
        nbr = int(arg)
        #print(nbr)
        if (nbr % 2 == 0):
            print("I'm Even.")
        else:
            print("I'm Odd.")
    else :
        raise AssertionError

try:
    if (len(sys.argv) > 2) :
        raise AssertionError
except AssertionError:
    print("AssertionError: more than one argument is provided") 

try:
    s = ""
    if (len(sys.argv) == 2):
        arg = sys.argv[1]
        if (arg.isnumeric()):
            checkOddEven(arg)
        elif (arg[0] == "+" or arg[0] == "-"):
            s = returnNumberWithoutSigne(arg)
            checkOddEven(s)
        else :
            raise AssertionError
except AssertionError:
    print("AssertionError: argument is not an integer")
