def grade(autogen, key):
    if "congrats!_but_now_f0r_n0s0urc3_..." in key:
        return True, "Correct!"
    elif "}yngrcne EacrBxz" in key:
        return False, "You're almost there. But try looking a bit more closely..."
    elif "Fg4GCRoHCQ4TFh0IBxENA" in key:
        return False, "You're getting there, but not quite. What is the string that you entered used for?"
    return False, "Nope! Have you tried viewing the source?"
