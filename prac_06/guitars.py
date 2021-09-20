"""
Cp1404 prac_06 - Guitar Program - uses Guitar class
"""
from prac_06.guitar import Guitar

PROGRAM_DESCRIPTION = "My guitars!"


def main():
    """Main section of guitars program"""
    guitars = []
    print(PROGRAM_DESCRIPTION)
    name = input("Name: ")
    while name != "":
        year =


def verify_user_input(prompt, data_type):
    """Get and verify user input based on variable parameters"""
    if data_type == "any":
        user_input = input(prompt)
        while user_input == "" or user_input == " ":
            print("Invalid input.")
            user_input = input(prompt)
    else:
        user_input = data_type(input(prompt))


main()
