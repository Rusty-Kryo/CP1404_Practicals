"""
Code for the basic list operation task for week 4 prac
- asks user for 4 numbers
- stores it in a list
- identifies
    > first and last number
    > largest and smallest number
    > average numbers


"""
req_num = 5 # amount of input numbers user type in
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 
             'NicolEye', 'swei45', 
             'BaseInterpreterInterface', 
             'BaseStdIn', 'Command', 'ExecState', 
             'InteractiveConsole', 'InterpreterInterface', 
             'StartServer', 'bob']

def main():
    while user_checker() == True:
        nums_list = []
        for i in range(1, req_num+1):
            num = int(input("Number:"))
            nums_list.append(num)
        print(nums_list)
        print(f"The first Number is {nums_list[0]}")
        print(f"the last number is {nums_list[req_num-1]}")
        smallest_num  = min(nums_list)
        largest_num = max(nums_list)
        print(f"The smallest number is {smallest_num}")
        print(f"The largest number is {largest_num}")
        average = calc_average(nums_list)
        print(f"The average of the numbers is {average}")


def calc_average(num):
    # average
    size_num = len(num)
    total = 0
    for i in range(0, 5):
        total = total + num[i]
    average = total / size_num
    return average
def user_checker():
    user_in = input("Input Username:")
    size = len(usernames)
    for i in range(0, size-1):
        if user_in == usernames[i]:
            print("Access Granted")
            return True
        else:
            print("Access Denied")
            break

main()

