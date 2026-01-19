from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker
# import seaborn as sns


def projection_life():
    """
    Docstring for projection_life
    Show the income Gross Domestic Product per
    country in 1900 regarding the Life Expectancy.
    We can see a correlation between those datas
    """
    dfIncome = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    dfExpLife = load("life_expectancy_years.csv")

    dfIncome.columns = dfIncome.columns.astype(int)
    dfExpLife.columns = dfExpLife.columns.astype(int)

    dfIncome1900 = dfIncome[1900]
    dfExpLife1900 = dfExpLife[1900]

    # dfIncome1900 = (
    #     dfIncome1900
    #     .str.replace("k", "e3", regex=False)
    #     .str.replace("M", "e6", regex=False)
    #     .astype(float)
    # )

    print(dfIncome1900, dfExpLife1900)

    newDf = pd.concat([dfIncome1900, dfExpLife1900], axis=1)
    newDf.columns = ["GNP", "Expectancy life"]
    newDf.dropna(inplace=True)
    # subset = newDf[(newDf["GNP"] >= 7000) & (newDf["GNP"] <= 10000)]
    # print("SUB",subset)
    print(newDf.to_string())

    print("corr", newDf.corr())
    # print("duplicated?", newDf.duplicated().to_string())

    newDf.plot(kind='scatter', x='GNP', y='Expectancy life')
    ax = plt.gca()
    ax.set_xlim(100, 10_000)
    ax.xaxis.set_major_locator(ticker.MaxNLocator(4))
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.show()


def main():
    projection_life()


if (__name__ == "__main__"):
    main()
