"""
Write a program to read this file, process the data and display processed information.
    - the champions and how many times they have won.
    - the countries of the champions in alphabetical order

"""
file_name = "wimbledon.csv"
def main():
    winner_to_numofwins = {}
    country_to_numofwins = {}
    with open(file_name, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
            line = line.split(",")

            if line[1] in country_to_numofwins:
                country_to_numofwins[line[1]] += 1
            else:
                country_to_numofwins[line[1]] = 1

            if line[2] in winner_to_numofwins:
                winner_to_numofwins[line[2]] += 1
            else:
                winner_to_numofwins[line[2]] = 1

        longest_length = find_long_name(winner_to_numofwins.keys())
        winner_to_numofwins_sorted = sorted(winner_to_numofwins.items())
        for winner, numofwins in winner_to_numofwins_sorted:
            print(f"{winner:{longest_length}} {numofwins}")

        winnning_country = ",".join(country_to_numofwins.keys())

        print(f"winning countries: {winnning_country}")




def find_long_name(names):
    name_length = []
    for name in names:
        length = len(name)
        name_length.append(length)

    longest_length = max(name_length)

    return longest_length



main()