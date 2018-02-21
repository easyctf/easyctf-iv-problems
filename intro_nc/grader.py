import string
import random

def generate_key(random):
    return random.randint(0, 2**31 - 1)

def generate_flag(seed):
    r = random.Random()
    r.seed(seed ^ 0x1337)
    s = ''.join(r.choice(string.hexdigits) for i in range(16))
    return 'hello_there!_' + s

def generate(random):
    seed = generate_key(random)
    return dict(variables=dict(seed=seed))

def grade(r, key):
    seed = generate_key(r)
    flag = generate_flag(seed)
    if key.find(flag) >= 0:
        return True, "Correct"
    return False, "Nope"
