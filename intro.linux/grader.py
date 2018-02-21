def grade(_, key):
    if key.find("i_know_how_2_find_hidden_files!") >= 0:
        return True, "Nice job!"
    return False, "Try using ls to find things out."
