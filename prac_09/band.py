"""
estimate: 2 hrs
actual:


Band class for my_band

"""
from prac_09.musician import Musician


class Band:
    """Is the superclass for musician."""

    def __init__(self, name):
        """Construct a band with name and empty members collection"""
        self.name = name
        self.members = []

    def play(self):
        """Goes through each of the member and displays what guitar they play"""
        for member in self.members:
            print(member.play())

    def add(self, member_details):
        """Adds another member"""
        self.members.append(member_details)

    def __str__(self):
        """Returns a string value for this class."""
        return f"{self.name} {self.members}"
