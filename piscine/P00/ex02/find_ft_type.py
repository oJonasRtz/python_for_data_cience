
def all_thing_is_obj(object: any) -> int:
	messages = {
		"list": "List : ",
		"tuple": "Tuple : ",
		"set": "Set : ",
		"dict": "Dict : ",
		"str": f"{str(object)} is in the kitchen : ",
	}
	
	obj_type = type(object)
	if obj_type.__name__ not in messages:
		print("Type not found")
		return 42
	
	print(messages[obj_type.__name__] + str(obj_type))
	return 42
