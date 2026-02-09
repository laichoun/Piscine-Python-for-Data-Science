#!/usr/bin/python3
import statistics


def ft_statistics(*args: any, **kwargs: any) -> None:
    print("Mean: ", statistics.mean(args))


def main():
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    print("-----")

if (__name__ == "__main__"):
    main()