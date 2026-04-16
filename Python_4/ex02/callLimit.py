#!/usr/bin/python3

def callLimit(limit: int):
    """
CallLimit is decorator factory. It returns a decorator and accepts parameters
as arguments.

CallLimiter is the decorator. A decorator is a function that takes as
parameter a function to modify it or add features and return another function.
This permits to modify a function without changing
the code of the function itself
In this case the function returned is a closure

limit_function is a closure :
- it captures variables of the parent function can read it or modify it,
-the function is retured by its parent callLimiter.
The limit_function is defined in another function as a closure it retains the
state of the captured variables across calls
    """
    count = 0

    def callLimiter(function):

        def limit_function(*args, **kwds):
            nonlocal count, limit
            if (count < limit):
                function(*args, **kwds)
            else:
                print("Error: <function ",
                      function.__name__, " at ",
                      hex(id(function)), "call too many time")
            count += 1
        return limit_function

    return callLimiter


@callLimit(3)
def f():
    print("f()")


@callLimit(1)
def g():
    print("g()")


for i in range(3):
    f()
    g()
