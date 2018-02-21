from io import BytesIO
import string

def get_flag(random):
	return 'p3sky_f0rm4t_s7uff'

def grade(random, key):
	flag = get_flag(random)
	if key.find(flag) >= 0:
		return True, "Correct"
	return False, "Incorrect"
