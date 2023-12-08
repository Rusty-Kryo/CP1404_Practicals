"""

Program for testing the unreliable car class program

"""

from prac_09.unreliable_car import UnreliableCar


def main():
    """Test the unreliable car class by running the following code."""
    for i in range(1, 100):
        my_car = UnreliableCar("Prius", 100, 50)
        my_car.drive(40)
        print(my_car)

        # # for debugging
        # my_car.add_fuel(40)
        # my_car.drive(60)
        # print(my_car)


main()
