def grade(autogen, key):
	if(key.find("betcha_wish_you_could_have_used_ANY") != -1):
		return True, "Nice digging!"
	return False, "Try again."
