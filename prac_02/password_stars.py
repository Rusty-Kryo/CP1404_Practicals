"""

password checker
- checks whether the user has typed in the correct password
- including the length of the password and the characters
- returns stars if the input password is 10 characters long

"""
valid = 'Correct Password'
invalid = 'Incorrect Password'
short = 'input too short'
password = input("Enter password:")

# checking password if it's correct
if len(password) == 10:
    if password == "Pythonista":
        print(valid)
else:
    print(short)

