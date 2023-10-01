"""
Code for practical 3, files task

1. Write code that asks the user for their name, then opens a file called
"name.txt" and writes that name to it. Remember to close your file.

2. (In the same file, but as if it were a separate program) Write code that opens
"name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file).

3. Create a text file called numbers.txt and save it in your prac directory.
Put the following three numbers on separate lines in the file and save it:
17
42
400

4. Write code that opens "numbers.txt", reads only the first two numbers and adds
them together then prints the result, which should be... 59.

Now write a fourth block of code that prints the total for all lines in numbers.txt
or a file with any number of numbers.

"""

# Task 1
name_file = 'user_name.txt'  # name of the file
Name_file = open(name_file, 'w')  # create/opens file with write mode

user_name = input("Type in User's Name:")  # Gets user's name and stores it into user_name
print(f"User's Name {user_name}", file=Name_file)

Name_file.close()  # closes the file

# Task 2
Name_file = open(name_file)
user_name = Name_file.read()
print(user_name)

# Task 3
number_file = 'numbers.txt'
Number_file = open(number_file, 'w')
numbers = [17, 42, 400]
for i, numbers in enumerate(numbers, 1):
    print(f"{numbers}", file=Number_file)
Number_file.close()

Number_file = open(number_file, 'r')
sum_of_numbers = 0
for i in range(1, 3, 1):
    numbers = int(Number_file.readline())
    sum_of_numbers += numbers

print("Total number:", sum_of_numbers)

Number_file.close()

# Task 4
Number_file = open(number_file, 'r')
sum_of_numbers = 0
for line in Number_file:
    numbers = int(line)
    sum_of_numbers += numbers

print("Total number:", sum_of_numbers)

Number_file.close()


