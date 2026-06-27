from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def cut_img(array):
    """cut 400x400 and convert to gray scale"""
    if array is None or array.size == 0:
        print("Invalid input: array must be a non-empty NumPy array.")
        return None

    zoom = array[120:520, 450:850]
    gray = zoom[:, :, 0]
    return gray


def rotate_img(array):
    """Transpose the given 2D NumPy array."""
    if array is None or array.size == 0:
        print("Invalid input: array must be a non-empty NumPy array.")
        return None

    width = len(array[0])
    height = len(array)
    transposed = [[0] * height for _ in range(width)]

    for i in range(height):
        for j in range(width):
            transposed[j][i] = array[i][j]

    return np.array(transposed)


def main():
    """Load image, zoom it, print data and display it"""
    image = ft_load("animal.jpeg")
    if image.size == 0:
        print("Error loading image.")
        return

    print(image)

    gray = cut_img(image)
    if gray is None:
        print("Error cutting image.")
        return
    rotated = rotate_img(gray)
    if rotated is None:
        print("Error rotating image.")
        return

    print(f"New shape after Transpose: {rotated.shape}")
    print(rotated)

    plt.imshow(rotated, cmap='gray')
    plt.savefig("rotated_image.png")
    plt.show()


if __name__ == "__main__":
    main()
