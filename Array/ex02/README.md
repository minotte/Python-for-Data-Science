# Load image

|||
|:----------------: |:-----------------------------------:|
| **Turn-in directory** | *ex01/* |
| **Files to turn in**| [load_image.py](./load_image.py) |
| **Allowed functions** | all libs for load images and table manipulation |


## Description
In this exercise, you need to write a function that **loads an image**, prints its format, and displays its pixel content in **RGB format**.  
Your function should support at least **JPG and JPEG** formats and handle any errors gracefully by displaying a clear error message.  
#### Function Prototype
```py
def ft_load(path: str) -> array: (you can return to the desired format)
```
### test.py
```py
from load_image import ft_load

print(ft_load("landscape.jpg"))
```
### Expected Output
If landscape.jpg is a valid image, running tester.py should produce:
```sh
$> python tester.py
The shape of image is: (257, 450, 3)
[[[19 42 83]
  [23 42 84]
  [28 43 84]
  ...
  [ 0 0 0]
  [ 1 1 1]
  [ 1 1 1]]]
```

- The shape represents:
    - 257 pixels in height
    - 450 pixels in width
    - 3 channels for RGB values

---------------
>  Error Handling
Your function should handle errors properly. Example cases:

- File not found → "Error: File not found"
- Unsupported format → "Error: Unsupported image format"
- Invalid image → "Error: Could not load image"



## Installation
Make sure you have Python installed along with the necessary libraries:
```sh
pip install pillow NumPy
```
## Usage

```sh
python test.py lanscape.jpg
```

## Notion

New library:

```python
# Used for working with images:
from PIL.Image import Image
```

To retrieve the values of the ***Red (R) channel***, ***Green (G) channel***, and ***Blue (B) channel*** of the pixel at coordinates (100, 250).

- Convention:
  - **r** red channel.
  - **g** green channel.
  - **b** blue channel.

Exemple:

```python
# Get the value of a pixel at (x, y):
img.getpixel((190, 250))
print("Red channel:", r, "Green channel:", g, "Blue channel:", b)
```
```ndarray```: n-dimensional array

-------------------------------
```
The shape of image is: (257, 450, 3)
```
in this exemple 
 - 257: nb of line
 - 450: nb of column
 - 3: channels(rgb) if we don't have it, the image is black and white
## License

[MIT](https://choosealicense.com/licenses/mit/)