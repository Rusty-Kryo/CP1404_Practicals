"""
estimate:2 hr 45 mins (7:48 pm)
actual:

GitHub repository link: https://github.com/Rusty-Kryo/CP1404_Practicals

"""

from prac_07.guitar import Guitar


def main():
    """ Opens the CSV file for reading, read line by line, save line as object and display """
    # creates an empty list called guitars
    guitars = []
    with open("guitars.csv", "r") as guitar_file:
        # Extracts the contents of the CSV file line by line
        for line in guitar_file:
            # gets rid of the unnecessary spaces
            # creates a list containing the values separated by a ','
            line = line.strip().split(",")
            # print(line)  # for debugging
            # creates an instance named guitar
            guitar = Guitar(line[0], int(line[1]), float(line[2]))
            # adds the
            guitars.append(guitar)

    # prints the instance using string method of Guitar unsorted
    print("guitars unsorted")
    for guitar in guitars:
        print(guitar)

    # prints the instance using string method of Guitar sorted
    print("guitars sorted")
    guitars.sort()


if __name__ == "__main__":
    main()
