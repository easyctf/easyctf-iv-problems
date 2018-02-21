from io import BytesIO
import string

def get_flag(random):
	return "h34p_expl01ts_ru1n1ng_my_f4nf1cs"

def grade(random, key):
	flag = get_flag(random)
	if key.find(flag) >= 0:
		return True, "Correct"
	return False, "Incorrect"
