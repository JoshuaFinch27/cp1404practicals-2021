"""
CP1404 Practical - Test Taxi Inherited Class
"""

from prac_08.taxi import Taxi


def main():
    """Test Taxi class (inherited from Car class)"""
    my_taxi = Taxi("Prius 1", 100, 1.23)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)


main()
