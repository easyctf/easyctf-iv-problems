from io import BytesIO
import string

alphabet = string.ascii_letters
haystack_size = 1000000
with open("20k.txt", "r") as f:
    words = f.readlines()


def get_problem(random):
    index = random.randint(0, haystack_size)
    flag = "".join(random.choice(alphabet) for x in range(25))
    return index, flag


def create_haystack(random):
    # Create a flag
    index, flag = get_problem(random)

    # Create the haystack
    haystack = ""
    while len(haystack) < haystack_size:
        haystack += random.choice(words).strip() + " "

    # Put the flag in the haystack
    haystack = haystack[:index] + "easyctf{" + flag + "}" + haystack[index + 1:]
    return BytesIO(haystack.encode())


def generate(random):
    return dict(files={
        "haystack.txt": create_haystack(random)
    })


def grade(random, key):
    _, flag = get_problem(random)
    if key.find(flag) >= 0:
        return True, "Correct!"
    return False, "Nope."
