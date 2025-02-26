#  Zoom on Me  

|||
|:----------------: |:-----------------------------------:|
| **Turn-in directory** | *ex03/* |
| **Files to turn in**| [load_image.py](./load_image.py), [zoom.py](./zoom.py)  |
| **Allowed functions** | Any library for loading, manipulating, and displaying images and arrays. |

## Description
This project involves loading an image, printing relevant details about it, applying a zoom effect, and displaying the result.  

  
Your program must:  
1. **Load the image** `"animal.jpeg"`.  
2. **Print information about the image**, including:  
   - The **size** in pixels (X and Y dimensions).  
   - The **number of channels** (e.g., grayscale or RGB).  
   - The **pixel content** of the image.  
3. **Zoom into a specific region** and print the new shape.  
4. **Display the image with axis scales** after zooming.  
5. Handle errors gracefully with clear messages.  

### Expected Output  
```bash
$ python zoom.py
The shape of image is: (768, 1024, 3)
[[[120 111 132]
  [139 130 151]
  [155 146 167]
  ...
  [120 156  94]
  [119 154  90]
  [118 153  89]]]

New shape after slicing: (400, 400, 1) or (400, 400)
[[[167]
  [180]
  [194]
  ...
  [102]
  [104]
  [103]]]

```
 > Note: The zoomed-in array content may vary based on the selected zoom area.

 ### Error Handling
If an error occurs (e.g., file not found, invalid image format, permission issues), the program must display a clear error message without crashing.

 ## Installation
 Make sure you have Python installed along with the necessary libraries:
```sh
pip install pillow numpy matplotlib
```
## Usage

```sh
python zoom.py
```
## Notion

- Displaying an Image with Matplotlib

## License

[MIT](https://choosealicense.com/licenses/mit/)