
def draw_values(*args):
	for arg in args:
		print(arg)
	
def hello():
	#Original objects from the subject
	ft_list = ["Hello", "tata!"]
	ft_tuple = ("Hello", "toto!")
	ft_set = {"Hello", "tutu!"}
	ft_dict = {"Hello" : "titi!"}

	# change the original objects
	ft_list[1] = "World!"
	ft_tuple = ("Hello", "Brazil!")
	ft_set.remove("tutu!")
	ft_set.add("São Paulo!")
	ft_dict["Hello"] = "42SãoPaulo!"

	#print changed objects
	draw_values(ft_list, ft_tuple, ft_set, ft_dict)


if __name__ == "__main__":
	hello()
