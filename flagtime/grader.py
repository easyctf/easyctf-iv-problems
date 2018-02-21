def grade(autogen, key):
	if key.find("ez_t1m1ng_4ttack!") != -1:
		return True, "Correct"
	return False, "Incorrect"
