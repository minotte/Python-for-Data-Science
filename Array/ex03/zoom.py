from load_image import ft_load
from PIL import Image as img
import numpy as np
import matplotlib.pyplot as plt
import sys


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
        img_array = ft_load("Array/ex02/animal.jpeg")
        if img_array is None:
            raise ValueError("Error: Image could not be loaded.")

        x1, y1, x2, y2 = 450, 100, 850, 500

        print(img_array)
        # Convert numpy.ndarray in Image
        image = img.fromarray(img_array)
        img_crop = zoom(image, x1, y1, x2, y2)
        print(f"New shape after slicing: {img_crop.size}")
        array_crop = np.array(img_crop)
        print(array_crop[0:1, :, 0:1])
        # Matplotlib
        plt.imshow(img_crop)
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
