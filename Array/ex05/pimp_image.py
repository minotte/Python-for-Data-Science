import numpy as np
import matplotlib.pyplot as plt
import sys


def show_image(img: np.array, title: str):
    """
    function to show the final image.
    """
    try:
        plt.imshow(img)
        plt.axis("on")
        plt.title(title)
        plt.show()
    except KeyboardInterrupt:
        print("\nInterruption... Bye!")
        sys.exit(1)


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
     Inverts the colors of an RGB image.

    Args:
        array (np.ndarray): Input image as a NumPy array.

    Returns:
        np.ndarray: Image with inverted colors.
    """
    rows, columns, _ = array.shape
    img_invert = array.copy()
    for row in range(rows):
        for column in range(columns):
            red, green, blue = array[row, column]
            img_invert[row, column] = (255 - red, 255 - green, 255 - blue)
    return img_invert


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Show the red layer of an RGB image.

    Args:
        array (np.ndarray): Input image as a NumPy array.

    Returns:
        np.ndarray: Image with just the red color.
    """
    rows, columns, _ = array.shape
    img_red = array.copy()
    for row in range(rows):
        for column in range(columns):
            red, green, blue = array[row, column]
            img_red[row, column] = (red, 0, 0)
    return img_red


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Show the green layer of an RGB image.

    Args:
        array (np.ndarray): Input image as a NumPy array.

    Returns:
        np.ndarray: Image with just the green color.
    """
    rows, columns, _ = array.shape
    img_green = array.copy()
    for row in range(rows):
        for column in range(columns):
            red, green, blue = array[row, column]
            img_green[row, column] = (0, green, 0)
    return img_green


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Show the blue layer of an RGB image.

    Args:
        array (np.ndarray): Input image as a NumPy array.

    Returns:
        np.ndarray: Image with just the blue color.
    """
    rows, columns, _ = array.shape
    img_blue = array.copy()
    for row in range(rows):
        for column in range(columns):
            red, green, blue = array[row, column]
            img_blue[row, column] = (0, 0, blue)
    return img_blue


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
