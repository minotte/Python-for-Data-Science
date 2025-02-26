#  Rotate me  

|||
|:----------------: |:-----------------------------------:|
| **Turn-in directory** | *ex04/* |
| **Files to turn in**| [load_image.py](./load_image.py), [rotate.py](./rotate.py)  |
| **Allowed functions** | Any library for loading, manipulating, and displaying images and arrays. |

## Description
In this exercise, you will create a program that loads the image `"animal.jpeg"`, extracts a **square section** from it, and **transposes** it manually (without using built-in libraries for transposition). The program should then display the transformed image and print its new shape along with the modified pixel data.
 

Your program must:  
1. **Load the image** `"animal.jpeg"`.  
2. **Print information about the image**, including:  
   - The **size** in pixels (X and Y dimensions).  
   - The **number of channels** (e.g., grayscale or RGB).  
   - The **pixel content** of the image.  
3. **Extract a square region** and print its shape.  
4. **Manually transpose the cropped image** (without NumPy’s `.T` or `.transpose()`).  
5. **Display the transposed image**.  
6. Handle errors gracefully with clear messages.

### Expected Output  
```bash
$ python zoom.py
The shape of image is: (768, 1024, 3)
[[[167]
[180]
[194]
...
[102]
[104]
[103]]]


New shape after Transpose: (400, 400)
[[167 180 194 ... 64 50 72]
...
[115 116 119 ... 102 104 103]]

```
 > Note: Your array after the transpose can be different.
You can look for the transpose method, it could help you ...

 ### Error Handling

If an error occurs (e.g., file not found, invalid image format, permission issues), the program must display a clear error message without crashing.

 ## Installation
 Make sure you have Python installed along with the necessary libraries:
```sh
pip install pillow numpy matplotlib
```
## Usage

```sh
python rotate.py
```
## Notion


### Matrix Transposition

- Transposing an image means flipping its rows into columns and vice versa.

*Example of a manual transposition for a 3x3 matrix:*

*Before Transpose:*

```
1  2  3
4  5  6
7  8  9
```

*After Transpose:*

```
1  4  7
2  5  8
3  6  9
```

- Matrix[i][j] → Matrix[j][i] 

## License

[MIT](https://choosealicense.com/licenses/mit/)