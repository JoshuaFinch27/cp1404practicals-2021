"""
CP1404 Practical - Unreliable Car class created from Car
"""

from random import randint
from prac_08.car import Car


class UnreliableCar(Car):
    """Class for an unreliable car"""

    def __init__(self, name, fuel, reliability):
        """Initialise UnreliableCar class"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive car based on reliability"""
        if randint(0, 100) >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
