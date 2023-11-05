"""
- stores the users emails as unique keys and names as values in a dictionary
- keeps on going until the user enters blank
- uses separate function to extract the name from the email as in the example below


estimate: 1hr 30 mins
actual:
"""

def main():
    email_dict = {}
    # get email from user
    email = input("Input Email\n>")
    while email != "":
        name = extract_name(email)
        choice_1 = input(f"Is your name, {name}? [Y/N]\n>").upper()
        if choice_1 == "Y":
            email_dict[email] = name
            print(f"email has been stored\n")
            email = input("Input Email\n>")
        elif choice_1 == "N":
            name = input("type your name\n>")
            email_dict[email] = name
            print(f"email has been stored\n")
            email = input("Input Email\n>")
        else:
            print("invalid entry")

    for emails in email_dict:
        print(f"{email_dict[emails]} ({emails})")

# process the email and extract the name
def extract_name(email):
    email_to_string = email.split("@")
    email_to_name = email_to_string.pop(0)
    email_to_name = email_to_name.strip("0123456789")
    if "_" in email_to_name:
        names = email_to_name.split("_")
    elif "." in email_to_name:
        names = email_to_name.split(".")
    else:
        names = email_to_name

    names = [name.title() for name in names]
    names = " ".join(names)
    print(names)


    return names


main()