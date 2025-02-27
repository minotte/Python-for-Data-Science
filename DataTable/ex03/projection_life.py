from load_csv import load
import matplotlib.pyplot as plt
import sys


def main() -> int:
    """
    main() -> int
    Description:
        Loads the data from "income_per_person_gdppercapita_ppp_inflation_
        adjusted.csv" and "life_expectancy_years.csv", then plots life
        expectancy vs GDP per capita for the year 1900.
        The graph displays a scatter plot with a logarithmic x-axis,
        titles, and labels for the axes.

    Variables:
        - year (str): Year for the data to be displayed.
    Returns:
        - `0` if successful.
        - `1` in case of an exception.
        - `130` if interrupted (Ctrl+C).
    """
    try:
        file = "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        csv_income = load(file)
        csv_life = load("../life_expectancy_years.csv")
        year = "1900"
        gdp = csv_income[year]
        life = csv_life[year]

        plt.scatter(gdp, life)
        plt.axis("on")
        plt.title(year)
        plt.ylabel("Life expectancy")
        plt.xlabel("Gross national product")
        plt.xscale("log")  # to convet the scale in log to be more clear
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.show()
        return 0

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nInterruption... Bye!")
        sys.exit(130)


if __name__ == "__main__":
    main()
