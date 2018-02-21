flag = "w3lc0m3_70_345yc7f"
alphabet = "abcdefghijklmnopqrstuvwxyz"

def get_problem(random):
    n = random.randint(1, 25)
    salt = "".join([random.choice("0123456789abcdef") for i in range(6)])
    return (n, salt)

def generate(random):
	n, salt = get_problem(random)
	trans = str.maketrans(alphabet, alphabet[n:] + alphabet[:n])
	ciphertext = ("easyctf{%s}" % "{}_{}".format(flag, salt)).translate(trans)
	return dict(variables=dict(
		ciphertext=ciphertext
	))

def grade(random, key):
	_, salt = get_problem(random)
	if(key.find("{}_{}".format(flag, salt)) != -1):
		return True, "Great! We hope you enjoy the competition."
	return False, "Try again."
