# DataTable

## Summary:
In this training session, you will learn how to load, manipulate, and display a dataset using Python for Data Science applications. By the end of the day, you will have a solid understanding of how to process data tables using libraries like Pandas and visualize them with tools such as Matplotlib

-------------------------
## Table of Contents:

- [Exercise 00: Load Dataset](#Exercise-00:-Load-My-Dataset)
- [Exercise 01: Draw Country Data](#Exercice-01:-Draw-Country-Data)
- [Exercise 02: Compare Country Data](Exercise-02:-Compare-Country-Data)
- [Exercise 03: Draw Data Projections](Exercise-03:-Draw-Data-Projections)

---------
## **Usage**
### **Installation**
Make sure you have the required libraries installed:
```sh
pip install matplotlib pandas
```

## Exercise 00: Load My Dataset

|||  
|:----------------: |:-----------------------------------:|  
| **Turn-in directory** | *ex00/* |  
| **Files to turn in** | [load_csv.py](./ex00/load_csv.py) |  
| **Allowed functions** | Matplotlib, Seaborn, or any library for Data Visualization |

- **Objective**: Write a function to load a dataset from a given path and return its dimensions.

- **Instructions:**

    - Create a function ``load(path: str) -> Dataset`` that loads the dataset from the specified file path, handles errors (e.g., invalid path, incorrect format), and returns the dataset's dimensions.
    - Return ``None`` in case of an error (e.g., invalid file path or format).
    - Display the dataset dimensions.

- Test Script:

```py
from load_csv import load
print(load("life_expectancy_years.csv"))
```

- Expected Output:


```sh
Loading dataset of dimensions (195, 302)
country 1800 1801 1802 1803 ... 2096 2097 2098 2099 2100
Afghanistan 28.2 28.2 28.2 28.2 ... 76.2 76.4 76.5 76.6 76.8
...
```

## Exercise 01: Draw Country Data

|||  
|:----------------: |:-----------------------------------:|  
| **Turn-in directory** | *ex01/* |  
| **Files to turn in** | [load_csv.py](./load_csv.py), [aff_life.py](./ex01/aff_life.py)  |  
| **Allowed functions** | Matplotlib, Seaborn, or any library for Data Visualization |

## 📌 Description
This program loads life expectancy data from a CSV file and plots the **life expectancy projection** of a specific country over time. The graph includes a **title, labeled axes, and a legend**.

### **Program Workflow**
1. **Load the CSV file** (`life_expectancy_years.csv`).
2. **Select a specific country** (e.g., France).
3. **Extract life expectancy data** over the years.
4. **Plot the trend using Matplotlib**.
5. **Format the graph** (axis labels, legend, tick rotations, etc.).

---


### **Running the script**
```sh
python aff_life.py
```
This will generate a graph showing the life expectancy trend for the selected country.

---

## 📊 **Expected Output**
The program generates a **line chart** representing the evolution of life expectancy for a specific country over time.

### **Graph Features:**
- **X-axis:** Years
- **Y-axis:** Life expectancy
- **Legend:** Country name

---
## Exercise 02: Compare My Country

|||  
|:----------------: |:-----------------------------------:|  
| **Turn-in directory** | *ex01/* |  
| **Files to turn in** | [load_csv.py](./load_csv.py), [aff_pop.py](./ex01/aff_pop.py)  |  
| **Allowed functions** | Matplotlib, Seaborn, or any library for Data Visualization |

### Description
This program compares the population data of your campus with another country. It loads the ``population_total.csv`` file, displays the population data from 1800 to 2050, and plots the data for both your campus and a country of your choice. The graph must include a title, legend for each axis, and a legend for each country.

**Program Workflow**
1. Load the population dataset (``population_total.csv``).
2. Select two countries: one for your campus and one for the comparison (e.g., your campus and the USA).
3. Extract population data for both countries from 1800 to 2050.
4. Plot the population comparison using Matplotlib or Seaborn, with the following graph features:
    - Title: "Population Comparison"
    - X-axis: Years (1800 to 2050)
    - Y-axis: Population
    - Legend: Country names*

---
### Running the script
```py
python aff_pop.py
```
---
### Expected Output
The program generates a line chart that shows the population trend for both countries (your campus and the selected country) from 1800 to 2050.

**Graph Features:**
- X-axis: Years (from 1800 to 2050)
- Y-axis: Population
- Legend: The names of the countries being compared

---
## Exercise 03: Draw My Year

|||  
|:----------------: |:-----------------------------------:|  
| **Turn-in directory** | *ex03/* |  
| **Files to turn in** | [load_csv.py](./load_csv.py), [projection_life.py](./ex03/projection_life.py)  |  
| **Allowed functions** | Matplotlib, Seaborn, or any library for Data Visualization |

### Description
This program loads two datasets, **income per person** and **life expectancy** from the years **1900**, and displays a graph comparing life expectancy and gross national product (GDP) for various countries in the year 1900.

**Program Workflow**
1. Load the life expectancy dataset (``life_expectancy_years.csv``) using the load function from Exercise 00.
2. Load the GDP dataset (``income_per_person_gdppercapita_ppp_inflation_adjusted.csv``).
3. Extract the data for the year 1900 for both life expectancy and GDP.
4. Plot the projection of life expectancy in relation to GDP for the year 1900, using Matplotlib or Seaborn, with the following graph features:
    - Title: "Life Expectancy vs. GDP in 1900"
    - X-axis: GDP per capita
    - Y-axis: Life expectancy
    - Legend: Country names

---
### Running the script
```sh
python projection_life.py
```
This will generate a graph displaying the relationship between life expectancy and GDP for the year 1900.
---
### Expected Output
The program generates a scatter plot that displays life expectancy against GDP for various countries in 1900.

**Graph Features:**
- X-axis: GDP per capita (for the year 1900)
- Y-axis: Life expectancy (for the year 1900)
- Legend: Country names