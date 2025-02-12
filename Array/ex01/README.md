# Array 2D Slicing
## Description
This project implements a function that takes a 2D array as input, prints its shape, and returns a truncated version of the array based on the provided start and end arguments using slicing.

## Usage
Function Prototype

```py 
def slice_me(family: list, start: int, end: int) -> list:
```

### Parameters
- ``family`` (list[list[float]]): A 2D list containing numerical values.
- ``start`` (int): The starting index for slicing.
- ``end`` (int): The ending index for slicing.
### Return Value
- A new 2D list containing the selected rows based on the slicing range.
## Constraints
- The input family must be a 2D list.
- The rows in family must have the same number of elements.
- If start or end is out of range, the function should handle it gracefully.
## Example
### Input (tester.py)
```py
from array2D import slice_me

family = [
    [1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]
]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
```
### Expected Output
```sh
My shape is : (4, 2)
My new shape is : (2, 2)
[[1.8, 78.4], [2.15, 102.7]]

My shape is : (4, 2)
My new shape is : (1, 2)
[[2.15, 102.7]]
```
