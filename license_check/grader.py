from io import BytesIO
import string


def grade(random, key):
	try:
		if (len(key) != 16):
			return False, "Invalid length, only submit the license key."
		email_key = 0x0aed12f1
		final_xor = 0x0aecbcc2
		hsh = 0
		for i in range(0, 4):
			n = int(key[(i*4):((i+1)*4)], 30)
			if (n == 0):
				return False, "Bad key value"
			hsh ^= n
		if ((final_xor ^ email_key ^ hsh) == 0):
			return True, "Correct"
		return False, "Key was incorrect"
	except:
		return False, "Invalid Key"
