import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image from the specified path and returns it as a NumPy array.
    The image is converted to RGB format before being returned.
    If the path is invalid or the image cannot be loaded,
    an empty array is returned.
    """
    if (
        not isinstance(path, str)
        or not path.strip()
        or not path.lower().endswith(('.jpg', '.jpeg'))
    ):
        print("Invalid input: path must be a  \
              non-empty string ending with .jpg or .jpeg.")
        return np.array([])

    try:
        with Image.open(path) as img:
            img = img.convert("RGB")
            img_array = np.array(img)

            print(f"The shape of image is: {img_array.shape}")
            return img_array
    except FileNotFoundError:
        print(f"File not found: {path}")
        return np.array([])
    except Exception as e:
        print(f"An error occurred while loading the image: {e}")
        return np.array([])


def main():
    """Tests the ft_load function with a sample image file."""
    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()
