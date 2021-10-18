"""
CP1404 Practical - Unreliable Car Tests
"""

from prac_08.unreliable_car import UnreliableCar


def main():
    """Test cars that have varying reliability"""
    great_car = UnreliableCar("Great Car", 100, 99)
    good_car = UnreliableCar("Good Car", 100, 85)
    decent_car = UnreliableCar("Decent Car", 100, 65)
    bad_car = UnreliableCar("Bad Car", 100, 45)
    really_bad_car = UnreliableCar("Really Bad Car", 100, 10)
    max_km_to_drive = int(input("Enter the max kn to drive: "))
    for i in range(1, max_km_to_drive):
        print("Attempting to drive {}km:".format(i))
        print(f"{great_car.name:12} drove {great_car.drive(i):2}km")
        print(f"{good_car.name:12} drove {good_car.drive(i):2}km")
        print(f"{decent_car.name:12} drove {decent_car.drive(i):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(i):2}km")
        print(f"{really_bad_car.name:12} drove {really_bad_car.drive(i):2}km")
    print(great_car)
    print(good_car)
    print(decent_car)
    print(bad_car)
    print(really_bad_car)


main()
