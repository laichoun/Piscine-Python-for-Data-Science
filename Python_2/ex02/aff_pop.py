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

    # for i, item in enumerate(dfLuxY):
    #     print(f"Index {i}: {item}")
    #     print("test", dfLuxY.iloc[i])
    #     if ("k" in dfLuxY.iloc[i]):
    #         print("Ok trouvé k")
    #         dfLuxY.iloc[i].replace("k", "").astype(float)
    #         dfLuxY.iloc[i] = dfLuxY.iloc[i] * 1000
    #     elif ("M" in dfLuxY.iloc[i]):
    #         print("Ok trouvé M")
    #         dfLuxY.iloc[i].replace("M", "").astype(float)
    #         dfLuxY.iloc[i] = dfLuxY.iloc[i] * 1000000


    # dfLuxY = dfLuxY.where(
    #     ~dfLuxY.str.contains("k"),
    #     dfLuxY.str.replace("k", "", regex=False).astype(float) * 1_000  
    # )

    dfLuxY = dfLuxY.where(
        ~dfLuxY.str.contains("M"),
        dfLuxY.str.replace("M", "", regex=False).astype(float) * 1_000_000
    )

    dfBelY = dfBelY.where(
        ~dfBelY.str.contains("M"),
        dfBelY.str.replace("M", "", regex=False).astype(float) * 1_000_000
    )

#     dfLuxY = (
#     dfLuxY.str.lower()
#     .str.replace("k", "e3", regex=False)
#     .str.replace("m", "e6", regex=False)
#     .astype(float)
# )
    
#     dfBelY = (
#     dfBelY.str.lower()
#     .str.replace("k", "e3", regex=False)
#     .str.replace("m", "e6", regex=False)
#     .astype(float)
# )


    # dfBelY = dfBelY.str.replace("M", "").astype(float)
    print("dfLuxY N", dfLuxY)
    print("dfBelY", dfBelY)

    plt.xlabel("Years")
    plt.ylabel("Population")
    plt.title("Population Projections")
    # get current axe
    ax = plt.gca()
    ax.yaxis.set_major_locator(ticker.MaxNLocator(4))
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x,
                                                      pos: f"{int(x)}M"))
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
