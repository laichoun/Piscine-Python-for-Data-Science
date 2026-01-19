import pandas as pd


def load(path: str):
    """
    Docstring for load

    :param path: type str
    Takes a path and return a dataFrame with the file's data
    """
    try:
        # print(pd.__version__)
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        df = df.set_index("country")
        return (df)

    except FileNotFoundError:
        print(f"FileNotFoundError:[Errno 2] No such file or directory: {path}")
        return (None)


def main():
    print(load("population_total.csv"))


if (__name__ == "__main__"):
    main()
