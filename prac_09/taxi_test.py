"""
estimate: 2hrs
actual: 46 mins


This code tests the car and taxi Superclass
and Subclass

"""

from prac_09.taxi import Taxi


def main():
    """ Main program that contains the lines of codes used for testing"""
    # Task 1
    my_taxi = Taxi("Prius 1", 100)  #, 1.23)
    # print(my_taxi)
    # Task 2
    my_taxi.drive(40)
    # Task 3
    print(my_taxi)
    print(f"Current fare is ${my_taxi.get_fare():.2f}")
    # Task 4
    # my_taxi.price_per_km = 2.22  # for debug
    my_taxi.start_fare()
    my_taxi.drive(100)
    # Task 5
    print(my_taxi)
    print(f"Current fare is ${my_taxi.get_fare():.2f}")


main()
