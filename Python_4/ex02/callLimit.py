#!/usr/bin/python3


def callLimit(limit: int): 
    count = 0
    def callLimiter(function):
        def limit_function(*args, **kwds):
            nonlocal count, limit
            if (count < limit):
                function(*args, **kwds)
            else:
                print("Error: <function ",  function.__name__, " at ", hex(id(function)),"call too many time")
            count +=1
        return limit_function

    return callLimiter


@callLimit(3)
def f():
    print ("f()")
@callLimit(1)
def g():
    print ("g()")

for i in range(3): 
    f()
    g()
