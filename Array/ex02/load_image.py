import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    ft_load(path: str) -> np.ndarray
    description:
        loads an image, prints its format,
        and displays its pixel content in RGB format.
    Args:
        - the path of an image
    Error:
        - if the path is wrong or the image can be open.
    Return:
        - array of every pixel with RGB
    """
    try:
        img = Image.open(path)
        img_array = np.array(img)
        print(f"The shape of image is: {img_array.shape}")
        ft_grey(img_array)
        return img_array

    except Exception as e:
        print(f"Error : {e}")


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Show the grey layer of an RGB image.

    Args:
        array (np.ndarray): Input image as a NumPy array.

    Returns:
        np.ndarray: Image with just the grey color.
    """
    rows, columns, _ = array.shape
    img_grey = array.copy()
    for row in range(rows):
        for column in range(columns):
            red, green, blue = array[row, column]
            grey = 0.2989 * red + 0.5870 * green + 0.1140 * blue
            img_grey[row, column] = (grey, grey, grey)
    return img_grey