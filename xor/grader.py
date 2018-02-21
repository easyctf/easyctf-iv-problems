from io import BytesIO
import string

alphabet = string.ascii_lowercase

def get_problem(random):
    xor_key = random.randint(1, 127)
    flag = "easyctf{" + "".join(random.choice(alphabet) for x in range(25)) + "}"
    return xor_key, flag

def create_problem(random):
    xor_key, flag = get_problem(random)

    print(xor_key, flag)
    
    enc = ""
    for c in flag:
        enc += chr(ord(c) ^ xor_key)
    return BytesIO(enc.encode())

def generate(random):
    return dict(files={
        "xor.txt": create_problem(random)
    })

def grade(random, key):
    xor_key, flag = get_problem(random)
    if key.lower().find(flag.lower()) >= 0:
        return True, "Correct!"
    return False, "Nope."
