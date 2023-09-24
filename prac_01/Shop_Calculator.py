"""
Shop total price calculator

"""
menu = """ (T)otal price and apply discount if applicable
(Q)uit
Any number will be considered as an item price"""
print(menu)

Com = ""
n = 0
total = 0
items_list = []
while Com != "F":
    UI = "Enter Item's Price:$"
    user_in = input(UI).upper()
    if user_in == "E":
        if total >= 100:
            discount = total * 0.1
            total = total - discount
            print(f"total price of {n}items:${total:.2f}")
        else:
            print(f"total price of {n}items:${total:.2f}")
        n = 0
        total = 0
        items_list = []
    elif user_in == "Q":
        Com = "F"

    elif float(user_in) >= 0:
        price = float(user_in)
        #checks whether if input price is positive or not
        if price >= 0:
            # process of adding the current input to a list,
            # incrementing n and printing them in the terminal
            n = n + 1
            items_list = items_list + [price]
            for p in items_list:
                print("Price of items:$", p)

            total = total + price
            print(f"Total price:${total:.2f}")
        # validates input price
        elif price < 0:
            print("invalid entry, try again")


