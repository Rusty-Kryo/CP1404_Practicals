"""
estimate:
actual:

program for a taxi driving simulator including a UI

"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = ("q)uit, c)hoose taxi, d)rive"
        "\n>>>")


# from prac_09

def main():
    """Main Function for the taxi simulator program"""
    # Create the Taxi instance
    prius = Taxi("Prius", 100)
    limo = SilverServiceTaxi("Limo", 100, 2)
    hummer = SilverServiceTaxi("Hummer", 100, 4)
    # Store each in a list called taxis
    taxis = [prius, limo, hummer]
    # print(taxis)  # for debugging
    # Set initial bill to date to 0
    bill_to_date = 0
    # Ask the user for a choice
    choice = input(MENU).lower()

    while choice != "q":
        try:
            if choice == "c":
                # display taxi list
                for i, taxi in enumerate(taxis, 1):
                    print(f"{i}) {taxi}")

                chosen_taxi = int(input("Choose Taxi:"))
                taxis[chosen_taxi - 1].start_fare()

            elif choice == "d":
                # Ask for the trip distance.
                trip_distance = int(input("Drive How Far?:"))
                # Drive the taxi.
                taxis[chosen_taxi-1].drive(trip_distance)
                # Display the current fare.
                current_bill = taxis[chosen_taxi - 1].get_fare()
                bill_to_date += current_bill
                print(f"Your {taxis[chosen_taxi - 1].name} trip cost you ${current_bill:.2f}")

        except ValueError:
            print("Invalid Input try again")
        except UnboundLocalError:
            print("Choose A Taxi")

        # Print the bill to date.
        print(f"Bill To Date:${taxis[chosen_taxi - 1].get_fare():.2f}")
        # Ask for the choice again.
        choice = input(MENU).lower()




main()
