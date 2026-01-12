from load_csv import load
import matplotlib.pyplot as plt


def affCountryData():
    df = load("life_expectancy_years.csv")
    print(df)
    # transform column country as an index
    # df = df.set_index("country")
    print(df.iloc[104])
    print("the data are : ", df.loc["Luxembourg"])
    dataLux = df.loc["Luxembourg"]
    print("before ", dataLux.index)
    dataLux.index = dataLux.index.astype(int)
    print("ind", df.index)
    print("col ", df.columns)
    plt.title("Luxembourg Life expectancy Projections")
    plt.xlabel("Years")
    plt.ylabel("Life expectancy")
    plt.plot(dataLux)

    ticks = list(range(1800, 2100, 40))
    plt.xticks(ticks)

    plt.show()
    plt.close()


def main():
    affCountryData()


if (__name__ == "__main__"):
    main()
