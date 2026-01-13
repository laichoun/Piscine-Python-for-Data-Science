import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load


def aff_pop():
    df = load("population_total.csv")
    print(df)
    dataLux = df.loc["France"]
    dataBel = df.loc["Belgium"]
    print(dataLux)
    dataLux.index = dataLux.index.astype(int)
    dataBel.index = dataBel.index.astype(int)

    print(dataLux.values)

    print("1800 - 2050", dataLux.loc[1800:2050])
    dfLuxY = dataLux.loc[1800:2050]
    dfBelY = dataBel.loc[1800:2050]

    dfLuxY = dfLuxY.str.replace("M", "").astype(float)
    dfBelY = dfBelY.str.replace("M", "").astype(float)
    print("dfLuxY", dfLuxY)
    print("dfBelY", dfBelY)

    plt.xlabel("Years")
    plt.ylabel("Population")
    plt.title("Population Projections")
    plt.plot(dfLuxY, label="Lux")
    
    plt.plot(dfBelY, label="Belgium")
    plt.legend()

    #get current axe
    ax = plt.gca()
    ax.yaxis.set_major_locator(ticker.MaxNLocator(4))
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f"{int(x)}M"))
    
    ticks = list(range(1800, 2050, 40))
    plt.xticks(ticks)
    plt.show()


def main():
    aff_pop()


if (__name__ == "__main__"):
    main()
