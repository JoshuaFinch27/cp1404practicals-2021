"""
CP1404 Prac 04 - Quick Pick

Pseudocode of program (not constants)

def main()
    get number_of_picks
    while number_of_picks <= 0
        print error message
        get number_of picks
    for a in range(number_of_picks)
        quick_pick = []
        for b in range(NUMBERS_PER_LINE)
            get random number with randint(MIN, MAX)
            while number in quick_pick
                append number to quick_pick
            sort quick_pick
        print output


main()

"""

import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_LINE = 6


def main():
    """Chooses sets of random numbers & prints them"""
    number_of_picks = int(input("How many quick_picks? "))
    while number_of_picks <= 0:
        print("Need to choose a number above 0.")
        number_of_picks = int(input("How many quick_picks? "))
    for a in range(number_of_picks):
        quick_pick = []
        for b in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
