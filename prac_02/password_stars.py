"""

password checker
- checks whether the user has typed in the correct password
- including the length of the password and the characters
- returns stars if the input password is 10 characters long

"""
menu = 'Enter Password'
valid = 'Correct Password'
not_valid = 'Incorrect Password'
short = 'input too short'

def main():
    print(menu)

    password = Password_getncheck()
    valid


def Password_getncheck():
    password = input()
    # checking password if it's correct
    if len(password) <= 10:

        print(short)

    password_check(password)

def password_check(password):
    if password == "Pythonista":
        print(valid)
        print('*' * len(password))


main()
