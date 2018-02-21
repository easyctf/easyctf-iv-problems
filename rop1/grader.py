from io import BytesIO
import string

def get_flag(random):
	return "r0ps_and_h0ps"

def grade(random, key):
	flag = get_flag(random)
	if key.find(flag) >= 0:
		return True, "Correct"
	return False, "Incorrect"