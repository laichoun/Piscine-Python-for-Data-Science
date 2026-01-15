import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load


def formatage_K_M(x, pos):
    if abs(x) < 1000:   # tolérance flottante
        return "k"
    if (x < 1_000_000):
        return (f"{x/1_000:.0f}k")
    else:
        return (f"{x/1_000_000:.0f}M")


def aff_pop():
    df = load("population_total.csv")
    print(df)
    dataLux = df.loc["Luxembourg"]
    dataBel = df.loc["Belgium"]
    print(dataLux)
    dataLux.index = dataLux.index.astype(int)
    dataBel.index = dataBel.index.astype(int)

    print(dataLux.values)

    print("1800 - 2050", dataLux.loc[1800:2050])
    dfLuxY = dataLux.loc[1800:2050]
    dfBelY = dataBel.loc[1800:2050]

    dfBelY = (
        dfBelY.str.lower()
        .str.replace("k", "e3", regex=False)
        .str.replace("m", "e6", regex=False)
        .astype(float)
    )

    dfLuxY = (
        dfLuxY.str.lower()
        .str.replace("k", "e3", regex=False)
        .str.replace("m", "e6", regex=False)
        .astype(float)
    )
    print("dfLuxY N", dfLuxY)
    print("dfBelY", dfBelY)

    plt.xlabel("Years")
    plt.ylabel("Population")
    plt.title("Population Projections")
    # get current axe
    ax = plt.gca()

    ax.yaxis.set_major_locator(ticker.MaxNLocator(4))
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(formatage_K_M))
    ticks = list(range(1800, 2050, 40))
    plt.xticks(ticks)

    plt.plot(dfLuxY, label="Lux", color='green')
    plt.plot(dfBelY, label="Belgium", color='blue')
    plt.legend(loc='lower right')

    plt.show()


def main():
    aff_pop()


if (__name__ == "__main__"):
    main()
