"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    - when a non-numerical input is detected.
2. When will a ZeroDivisionError occur?
    - when the denominator is either a zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    - make it so that it will not take a 0 for an input
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # Makes sure that denominator is never equal to zero
    while denominator == 0:
        print("denominator can't be zero")
        denominator = int(input("Enter the denominator: "))


    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

print("Finished.")