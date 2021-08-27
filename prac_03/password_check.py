"""
Password Length Checker Program
"""

MINIMUM_PASSWORD_LENGTH = 10

password = input("Password: ")
while len(password) < MINIMUM_PASSWORD_LENGTH:
    print("Password too short, must be at least 10 characters long")
    password = input("Password: ")
for character in password:
    print("*", end="")
