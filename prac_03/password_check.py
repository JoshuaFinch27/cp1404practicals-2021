"""
Password Length Checker Program (modified)
"""

MINIMUM_PASSWORD_LENGTH = 10


def main():
    """Checks password"""
    password = get_password()
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Password too short, must be at least 10 characters long")
        password = get_password()
    print_number_of_asterisks(password)


def print_number_of_asterisks(password):
    """Prints an asterisk for each character in the password"""
    for _ in password:
        print("*", end="")


def get_password():
    """Gets password from user"""
    password = input("Password: ")
    return password


main()
