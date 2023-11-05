"""
estimated: 10 mins
actual: 11 mins

GitHub repository link: https://github.com/Rusty-Kryo/CP1404_Practicals

edited to satisfy clean coding

Class for the more guitars task,
"""

class Guitar:
    """ Represents information about Guitars"""
    def __init__(self, name="", year=0, cost=0):
        """ Builds a Guitar based on the given values"""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """ Returns the current age of the guitar """
        return 2023 - self.year

    def is_vintage(self):
        """ Checks whether the guitar is vintage"""
        return self.get_age() >= 50

    def __str__(self):
        """ Returns a string format for printing"""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """ Checks which guitar is older"""
        return self.year < other.year