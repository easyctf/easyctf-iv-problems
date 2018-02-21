def grade(autogen, key):
	if key.upper().find("THIS_IS_AN_EASY_FLAG_TO_GUESS") != -1:
		return True, "Correct!"
	return False, "You can't  guess!"
