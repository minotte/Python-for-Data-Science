from load_csv import load
import matplotlib.pyplot as plt
import sys


def harmonization(population: str) -> float:
    """
    harmonization(population: str) -> float:
    Description:
        This function harmonizes population numbers from the CSV.
        In the dataset, 'M' means millions and 'K' means thousands.
    Return:
        - a float representing the actual population number.
    """
    if population.endswith("M"):
        return float(population[:-1]) * 10**6
    elif population.endswith("K"):
        return float(population[:-1]) * 10**3
    return float(population)


def main() -> int:
    """
    main() -> int
    Description:
        The program loads the CSV file "population_total.csv",
        extracts the population data for two countries, and displays
        the projected population.
    Variables:
        - `country1` (str): First country to compare.
        - `country2` (str): Second country to compare.
    Returns:
        - `0` if successful.
        - `1` in case of an exception.
        - `130` if interrupted (Ctrl+C).
    """
    try:
        tab_csv = load("../population_total.csv")

        country1 = "France"
        country2 = "Belgium"

        ctry1_data = tab_csv[tab_csv["country"] == country1]
        ctry2_data = tab_csv[tab_csv["country"] == country2]

        year = ctry1_data.columns[1:].astype(int)
        population1 = [harmonization(pop) for pop in ctry1_data.values[0][1:]]
        population2 = [harmonization(pop) for pop in ctry2_data.values[0][1:]]

        plt.plot(year, population1, label=country1)
        plt.plot(year, population2, label=country2)
        plt.axis("on")
        plt.title("Population Projections")
        plt.ylabel("Population")
        plt.xlabel("Year")
        plt.xticks(range(1800, 2051, 40))
        plt.yticks([20_000_000, 40_000_000, 60_000_000], ['20M', '40M', '60M'])
        # plt.grid(True)
        plt.legend(loc="lower right")
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
