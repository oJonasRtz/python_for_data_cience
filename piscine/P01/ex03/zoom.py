from load_image import ft_load
import matplotlib.pyplot as plt


def zoom_img(array):
    """cut 400x400 and convert to gray scale"""
    if array is None or array.size == 0:
        print("Invalid input: array must be a non-empty NumPy array.")
        return None

    zoom = array[120:520, 450:850]
    gray = zoom[:, :, 0]
    return gray


def main():
    """Load image, zoom it, print data and display it"""
    image = ft_load("animal.jpeg")
    if image.size == 0:
        print("Error loading image.")
        return

    print(image)

    zoomed = zoom_img(image)
    print(f"New shape after slicing: {zoomed.shape}")
    print(zoomed)

    plt.imshow(zoomed, cmap='gray')
    plt.savefig("zoomed_image.png")
    plt.show()


if __name__ == "__main__":
    main()
