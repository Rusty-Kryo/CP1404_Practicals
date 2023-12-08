"""
estimate: 1hr 30mins
actual: 1hr

This code is the subclass of car called unreliable car for
week 9 coding practical.

"""
import random
from prac_09.car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialise an unreliable car instance.
            reliability is a float, the chance it will drive.
        """
        super().__init__(fuel, name)
        self.reliability = reliability

    def __str__(self):
        """Returns a string like car but with reliability."""
        return f"{super().__str__()}, Reliability:{self.reliability}"

    def drive(self, distance):
        """Drive the car like the car class, with the addition of checking
        if it will drive or not."""
        will_it_drive = random.randint(0, 101)
        if will_it_drive < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven

        else:
            print("Car Did Not Drive!!")
