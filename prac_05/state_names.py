"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
def main():
    print(CODE_TO_NAME)
    while True:
        state_code = input("Enter short state: ").upper()
        while state_code != "":
            if state_code in CODE_TO_NAME:
                print(f"{state_code:4} is {CODE_TO_NAME[state_code]}")
                break
            else:
                print("Invalid short state")
                state_code = input("Enter short state: ").upper()

main()
