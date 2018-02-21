def grade(autogen, key):
	if(key.find("y0u_added_thr33_nums!") != -1):
		return True, "Yay it adds correctly!"
	return False, "Try again?"
