"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():

    data = get_data()
    print(data)
    size = len(data[1])
    for i in range(1, size + 1):
        print(f"{data[i][0]} is taught by {data[i][1]} and has {data[i][2]} students ")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    datas = []
    input_file = open(FILENAME)

    for line in input_file:
        line = line.strip().split(',')  # Separate the data into its parts
        line[2] = int(line[2])
        #print(line)  # See if that worked

        datas.append(line)

    input_file.close()
    return datas

main()