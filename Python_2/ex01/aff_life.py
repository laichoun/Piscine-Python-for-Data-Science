from load_csv import load
import matplotlib.pyplot as plt


def affCountryData():
    df = load("life_expectancy_years.csv")
    print(df)
    # transform column country as an index
    df = df.set_index("country")
    print(df.iloc[104])
    print(df.loc["Luxembourg"])
    plt.title("Luxembourg Life expectancy Projections")
    plt.xlabel("Years")
    plt.ylabel("Life expectancy")
    plt.plot(df.loc["Luxembourg"])
    plt.show()


def main():
    affCountryData()


if (__name__ == "__main__"):
    main()
