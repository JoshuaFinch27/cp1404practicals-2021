"""
CP1404 - Practical
Fixed program to determine score status
"""

score = float(input("Enter score: "))
while score != -1:
    if score > 100 or score < 0:
        print("Invalid score")
    elif score > 90:
        print("Excellent")
    elif score > 50:
        print("Passable")
    else:
        print("Bad")
    score = float(input("Enter score: "))
