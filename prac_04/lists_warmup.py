"""
1. what values do the following expression has?
    - numbers[0] = 3
    - numbers[-1] = 2
    - numbersp[3] = 1
    - numbers[:-1] = all except 2
    - numbers[3:4] = exclude first 3 and include only the
    first 4 therefore, its 1
    - 5 in numbers = true because there is a number 5 in
    the list
    - 7 in numbers = false because there is no number 7 in
    th elist
    - "3" in numbers = false because the 3 in the list is not
    a string its an integer
    - numbers + [6, 5 , 3] = will add [6, 5, 3] into the
    list called numbers


"""

#numbers = [3, 1, 4, 1, 5, 9, 2]
numbers = ["ten", 1, 4, 1, 5, 9, 1]

a = numbers[2:]
b = 9 in numbers
print(a)
print(b)
