import pandas as pd


def load(path: str):
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return (df.to_string(index=False))

    except FileNotFoundError:
        print(f"FileNotFoundError:[Errno 2] No such file or directory: {path}")
    except UnicodeDecodeError:
        print("UnicodeDecodeError: 'utf-8' codec can't decode"
              "byte 0xff in position 0: invalid start byte")

        return (None)


def main():

    print(load("life_expectancy_years.csv"))


if (__name__ == "__main__"):
    main()
