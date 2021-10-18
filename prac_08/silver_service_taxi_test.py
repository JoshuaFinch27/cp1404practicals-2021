"""
CP1404 Practical - SilverServiceTaxi Class Tests
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """SilverServiceTaxi Class Testing"""
    test_taxi_1 = SilverServiceTaxi("Hummer", 200, 4)
    test_taxi_1.drive(0)  # Output is the same as the Hummer example output
    print(test_taxi_1)
    print(f"${test_taxi_1.get_fare():.2f}")

    test_taxi_2 = SilverServiceTaxi("Cheap Limo", 150, 2)
    test_taxi_2.drive(18)
    print(test_taxi_2)
    print(f"${test_taxi_2.get_fare():.2f}")


main()
