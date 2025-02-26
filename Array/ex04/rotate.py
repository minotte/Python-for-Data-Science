from load_image import ft_load
from PIL import Image as img
import numpy as np
import matplotlib.pyplot as plt
import sys


# zoom

def zoom(image: img.Image, x1: int, y1: int, x2: int, y2: int) -> img.Image:
    """
    Zoom function that crops an image to a specified area.

    Args:
        image (Image.Image): The image to crop.
        x1, y1 (int): Top-left coordinates of the crop.
        x2, y2 (int): Bottom-right coordinates of the crop.

    Returns:
        Image.Image: The cropped (zoomed) image.
    """
    return image.crop((x1, y1, x2, y2))


# rotate

def rotate(array: np.ndarray) -> np.ndarray:
    """
    Rotate (transpose) an image matrix manually.
    Matrix[i][j] → Matrix[j][i]

    Args:
        array (np.array): 2D image matrix.

    Returns:
        np.array: Transposed image matrix.
    """
    columns = len(array[0])
    lines = len(array)
    new_array = []
    for i in range(columns):
        row = []
        for line in range(lines):
            row.append(array[line][i])
        new_array.append(row)
    return np.array(new_array)


# Show image

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


# main

def main():
    """
    Main function of the program.
    Loads an image, prints its pixel values, and displays a zoomed-in version.
    """
    try:
        img_array = ft_load("Array/ex02/animal.jpeg")
        if img_array is None:
            raise ValueError("Error: Image could not be loaded.")

        x1, y1, x2, y2 = 450, 100, 850, 500

        # Convert numpy.ndarray in Image
        image = img.fromarray(img_array)
        img_crop = zoom(image, x1, y1, x2, y2)
        array_crop = np.array(img_crop)
        print(array_crop[0:1, :, 0:1])
        img_rotate = rotate(array_crop)
        print(f"New shape after Transpose: {img_rotate.size}")
        print(img_rotate)
        show_image(img_rotate, "Rotated Image")

    except ValueError as e:
        print(e)
    except KeyboardInterrupt:
        print("\nInterruption... Bye!")
        sys.exit(1)
    except Exception as e:
        print(f"Error : {e}")


if __name__ == "__main__":
    main()
