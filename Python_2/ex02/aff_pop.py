import matplotlib.pyplot as plt
from load_csv import load


def aff_pop():
    df = load("population_total.csv")
    print(df)
    dataLux = df.loc["France"]
    dataBel = df.loc["Belgium"]
    print(dataLux)
    dataLux.index = dataLux.index.astype(int)
    dataBel.index = dataBel.index.astype(int)

    print("1800 - 2050", dataLux.loc[1800:2050])
    dfLuxY = dataLux.loc[1800:2050]
    dfBelY = dataBel.loc[1800:2050]
    print("dfLuxY", dfLuxY)
    print("dfBelY", dfBelY)

    plt.xlabel("Years")
    plt.ylabel("Population")
    plt.title("Population Projections")
    plt.plot(dfLuxY)
    plt.plot(dfBelY)

    plt.yticks()

    plt.show()


def main():
    aff_pop()


if (__name__ == "__main__"):
    main()
