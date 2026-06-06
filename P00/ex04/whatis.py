import sys

def is_odd_or_even(num: int) ->str:
	return num & 1 and "Odd" or "Even"

def main(args):
	if (len(args) == 0):
		return

	assert len(args) == 1, "more than one argument is provided"
	try:
		num = int(args[0])
		print(f"I'm {is_odd_or_even(num)}.")
	except ValueError:
		raise AssertionError("argument is not an integer")

if __name__ == "__main__":
	try:
		main(sys.argv[1:])
	except AssertionError as e:
		print(f"AssertionError: {e}")