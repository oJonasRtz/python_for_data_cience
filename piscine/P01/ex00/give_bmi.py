import numpy as np


def give_bmi(
        height: list[int | float],
        weight: list[int | float]
) -> list[int | float]:
    """ It returns a list of BMI values."""
    try:
        # Input Validation
        if (
            not isinstance(height, list)
            or not isinstance(weight, list)
            or len(height) != len(weight)
        ):
            raise Exception()
        for h, w in zip(height, weight):
            if (
                not type(h) in (int, float)
                or not type(w) in (int, float)
                or h <= 0  # Height cannot be zero or negative
                or w <= 0  # Weight cannot be zero or negative
            ):
                raise Exception()

        # Calculate BMI
        return (np.array(weight) / np.array(height) ** 2).tolist()
    except Exception:
        return []


def apply_limit(
        bmi: list[int | float],
        limit: int
) -> list[bool]:
    """ It returns a list of booleans (True if above the limit)."""
    try:
        # Input Validation
        if not isinstance(bmi, list) or not isinstance(limit, int):
            raise Exception()
        for b in bmi:
            if not type(b) in (int, float):
                raise Exception()

        # Apply Limit
        return [b > limit for b in bmi]
    except Exception:
        return []


def main():
    """Tests the give_bmi and apply_limit functions with sample data."""
    height = [2.71, -1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
