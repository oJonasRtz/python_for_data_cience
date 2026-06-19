import numpy as np


def slice_me(
		family: list,
		start: int, end: int
) -> list:
	f_slice = family[start:end]

	print(f"my shape is {np.array(family).shape}")
	print(f"my new shape is {np.array(f_slice).shape}")

	return f_slice


if __name__ == "__main__":
	family = [
		[1.80, 78.4],
		[2.15, 102.7],
		[2.10, 98.5],
		[1.88, 75.2]
	]
	
	print(slice_me(family, 0, 2))
	print(slice_me(family, 1, -2))
