"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            Convert2Celsius()
        elif choice == "F":
            Covert2Celsius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def Covert2Celsius():
    # acquires a value from user
    fahrenheit = float(input("fahrenheit: "))
    # Hint: celsius = 5 / 9 * (fahrenheit - 32)
    # converts fahrenheit to celsius using the equation given as hint
    celsius = 5 / 9 * (fahrenheit - 32)
    # Remove the "pass" statement when you are done. It's a placeholder.
    # pass
    print(f"result:{celsius:.2f}C")


def Convert2Fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


