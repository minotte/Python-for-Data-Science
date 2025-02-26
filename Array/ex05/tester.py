from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey
from pimp_image import show_image


def main() -> int:
    """
    main function
    """
    try:
        img_array = ft_load("./landscape.jpg")
        print(img_array)
        show_image(img_array, "orginal")

        img_invert = ft_invert(img_array)
        show_image(img_invert, "invert")

        img_red = ft_red(img_array)
        show_image(img_red, "red layer")
        img_green = ft_green(img_array)
        show_image(img_green, "green layer")
        img_blue = ft_blue(img_array)
        show_image(img_blue, "blue layer")
        img_grey = ft_grey(img_array)
        show_image(img_grey, "image in grey")

        print(ft_invert.__doc__)

    except Exception as e:
        print(f"Error : {e}")


if __name__ == "__main__":
    main()
