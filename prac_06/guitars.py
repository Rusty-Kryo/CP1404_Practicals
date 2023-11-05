"""

Playing guitar (not really) task

"""

from prac_06.guitar import Guitar

def main():
    guitars = []
    menu = ("D - Display My Guitar List"
            "\nA - Add guitar"
            "\nQ - Quit"
            "\n>>>")
    while True:
        print("My List!")
        com = input(menu).upper()

        if com == "D":
            print("--- My Guitars ---")
            for i, guitar in enumerate(guitars, 1):
                vintage_info = "(vintage)" if guitar.is_vintage() else ""
                print(f"Guitar {i:2}: {guitar.name} ({guitar.year}), worth ${guitar.cost:.2f} {vintage_info}")

        elif com == "A":
            print("Add Guitar Details")
            name = input("Name:")
            year = int(input("Year:"))
            cost = float(input("cost: $"))

            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)
            print(f"{str(new_guitar)} has been added.")

        elif com == "Q":
            break

        else:
            print("Invalid Input!")


try:
    main()
except Exception as Error:
    print(f"{Error} has occured")