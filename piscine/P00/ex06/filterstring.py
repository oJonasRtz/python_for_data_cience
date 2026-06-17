import sys
import ft_filter


def test_doc():
    """Prints the docstrings of the original filter
 function and the ft_filter function."""
    print("\tORIGINAL FUNCTION:\n")
    print(filter.__doc__)

    print("\tMY FUNCTION:\n")
    print(ft_filter.ft_filter.__doc__)


def is_valid(args):
    """Checks if the args are: string number"""
    if (
        len(args) != 2
        or not args[0]
        or not args[1]
    ):
        return False

    try:
        int(args[1])
        return True
    except ValueError:
        return False


def main(args):
    """Main function to demonstrate the ft_filter function."""
    # test_doc()

    if not is_valid(args):
        raise AssertionError("the arguments are bad")

    s = args[0].split(" ")
    n = int(args[1])
    result = ft_filter.ft_filter(lambda x: len(x) > n, s)
    print(result)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except AssertionError as e:
        print(f"AssertionError: {e}")
