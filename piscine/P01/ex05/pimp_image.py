from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def show_image(array, title="Image"):
    """Displays the given image represented as a NumPy array."""
    plt.figure()
    plt.imshow(array)
    plt.title(title)
    plt.savefig(f"{title.lower().replace(' ', '_')}.png")
    plt.show()


def ft_invert(array) -> np.array:
    """Inverts the color of the image received."""
    inverted_array = 255 - array

    show_image(inverted_array, title="Inverted Image")
    return inverted_array


def ft_red(array) -> np.array:
    """
    Creates a red version of the given image represented as a NumPy array.
    """
    red = array * np.array([1, 0, 0])

    show_image(red, title="Red Image")
    return red


def ft_green(array) -> np.array:
    """
    Creates a green version of the given image represented as a NumPy array.
    """
    green = array.copy()
    green[:, :, 0] = green[:, :, 0] - green[:, :, 0]
    green[:, :, 2] = green[:, :, 2] - green[:, :, 2]

    show_image(green, title="Green Image")
    return green


def ft_blue(array) -> np.array:
    """Creates a blue version of the given image represented as a NumPy array.
    """
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0

    show_image(blue, title="Blue Image")
    return blue


def ft_grey(array) -> np.array:
    """Converts the given image represented as a NumPy array to grayscale.
    """
    grey = array.mean(axis=2)

    new = array.copy()
    new[:, :, 0] = grey
    new[:, :, 1] = grey
    new[:, :, 2] = grey

    show_image(new, title="Grey Image")
    return new


def main():
    """tests the image manipulation functions with a sample image file."""
    img = ft_load("landscape.jpg")
    if img.size == 0:
        print("Error loading image.")
        return

    ft_invert(img)
    ft_red(img)
    ft_green(img)
    ft_blue(img)
    ft_grey(img)
    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
