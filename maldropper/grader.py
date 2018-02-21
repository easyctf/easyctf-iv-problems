from io import BytesIO
import string

def get_flag(random):
	return "12761716281964844769159211786140015599014519771561198738372"

def grade(random, key):
	flag = get_flag(random)
	if key.find(flag) >= 0:
		return True, "Correct"
	return False, "Incorrect"