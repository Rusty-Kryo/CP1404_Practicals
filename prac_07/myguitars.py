"""
estimate:2 hr 45 mins (7:48 pm)
actual:

GitHub repository link: https://github.com/Rusty-Kryo/CP1404_Practicals

more guitars task, this program includes
- Opens the CSV file for reading
- Read the contents line by line
- Makes an object from the contents of the line
- Stores the objects into a list
- Asks the user for details about a new guitar
- Makes an object from the user input
- Saves the new guitar object into the same list
- Sorts the list based on age and display the list
- Opens the CSV file for writing
- Writes the contents of the list into the CSV file

"""

from prac_07.guitar import Guitar

guitar_file = "guitars.csv"

def main():
    """ Opens the CSV file for reading, read line by line, save line as object and display """
    # creates an empty list called guitars
    guitars = []
    with open(guitar_file, 'r') as file:
        # Extracts the contents of the CSV file line by line
        for line in file:
            # gets rid of the unnecessary spaces
            # creates a list containing the values separated by a ','
            line = line.strip().split(",")
            # print(line)  # for debugging
            # creates an object named guitar using the contents of line
            guitar = Guitar(line[0], int(line[1]), float(line[2]))
            # stores the object into the list called guitars
            guitars.append(guitar)

    # # (for debugging)
    # # prints the instance using string method of Guitar unsorted
    # print("guitars unsorted")
    # for guitar in guitars:
    #     print(guitar)

    # Acts the user to enter detials for a new guitar
    guitar_name = input("Guitar Name:").title()
    guitar_production_year = int(input("Guitar Production Year:"))
    guitar_price = float(input("Guitar Price:"))
    # makes an object for the
    new_guitar = Guitar(guitar_name, guitar_production_year, guitar_price)
    # adds the new guitar into the list called guitars
    guitars.append(new_guitar)

    # prints the instance using string method of Guitar sorted
    # print("guitars sorted")  # for debugging
    guitars.sort()
    for guitar in guitars:
        print(guitar)

    # saves the contents of the list into the same csv file, used in the beginning
    with open(guitar_file, 'w') as file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=file)

if __name__ == "__main__":
    main()
