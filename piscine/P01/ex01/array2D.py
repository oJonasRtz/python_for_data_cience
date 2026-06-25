import numpy as np


def slice_me(
        family: list,
        start: int, end: int
) -> list:
    """
    Slices a 2D list (list of lists) from the specified start index to
    the end index (exclusive). """
    if (
        not isinstance(family, list) or
        not family or
        not all(isinstance(i, list) for i in family)
    ):
        print("Invalid input: family must be a non-empty list of lists.")
        return []

    # Check same size
    for i in family:
        if len(i) != len(family[0]):
            print("Invalid input: all inner lists must have the same size.")
            return []

    f_slice = family[start:end]

    print(f"my shape is : {np.array(family).shape}")
    print(f"my new shape is : {np.array(f_slice).shape}")

    return f_slice


def main():
    """Tests the slice_me function with a sample 2D list."""
    family = [
        [], []
    ]

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
