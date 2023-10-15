
"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []  # pre-alocation
    num_of_months = int(input("How many months? "))

    for month in range(1, num_of_months + 1):
        # things to do 3
        # income = float(input("Enter income for month " + str(month) + ": "))
        income = float(input(f"Enter income fir mont {month} :"))
        incomes.append(income)

    print_income_report(incomes, num_of_months)


def print_income_report(incomes, num_of_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))
    # yes, it is only taking in what it needs, as seen above
    # it takes in income and number_of_months for processing
    # in the for loop

main()