import numpy as np
import csv


def load(path: str) -> np.ndarry:
    arrList = []
    with open("life_expectancy_years.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            arrList.append(line)
    arr = np.array(arrList)
    # print(arrList)
    print("Loading dataset of dimensions ", arr.shape)
    return (arr)


def main():
    print(load("life_expectancy_years.csv"))


if (__name__ == "__main__"):
    main()
