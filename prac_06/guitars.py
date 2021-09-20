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
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        add_new_guitar = Guitar(name, year, cost)
        guitars.append(add_new_guitar)
        print(Guitar.__str__(add_new_guitar), "added.")
        name = input("Name: ")
    # Test data
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:     # empty = False, not-empty = True
        guitars.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("Why are you using this program if you don't have any guitars?")


main()
