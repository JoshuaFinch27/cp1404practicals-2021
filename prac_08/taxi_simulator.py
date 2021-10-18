"""
CP1404 Practical - Taxi (Task) Simulator using Taxi and SilverServiceTaxi classes

Write a taxi simulator program that uses your Taxi and SilverServiceTaxi classes.
Each time, until they quit:

- The user should be able to choose from a list of available taxis,
- They can choose how far they want to drive,
- At the end of each trip, show them the trip cost and add it to their bill.
"""

from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MAIN_MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Main section of program"""
    total_trip_cost = 0
    current_taxi = None

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Lets drive!")
    print(MAIN_MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            try:
            except:
        elif menu_choice == "d":
            if:
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_trip_cost:.2f}")
        print(MAIN_MENU)
        menu_choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_trip_cost:.2f}")
    print(f"Taxis are now:\n{taxis}")


main()
