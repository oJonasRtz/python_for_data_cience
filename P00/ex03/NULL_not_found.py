
def NULL_not_found(object: any) -> int:
	messages = {
		"NoneType": "Nothing: ",
		"float": "Cheese: ",
		"int": "Zero: ",
		"str": "Empty: ",
		"bool": "Fake: ",
	}

	obj_type = type(object)
	value = str(object)
	is_nan = obj_type.__name__ == "float" and object != object
	if (
		(
			object
	 		and
			not is_nan
		)
		or
		obj_type.__name__ not in messages
	):
		print("Type not found")
		return 1

	print(messages[obj_type.__name__] + value + " " + str(obj_type))
	return 0