#!/usr/bin/env python3

import csv
import math
import os
import random
import signal
import sys
import time

ROUNDS = 50
TIMEOUT = 30

os.chdir(os.path.dirname(__file__))

QUESTION_CHOICES = [
    ('land area (m^2)', 'ALAND'),
    ('water area (m^2)', 'AWATER'),
    ('latitude (degrees)', 'INTPTLAT'),
    ('longitude (degrees)', 'INTPTLONG'),
]


def signal_interrupt(signum, frame):
    print("\n\nOh no, you're out of time!")
    exit(1)


def read_data():
    with open('Gaz_zcta_national.txt', newline='') as csvfile:
        lines = [line.rstrip() for line in csvfile.readlines()]
    data = {}
    reader = csv.DictReader(lines,
                            dialect=csv.excel_tab,
                            skipinitialspace=True)
    for row in reader:
        data[row['GEOID']] = row

    return data


def compare_answers(a, b):
    try:
        a, b = float(a), float(b)
    except ValueError:
        return False
    return math.isclose(a, b, rel_tol=1e-3)


def main():
    signal.signal(signal.SIGALRM, signal_interrupt)
    data = read_data()
    zips = list(data.keys())

    print("+======================================================================+")
    print("| Welcome to Zippy! We love US zip codes, so we'll be asking you some  |")
    print("| simple facts about them, based on the 2010 Census. Only the          |")
    print("| brightest zip-code fanatics among you will be able to succeed!       |")
    print("| You'll have {:2d} seconds to answer {:2d} questions correctly.             |"
          .format(TIMEOUT, ROUNDS))
    print("+======================================================================+")
    print()

    time.sleep(1)
    print('3...', end=' ')
    sys.stdout.flush()
    time.sleep(1)
    print('2...', end=' ')
    sys.stdout.flush()
    time.sleep(1)
    print('1...', end=' ')
    sys.stdout.flush()
    time.sleep(1)
    print(' Go!')
    signal.alarm(TIMEOUT)

    for t in range(ROUNDS):
        print("\nRound {:2d} / {:2d}".format(t+1, ROUNDS))
        z = random.choice(zips)
        c = random.choice(QUESTION_CHOICES)

        print("  What is the {} of the zip code {}?"
              .format(c[0], z), end=' ')
        user_str = input()
        ans_str = data[z][c[1]]

        if compare_answers(user_str, ans_str):
            print("\nThat's correct!")
        else:
            print("\nSorry, that's incorrect :(")
            print("The correct answer was {}.".format(ans_str))
            return

    print("\nYou succeeded! Here's the flag:")
    with open('flag.txt') as f:
        print(f.read())


if __name__ == '__main__':
    main()
    sys.stdout.flush()

