"""
CP1404 - Practical
Fixed program to determine score status do-over
"""

import random


def main():
    """Ask user for score and prints the results & repeats with a random score"""
    score = float(input("Enter score: "))
    result = determine_score_result(score)
    print(result)
    random_score = random.randint(0, 101)
    random_result = determine_score_result(random_score)
    print(random_result)


def determine_score_result(score):
    """Determines what result the score gets and returns answer"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
