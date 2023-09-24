"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
# Makes a menu and asks for the sales that
# will be used for calculation
menu = "User Sales Based Bonus Calculator"
print(menu)
sales = float(input("Enter Sales:$"))

while sales >= 0:
    # Calculations process
    if sales < 1000:
        bonus = 0.1
        total = sales*bonus
        print(total)
    elif sales > 1000:
        bonus = 0.15
        total = sales * bonus
        print(total)
    else:
        print("invalid input")

    print(menu)
    sales = float(input("Enter Sales:$"))

print("Thank You")

