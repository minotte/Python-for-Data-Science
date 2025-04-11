from load_image import ft_load
from PIL import Image as img
import numpy as np
import matplotlib.pyplot as plt
import sys


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Show the grey layer of an RGB image.

    Args:
        array (np.ndarray): Input image as a NumPy array.

    Returns:
        np.ndarray: Image with just the grey color.
    """
    rows, columns, _ = array.shape
    img_grey = np.zeros((rows, columns, 1), dtype=np.uint8)
    for row in range(rows):
        for column in range(columns):
            red, green, blue = array[row, column]
            grey = 0.2989 * red + 0.5870 * green + 0.1140 * blue
            img_grey[row, column] = (grey)
    return img_grey


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


def main():
    """
    Main function of the program.
    Loads an image, prints its pixel values, and displays a zoomed-in version.
    """
    try:
        img_array = ft_load("animal.jpeg")
        if img_array is None:
            raise ValueError("Error: Image could not be loaded.")

        x1, y1, x2, y2 = 450, 100, 850, 500

        print(img_array[0:1])
        # Convert numpy.ndarray in Imagex
        image = img.fromarray(img_array)
        img_crop = zoom(image, x1, y1, x2, y2)
        img_crop_array = np.array(img_crop)

        img_grey = ft_grey(img_crop_array)
        # img_grey = np.expand_dims(img_grey, axis=-1)
        print(f"New shape after slicing: {img_grey.shape}")
        print(img_grey[0:1])

        # Matplotlib
        plt.imshow(img_grey, cmap="gray")
        plt.axis("on")
        plt.title("Zoomed image")
        plt.show()
    except ValueError as e:
        print(e)
    except KeyboardInterrupt:
        print("\nInterruption... Bye!")
        sys.exit(1)
    except Exception as e:
        print(f"Error : {e}")


if __name__ == "__main__":
    main()
