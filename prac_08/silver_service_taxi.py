"""
CP1404 Practical - SilverServiceTaxi Class which is derived from Taxi class derived from Car class
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Defines the Silver Service subset of Taxi's"""
    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise class"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of specifically a Silver Service Taxi with flag fall"""
        return f"{super().__str__()} plus flag fall of {self.flag_fall}"

    def get_fare(self):
        """Get the current fare"""
        return self.flag_fall + super().get_fare()
