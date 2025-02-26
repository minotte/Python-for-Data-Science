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
        img.close()
        return img_array

    except Exception as e:
        print(f"Error : {e}")
