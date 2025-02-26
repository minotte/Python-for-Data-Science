# Give my BMI

|||
|:----------------: |:-----------------------------------:|
| **Turn-in directory** | *ex01/* |
| **Files to turn in**| [give_bmi.py](./give_bmi.py) |
| **Allowed functions** | numpy or any lib of table manipulation |


## Description
This project implements two functions:

**give_bmi(height, weight):** Calculates the Body Mass Index (BMI) from a list of heights and weights.

**apply_limit(bmi, limit):** Checks if each BMI value exceeds a given limit.

---
## BMI Formula
BMI is calculated using the following formula:

```BMI = weight / (height²)```
 
where:
- **weight** is in kilograms (kg)  
- **height** is in meters (m)
​
 
where weight is in kilograms and height is in meters.

---

## Installation
No specific installation is required. Just ensure you have Python 3 installed on your machine.

---
## Usage
#### 1️. Run the test file

Use tester.py to execute the tests:
```bash
python tester.py
```

#### 2️.  Example Code
```py
from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))  # [22.50..., 29.03...] <class 'list'>

print(apply_limit(bmi, 26))  # [False, True]
```
## Expected Output
```bash

$> python tester.py
[22.507863455018317, 29.0359168241966] <class 'list'>
[False, True]
```
---
## Error Handling
The height and weight lists must be of the same size.
Values must be numbers (int or float).
An error should be raised if the data is incorrect.
