# Pimp My Image

|||  
|:----------------: |:-----------------------------------:|  
| **Turn-in directory** | *ex05/* |  
| **Files to turn in**| [load_image.py](./load_image.py), [pimp_image.py](./pimp_image.py)  |  
| **Allowed functions** | Any library for loading, manipulating, and displaying images and arrays. |

## Description

In this exercise, you will implement **five different color filters** for images. Each filter will manipulate the pixel values while maintaining the **original shape** of the image.

Your program must:
1. **Load the image** `landscape.jpg`.
2. **Apply five different filters**:
   - Invert colors
   - Enhance red tones
   - Enhance green tones
   - Enhance blue tones
   - Convert to grayscale
3. **Display the modified images**.
4. **Print the docstrings** of the filter functions.

### Function Prototypes
Each function must adhere to the following signature:
```python
# Inverts the colors of the image
def ft_invert(array) -> array:
    # Your code here

# Enhances the red channel
def ft_red(array) -> array:
    # Your code here

# Enhances the green channel
def ft_green(array) -> array:
    # Your code here

# Enhances the blue channel
def ft_blue(array) -> array:
    # Your code here

# Converts the image to grayscale
def ft_grey(array) -> array:
    # Your code here
```

### Operator Restrictions
Each function can only use the following operators:
- **invert**: `=`, `+`, `-`, `*`
- **red**: `=`, `*`
- **green**: `=`, `-`
- **blue**: `=`
- **grey**: `=`, `/`

---

## Expected Output
```bash
$ python tester.py
The shape of image is: (257, 450, 3)
[[[19 42 83]
  [23 42 84]
  [28 43 84]
  ...
  [ 0 0 0]
  [ 1 1 1]
  [ 1 1 1]]]
...
Inverts the color of the image received.
$>
```

> 📌 **Note:** Your output might vary depending on the image used.

---

## Installation
Make sure you have Python installed along with the necessary libraries:
```sh
pip install pillow numpy matplotlib
```

## Usage
Run the following command to test your functions:
```sh
python tester.py
```

---

## Notion
- Image filtering using NumPy arrays
- Manipulating individual color channels
- Using basic arithmetic operations for transformations

## License
[MIT](https://choosealicense.com/licenses/mit/)

