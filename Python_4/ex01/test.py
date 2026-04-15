def fac(n):
    if (n == 1 or n == 0):
        return (1)
    else :
        print("the fac is : ",n, n-1)
        return (fac(n-1) * n)


def main():
    print (fac(4))

main()

# https://github.com/semx2a/piscine-python/tree/main/py04/ex00