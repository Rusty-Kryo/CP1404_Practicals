"""
estimated: 1hr 30mins
actual:1hr 23mins

"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """This class is a subclass of Taxi, which allows the scaling
        of fare depending on the fanciness."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Construct the instance for fanciness, call the init of Taxi
            and calculates the price per km of the fancy taxi. """
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def __str__(self):
        """Return the same string as taxi but with fanciness added."""
        return f"{super().__str__()} plus flagfall of {self.flagfall}"

    def get_fare(self):
        """Return the fare for the trip, including the flagfall."""
        fare = super().get_fare()
        return fare + self.flagfall
