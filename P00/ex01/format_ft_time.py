import time
from datetime import datetime

def format_ft_time():
	seconds = time.time()
	
	print(f"Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation")
	date = datetime.now().strftime("%b %d %Y")
	print(date)

if __name__ == "__main__":
	format_ft_time()
