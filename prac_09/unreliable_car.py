"""
estimate: 1hr 30mins
actual:

This code is the subclass of car called unreliable car for
week 9 coding practical.

"""
import random

from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(fuel, name)
        self.reliability = reliability

    def __str__(self):
        return f"{super().__str__()}, Reliability:{self.reliability}"

    def drive(self, distance):
        will_it_drive = random.randint(0, 101)
        if will_it_drive < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            print("Car Did Not Drive!!")

