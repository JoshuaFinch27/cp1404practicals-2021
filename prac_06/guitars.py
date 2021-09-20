"""
Cp1404 prac_06 - Guitar Program - uses Guitar class
"""
from prac_06.guitar import Guitar

PROGRAM_DESCRIPTION = "My guitars!"
CURRENT_YEAR = 2021
GUITAR_TOO_OLD = 1000
MAXIMUM_GUITAR_COST = 3000000  # Most expensive guitar sold for $2,700,000 https://www.gak.co.uk/blog/expensive-guitars/
MINIMUM_GUITAR_COST = 0


def main():
    """Main section of guitars program"""
    guitars = []
    print(PROGRAM_DESCRIPTION)
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        while CURRENT_YEAR < year < GUITAR_TOO_OLD:
            print("Invalid year of construction/purchase.")
            year = int(input("Year: "))
        cost = float(input("Cost: "))
        while MAXIMUM_GUITAR_COST < cost <= MINIMUM_GUITAR_COST:
            print(f"Invalid cost of guitar, must be more than ${MINIMUM_GUITAR_COST} and less than ${MAXIMUM_GUITAR_COST}")
            cost = float(input("Cost: "))
        add_new_guitar = Guitar(name, year, cost)
        guitars.append(add_new_guitar)
        print(f"{add_new_guitar} added.\n")
        name = input("Name: ")


main()
