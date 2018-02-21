from io import BytesIO
import string
import os

alphabet = string.ascii_lowercase

f = open("words.txt", "r")
words = f.readlines()
f.close()

# len(word) == 11 because we know the flag starts with easyctf{,
# so we can get the first 8 characters of the key
# this narrows the search space to a reasonable amount
keys = [word.strip() for word in words if len(word) == 11]


def get_problem(random):
    word_1 = random.choice(keys)
    word_2 = random.choice(keys)
    key = word_1 + word_2
    flag = "easyctf{" + "flag" * 4 + "".join(random.choice(alphabet) for x in range(50)) + "}"
    return key, flag


def create_problem(random):
    key, flag = get_problem(random)
    enc = ""
    for x in range(len(flag)):
        enc += chr(ord(flag[x]) ^ ord(key[x % len(key)]))
    return BytesIO(enc.encode())


def generate(random):
    return dict(files={
        "keyed_xor.txt": create_problem(random)
    })


def grade(random, key):
    _, flag = get_problem(random)
    if key.find(flag) >= 0:
        return True, "Correct!"
    return False, "Nope."
