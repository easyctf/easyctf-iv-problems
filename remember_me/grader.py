def grade(autogen, key):
	if key.lower().find("4ud10_st3g") != -1:
		return True, "Correct"
	return False, "Incorrect"
