from load_csv import load
import matplotlib.pyplot as plt
import sys


def main() -> int:
    """
    main() -> int
    Description:
        the programme will be load a csv "life_expectancy_years.csv",
        extract the data of the country you choose in the variable
        country_search and will show the graphic.
    Variables:
        - `country_search` (str): The country to filter from the dataset
    Returns:
        - `0` if successful.
        - `1` in case of an exception.
        - `130` if interrupted (Ctrl+C).
    """
    try:
        tab_csv = load("../life_expectancy_years.csv")
        # tab_csv.head()
        country_search = "France"
        country_data = tab_csv[tab_csv["country"] == country_search]
        year = country_data.columns[1:]
        life_expectancy = country_data.values[0][1:]

        plt.plot(year, life_expectancy, label=country_search)
        plt.axis("on")
        plt.title(country_search + " Life expectancy Projection")
        plt.ylabel("Life expectancy")
        plt.xlabel("Year")
        plt.xticks(year[::40], rotation=0)
        plt.legend()
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
