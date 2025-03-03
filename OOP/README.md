# Training Piscine Python for Data Science - 3
## Oriented Object Programming

### Summary
This module introduces Object-Oriented Programming (OOP) concepts in Python, including classes and inheritance. You will apply these principles to solve exercises related to character management and mathematical computations.


## Contents
1. [Specific Instructions](#specific-instructions)
2. [Exercises](#exercises)
   - [Exercise 00: GOT S1E9](#exercise-00-got-s1e9)
   - [Exercise 01: GOT S1E7](#exercise-01-got-s1e7)
   - [Exercise 02: Now it's Weird!](#exercise-02-now-its-weird)
   - [Exercise 03: Calculate My Vector](#exercise-03-calculate-my-vector)
   - [Exercise 04: Calculate My Dot Product](#exercise-04-calculate-my-dot-product)
3. [License](#License)

---


## Specific Instructions

- No global scope code; encapsulate everything in functions.
- Every script must contain a `main()` function:
  ```python
  def main():
      # Your tests and error handling here
  if __name__ == "__main__":
      main()
  ```
- All exceptions must be handled explicitly.
- Every function, class, and method must have a documentation string (`__doc__`).
- Follow the Python style guide (`flake8`).

---

## Exercises

### Exercise 00: GOT S1E9

|||
|:----------------: |:-----------------------------------:|
| **Turn-in directory** | *ex00/* |
| **Files to turn in**| [S1E9.py](ex00/S1E9.py) |
| **Allowed functions** | None |

**Objective:**
- Create an abstract `Character` class with attributes:
  - `first_name` (mandatory)
  - `is_alive` (optional, default is `True`)
- Implement a `die()` method that sets `is_alive` to `False`.
- Create a `Stark` class inheriting from `Character`.

### Exercise 01: GOT S1E7
|||
|:----------------: |:-----------------------------------:|
| **Turn-in directory** | *ex01/* |
| **Files to turn in**| [S1E9.py](ex01/S1E9.py),[S1E7.py](ex01/S1E7.py) |
| **Allowed functions** | None |

**Objective:**
- Implement `Baratheon` and `Lannister` classes inheriting from `Character`.
- Override `__str__` and `__repr__` to return strings instead of object representations.
- Implement a class method `create_lannister()` to create a `Lannister` character dynamically.

### Exercise 02: Now it's Weird!
|||
|:----------------: |:-----------------------------------:|
| **Turn-in directory** | *ex02/* |
| **Files to turn in**| [S1E9.py](ex02/S1E9.py),[S1E7.py](ex02/S1E7.py), [DiamondTrap.py](ex02/DiamondTrap.py) |
| **Allowed functions** | None |
  
**Objective:**
- Implement a `King` class inheriting from both `Baratheon` and `Lannister` (diamond inheritance).

### Exercise 03: Calculate My Vector

|||
|:----------------: |:-----------------------------------:|
| **Turn-in directory** | *ex03/* |
| **Files to turn in**| [ft_calculator.py](ex03/ft_calculator.py) |
| **Allowed functions** | None |

  
**Objective:**
- Create a `Calculator` class that performs:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
- Operations must be performed on vectors with a scalar.

### Exercise 04: Calculate My Dot Product
|||
|:----------------: |:-----------------------------------:|
| **Turn-in directory** | *ex04/* |
| **Files to turn in**| [ft_calculator.py](ex04/ft_calculator.py) |
| **Allowed functions** | None |
 
**Objective:**
- Extend the `Calculator` class to handle:
  - Dot product of two vectors.
  - Vector addition and subtraction.
- Implement decorators to allow calling class methods without instantiation.

---
## License

[MIT](https://choosealicense.com/licenses/mit/)