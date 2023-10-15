"""
Hex Colour dictionary
- takes in colour name the hex code (#XXXXXX)
- with error handling for incorrect input
- continously runs until user enters blank ("")

"""

HEX_COL = {"ABSOLTE ZERO": "#0048BA", "ACIDE GREEN": "#B0BF1A", "BRINK PINK": "#FB607F", "BRONZE": "#CD7F32",
           "CAMEL": "#C19A6B", "CANDY APPLE RED": "#FF0800", "EMINENCE": "#6C3082", "EGGSHELL": "#F0EAD6",
           "GOLDENROD": "#DAA520", "JAPANESE CARMINE": "#9D2933"}


def main():
    print(HEX_COL)
    colour = input("Enter Colour Name:").upper()
    while colour != "":
        if colour in HEX_COL:
            print(f"Hex Colour code for {colour} is\t{HEX_COL[colour]}")
            colour = input("Enter Colour Name:").upper()
        else:
            print("Invalid Colour, try again")
            colour = input("Enter Colour Name:").upper()


main()
