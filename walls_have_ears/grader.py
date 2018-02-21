import string
import random

m = 2**31 - 1


def generate_key(random):
    return random.randint(1, m)


def generate_flag(seed):
    r = random.Random()
    r.seed(1337)
    r.seed(seed ^ r.randint(1, m))
    s = "".join(r.choice(string.hexdigits) for i in range(9))
    return "is_anything_safe?_" + s


def generate(random):
    seed = generate_key(random)
    return dict(variables=dict(seed=seed))


def grade(r, key):
    seed = generate_key(r)
    flag = generate_flag(seed)
    if key.find(flag) >= 0:
        return True, "Correct"
    return False, "Nope"
