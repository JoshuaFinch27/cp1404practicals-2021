"""
CP1404 prac_06 - Testing Guitar class
"""

from prac_06.guitar import Guitar


def test_guitar_class():
    """Tests the guitar class"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    first_guitar = Guitar(name, year, cost)
    second_guitar = Guitar("Another guitar", 2013, 22748.60)
    print_guitar_age(first_guitar, 98)
    print_guitar_age(second_guitar, 7)
    print_guitar_vintage_status(first_guitar, True)
    print_guitar_vintage_status(second_guitar, False)


def print_guitar_age(guitar, expected_age):
    """Prints the name, expected age and actual age of a guitar"""
    print(f"{guitar.name} get_age() - Expected {expected_age}. Got {guitar.get_age()}.")


def print_guitar_vintage_status(guitar, expected_boolean):
    """Prints the name, expected value and actual value of if the guitar is vintage or not"""
    print(f"{guitar.name} is_vintage() - Expected {expected_boolean}. Got {guitar.is_vintage()}.")


test_guitar_class()
