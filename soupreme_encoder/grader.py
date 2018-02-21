import binascii

flag_prefix = "hexit_mate_"


def get_problem(random):
    flag = flag_prefix + "".join([random.choice("0123456789abcdef") for i in range(20)])
    return flag


def generate(random):
    flag = binascii.hexlify(bytes(get_problem(random), "utf-8")).decode("utf-8")
    return dict(variables=dict(flag=flag))


def grade(random, key):
    flag = get_problem(random)
    if key.find("{}".format(flag)) != -1:
        return True, "Yay you dehexed it!"
    return False, "Wrong encoding?"
