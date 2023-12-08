"""
Program is used for testing the silver service taxi program
"""

from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Tests the SilverServiceTaxi class program."""
    my_fancy_taxi = SilverServiceTaxi("Tesla", 100, 2)
    # print(my_fancy_taxi.price_per_km) # for debugging
    my_fancy_taxi.start_fare()
    my_fancy_taxi.drive(18)
    # print(my_fancy_taxi.get_fare()) # for debugging
    fare = my_fancy_taxi.get_fare()
    print(f"For an {my_fancy_taxi._odometer}km trip in a SilverServiceTaxi with a "
          f"fanciness of {my_fancy_taxi.fanciness}, the fare should be {fare}")
    print(my_fancy_taxi)

main()