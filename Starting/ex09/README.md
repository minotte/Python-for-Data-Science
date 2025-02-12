# 📦 ft_package

**ft_package** is a simple Python package that provides the `count_in_list` function, which counts the occurrences of an element in a list.

---

## Installation

### 1️ Install the package locally

First, make sure **pip** and **setuptools** are up to date:

```sh
pip install --upgrade pip setuptools wheel
```

Then, in the directory containing setup.py, run:
```sh 
python setup.py sdist bdist_wheel
```

This will generate a dist/ folder with .tar.gz and .whl files.

Now, install the package using:

```sh
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```
or
```sh
pip install ./dist/ft_package-0.0.1.tar.gz
```
---
### 2️ Verify the installation
```sh
pip list | grep ft_package
```
```sh
pip show -v ft_package
```
---
## Usage
```sh
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # Output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # Output: 0
```

---

## Package Description
The package includes a single function:


count_in_list(lst, item)

Parameters:

- lst (list) : 
    - lst (list) The list in which to search.
    - item (any) : The element to count.
- Returns:
    - The number of occurrences of item in lst.
