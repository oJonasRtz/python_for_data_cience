import sys


def counter(string: str) -> dict[str, int]:
    """Counts various types of characters in the input string."""
    if not isinstance(string, str):
        raise AssertionError("Input must be a string.")

    cnt: dict[str, int] = {
        "lowercase": 0,
        "uppercase": 0,
        "digits": 0,
        "punctuation": 0,
        "spaces": 0,
        "total": len(string),
    }

    for char in string:
        cnt["lowercase"] += char.islower()
        cnt["uppercase"] += char.isupper()
        cnt["digits"] += char.isdigit()
        cnt["punctuation"] += char in ".,;:!?\"'()[]{}-"
        cnt["spaces"] += char.isspace()

    return cnt


def take_input(args: list[str]) -> str:
    """
        Takes input from command line arguments \
        or prompts the user if no arguments are provided.
    """
    if not isinstance(args, list):
        raise AssertionError("Input must be a list of strings.")

    assert len(args) <= 1, "Wrong number of arguments."

    try:
        if len(args) == 1:
            return args[0]
        else:
            print("What is the text to count?")
            return sys.stdin.read()
    except EOFError:  # Handle CTRL+D (Unix) or CTRL+Z (Windows) input
        return ""


def print_results(cnt: dict[str, int]) -> None:
    """Prints the results of the character count."""
    if not isinstance(cnt, dict):
        raise AssertionError("Input must be a dictionary.")

    print(f"The text contains {cnt['total']} characters:")
    print(f"{cnt['uppercase']} upper letters")
    print(f"{cnt['lowercase']} lower letters")
    print(f"{cnt['punctuation']} punctuation marks")
    print(f"{cnt['spaces']} spaces")
    print(f"{cnt['digits']} digits")


def main(args: list[str]) -> None:
    """Main function to execute the string analysis."""
    if not isinstance(args, list):
        raise AssertionError("Input must be a list of strings.")

    string = take_input(args)

    cnt = counter(string)
    print_results(cnt)


if __name__ == "__main__":
    try:
        # Printing docstrings for demonstration purposes
        # print(main.__doc__)
        # print(take_input.__doc__)
        # print(counter.__doc__)
        # print(print_results.__doc__)

        # Running the main program with command line arguments
        main(sys.argv[1:])
    except AssertionError as e:
        print(f"AssertionError: {e}")
